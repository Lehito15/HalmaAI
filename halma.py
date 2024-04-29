import random

from player import Player
import copy
import time


class Halma:
    def __init__(self):

        self.board = []
        self.player2 = Player()
        self.player1 = Player()
        self.moves = set()
        self.base1 = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1),
                      (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1)}
        self.base2 = {(15, 15), (15, 14), (15, 13), (15, 12), (15, 11), (14, 15), (14, 14), (14, 13), (14, 12),
                      (14, 11),
                      (13, 15), (13, 14), (13, 13), (13, 12), (12, 15), (12, 14), (12, 13), (11, 15), (11, 14)}

    def read_board_from_file(self, file):
        self.board = []
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    row = list(map(int, line.strip().split()))
                    self.board.append(row)
        except FileNotFoundError:
            print('nie ma pliku')

    def check_winner(self):
        win2 = all(self.board[x][y] == 2 for x, y in self.base1)
        win1 = all(self.board[x][y] == 1 for x, y in self.base2)
        if win2:
            return 2
        if win1:
            return 1
        return None

    def make_move(self, old_pos, new_pos):
        x, y = old_pos
        x_new, y_new = new_pos
        temp = self.board[x][y]
        self.board[x][y] = self.board[x_new][y_new]
        self.board[x_new][y_new] = temp

    def make_move1(self, move):
        if move[0] != []:
            pos_old, pos_new = move[0][0]
            x, y = pos_old
            x_new, y_new = pos_new
            temp = self.board[x][y]
            # print(temp, 'ruch')
            self.board[x][y] = self.board[x_new][y_new]
            self.board[x_new][y_new] = temp

    def print_board(self):
        for row in self.board:
            print(' '.join(str(cell) for cell in row))

    def generate_random_board(self):
        self.board = [[0] * 16 for _ in range(16)]
        number_of_1 = 0
        number_of_2 = 0
        while number_of_1 != 19:
            x = random.randrange(0, 16)
            y = random.randrange(0, 16)
            if self.board[x][y] == 0:
                self.board[x][y] = 1
                number_of_1 += 1
        while number_of_2 != 19:
            x = random.randrange(0, 16)
            y = random.randrange(0, 16)
            if self.board[x][y] == 0:
                self.board[x][y] = 2
                number_of_2 += 1

    def game(self):
        while self.check_winner() is None:
            move_2 = self.player2.minmax(([], self.board), 1, True, self.player2.strategy_offensive)
            self.make_move1(move_2)
            print('ruch 2')
            move_1 = self.player1.minmax(([], self.board), 1, False, self.player1.strategy_offensive)
            self.make_move1(move_1)
            print('ruch 1')
            self.print_board()
        print(self.check_winner())

    def game_alpha_beta(self, depth, h1, h2):
        rounds = 0
        while self.check_winner() is None:
            move_2 = self.player2.minimax_alpha_beta(([], self.board), depth, False, h2, float('-inf'), float('inf'))
            self.make_move1(move_2)
            # print('ruch 2')
            # self.print_board()
            move_1 = self.player1.minimax_alpha_beta(([], self.board), depth, True, h1, float('-inf'), float('inf'))
            self.make_move1(move_1)
            # print('ruch 1')
            # self.print_board()
            # move_2 = self.player2.minimax_alpha_beta(([], self.board), depth, False, h2, float('-inf'), float('inf'))
            # self.make_move1(move_2)
            # print('ruch 2')
            # self.print_board()

            rounds += 1
            if rounds > 300:
                points_1 = self.player1.count_pawns_in_base(self.board, self.player1.base2, 1)
                points_2 = self.player1.count_pawns_in_base(self.board, self.player1.base1, 2)
                if points_1 > points_2:
                    return 1
                elif points_2 > points_1:
                    return 2
                else:
                    return 0

            # print(rounds)
        # print(self.check_winner())
        # print(rounds)
        return self.check_winner()


if __name__ == "__main__":
    halma = Halma()
    halma.read_board_from_file('halmaWinner.txt')
    # halma.generate_random_board()

    a  = halma.game_alpha_beta(2, halma.player1.strategy_ofensivev2, halma.player1.strategy_go_in_group)
    print(a)

