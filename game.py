from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import math


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        # for i in 0,1,2
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # return list of available spots
        # a spot is available if it contains a ' ' and not an x or o
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def num_empty_squares(self):
        return self.board.count(' ')

    def not_over(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):

        row_ind = math.floor(square / 3)
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([s == letter for s in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([s == letter for s in column]):
            return True

        if square % 2 == 0:

            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.not_over():
        # get_move is in Player class because sub-class gets their moves differently
        # HumanPlayer takes input, RandomComputerPlayer picks at random and GeniusComputerPlayer uses minimax
        if letter == '0':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            print(letter + f' makes a move to square {square}')
            if print_game:
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print(f'{letter} won the game!')
                return letter

            if letter == 'X':
                letter = '0'
            else:
                letter = 'X'

    if print_game:
        print("It's a tie!")


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    # o_player = RandomComputerPlayer('0')
    o_player = GeniusComputerPlayer('0')
    t = TicTacToe()
    play(t, x_player, o_player)
