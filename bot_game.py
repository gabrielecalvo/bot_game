import random


class Game:
    n_squares = 10
    winner = None

    def __init__(self, bots, verbose=False):
        self.bots = bots
        self.verbose = verbose

        self._set_starting_positions()

    def _set_starting_positions(self):
        for b in self.bots:
            b.position = 0

    def show_board(self):
        print("=" * 30)
        board = {i: [] for i in range(self.n_squares + 1)}
        for bot in self.bots:
            board[bot.position].append(bot)

        for square, bots_in_square in board.items():
            print(f"{square}: {bots_in_square}")

    def play_round(self):
        if self.winner is None:
            random.shuffle(self.bots)
            if self.verbose:
                print(self.bots)

            for bot in self.bots:
                self._play_bot(bot)
                if self.winner:
                    break

            for bot in self.bots:
                bot.direction = 1

        if self.verbose:
            if self.winner:
                print(f"========== Race Over, WINNER: {self.winner} ========== ")
            self.show_board()

    def _play_bot(self, bot):
        bot_position_dictionary = {b: b.position for b in self.bots}

        action_str = bot.play(bot_position_dictionary)
        if action_str == "walk":
            pos_from, pos_to = bot.walk()
            if self.verbose:
                print(f"{str(bot):<15} walked from {pos_from} to {pos_to}")
        elif action_str == "sabotage":
            sabotaged_bots = bot.sabotage(self.bots)
            if self.verbose:
                print(f"{str(bot):<15} sabotaged {sabotaged_bots}")

        if bot.position >= self.n_squares:
            self.winner = bot


class Bot:
    position = 0
    direction = 1
    strategy_func = None

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}Bot"

    def walk(self):
        from_position = self.position
        self.position = max(0, self.position + self.direction)
        to_position = self.position
        return from_position, to_position

    def sabotage(self, bots):
        sabotaged_bots = []
        for bot in bots:
            if bot.position == self.position and bot != self:
                bot.direction = -1
                sabotaged_bots.append(bot)
        return sabotaged_bots

    def play(self, bot_positions):
        if self.strategy_func is not None:
            return self.strategy_func(bot_positions)

        return random.choice(["walk", "sabotage"])


def grand_prix(bots, n=1000, prog_bar=None):
    winnings = {b: 0 for b in bots}
    for i in range(n):
        game = Game(bots, verbose=False)
        while game.winner is None:
            game.play_round()
        winnings[game.winner] += 1

        if prog_bar:
            prog_bar.progress((i + 1) / n)

    return winnings
