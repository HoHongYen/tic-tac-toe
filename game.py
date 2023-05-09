import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        print('Bảng đánh số vị trí: ')
        # 0 | 1 | 2
        # number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        number_board = [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):

    # if print_game:
    #     game.print_board_nums()

    letter = 'X'
    turn = 1
    while game.empty_squares():
        if print_game:
            print('------------- Lượt đi thứ {} ------------------------'.format(turn))
            game.print_board_nums()
        turn += 1
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                if letter == 'X':
                    print('Máy (X) đánh vào ô số {}'.format(square+1))
                else:
                    print('Người chơi (O) đánh vào ô số {}'.format(square+1))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    if (letter == 'X'):
                        print('Máy (X) thắng!')
                    else:
                        print('Người chơi (O) thắng!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player
        if (print_game):
            time.sleep(.8)

    if print_game:
        print('Kết quả: hòa!')



# if __name__ == '__main__':
#     x_player = SmartComputerPlayer('X')
#     o_player = HumanPlayer('O')
#     t = TicTacToe()
#     play(t, x_player, o_player, print_game=True)


# check win times with random computer player
if __name__ == '__main__':
    cnt_x = 0
    cnt_o = 0
    cnt_ties = 0
    number_of_game = 100
    for _ in range(number_of_game):
        x_player = SmartComputerPlayer('X')
        o_player = RandomComputerPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == 'X':
            cnt_x += 1
        elif result == 'O':
            cnt_o += 1
        else: cnt_ties += 1
    print(f'Sau {number_of_game} trận ta có: \n- Máy (X) thắng {cnt_x} trận \n- Máy chơi random (O) thắng {cnt_o} trận \n- Số trận hòa là {cnt_ties}')


