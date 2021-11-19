import random
import math


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_moves())


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):

        valid_move = False
        while not valid_move:
            try:
                square = input(self.letter + '\'s turn. Choose a square between 0-9')
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_move = True
            except ValueError:
                print("Invalid value chosen. Try again")
        return val


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # pick square from minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        # state = screenshot of the game at that point
        max_player = self.letter
        other_player = '0' if player == 'X' else 'X'

        # base case - previous move led to a winning move
        if state.current_winner == other_player:
            # we return position & the score
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                                    state.num_empty_squares() + 1)}
        elif not state.not_over():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # step 1: try that spot
            state.make_move(possible_move, player)

            # step 2: recurse minimax, simulate the game using minimax
            sim_score = self.minimax(state, other_player)  # change the player

            # step 3: undo the move
            state.board[possible_move] = ' '  # change board to previous state of blank
            state.current_winner = None  # reset winner to None
            sim_score['position'] = possible_move

            # step 4: update the dictionary if needed
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score  # maximize the max_player
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score  # minimize the other_player
        return best
