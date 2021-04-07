import subprocess
from pathlib import Path


def main():
    fp = Path(__file__).parent / "app.py"
    subprocess.call(f"streamlit run {fp}")


if __name__ == "__main__":
    main()
