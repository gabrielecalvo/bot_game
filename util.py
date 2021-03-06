import importlib.util
import shutil
from pathlib import Path
from typing import List

import pandas as pd
import plotly.express as px

from bot_game import Bot

EXAMPLES_FOLDER = Path("examples")
DOWNLOAD_FOLDER = Path("downloads")
DOWNLOAD_FOLDER.mkdir(exist_ok=True)


def save_code_to_file(code: str, filename: str):
    fpath = DOWNLOAD_FOLDER / f"{filename}.py"
    with open(fpath, "w") as fh:
        fh.write(code)

    return fpath


def save_file(filename: str, filebytes: bytes):
    fpath = DOWNLOAD_FOLDER / filename
    with open(fpath, "wb") as fh:
        fh.write(filebytes)

    return fpath


def import_file(fpath: Path):
    spec = importlib.util.spec_from_file_location(fpath.parts[-1], str(fpath))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def validate_file(fpath: Path):
    m = import_file(fpath)
    assert hasattr(m, "strategy"), "The file does not have a function called `strategy`"
    assert callable(
        m.strategy
    ), "The variable `strategy` is not callable! Is it a function?"


def build_all_bots() -> List[Bot]:
    bots = []
    for fp in DOWNLOAD_FOLDER.glob("*.py"):
        bot = Bot(name=fp.stem)
        m = import_file(fp)
        bot.strategy_func = m.strategy
        bots.append(bot)

    return bots


def add_example_bots():
    for fp in EXAMPLES_FOLDER.glob("*.py"):
        shutil.copy(fp, DOWNLOAD_FOLDER / fp.parts[-1])


def plot_grand_prix_results(winnings, x_col="Bot", y_col="Races Won"):
    podium_df = (
        pd.Series(winnings, name=y_col)
        .sort_values(ascending=False)
        .rename_axis(x_col)
        .reset_index()
    )

    fig = px.bar(podium_df, x=x_col, y=y_col, color=y_col)
    return fig


def create_animation(df):
    fig = px.scatter(
        df.assign(
            size=10,
        ),
        x="position",
        y="name",
        animation_frame="round",
        animation_group="name",
        size="size",
        color="name",
        hover_data=["direction", "last_action", "action_order"],
        hover_name="name",
        range_x=[0, 10],
    )
    return fig


def delete_all_bots():
    for fp in DOWNLOAD_FOLDER.glob("*.py"):
        fp.unlink()
