import random

from player import Player
import copy
import time


class Halma:
    def __init__(self):

        self.board = []
        self.player2 = Player(2)
        self.player1 = Player(1)
        self.moves = set()
        self.base1 = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1),
                      (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1)}
        self.base2 = {(15, 15), (15, 14), (15, 13), (15, 12), (15, 11), (14, 15), (14, 14), (14, 13), (14, 12),
                      (14, 11),
                      (13, 15), (13, 14), (13, 13), (13, 12), (12, 15), (12, 14), (12, 13), (11, 15), (11, 14)}

    def read_board_from_file(self, file):
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    row = list(map(int, line.strip().split()))
                    self.board.append(row)
        except FileNotFoundError:
            print('nie ma pliku')
        # print(type(self.board[0][0]))

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
        self.print_board()

    def game(self):
        while self.check_winner() is None:
            move_2 = self.player2.minmax(([], self.board), 1, False,self.player2.evaluate)
            self.make_move1(move_2)
            print('ruch 2')
            move_1 = self.player1.minmax(([], self.board), 1, True,  self.player1.evaluate)
            self.make_move1(move_1)
            print('ruch 1')
            self.print_board()
            # move_2 = self.player2.minmax(([], self.board), 1, False)
            # self.make_move1(move_2)
            # print('ruch 2')
        print(self.check_winner())

    def game_alpha_beta(self, depth):
        rounds = 0;
        while self.check_winner() is None:
            # move_2 = self.player2.minimax_alpha_beta(([], self.board), depth, False, self.player2.evaluate1,
            #                                          float('-inf'), float('inf'))
            # self.make_move1(move_2)
            # print('ruch 2')
            # self.print_board()
            move_1 = self.player1.minimax_alpha_beta(([], self.board), depth, True, self.player1.evaluate3, float('-inf'), float('inf'))
            self.make_move1(move_1)
            print('ruch 1')
            self.print_board()
            move_2 = self.player2.minimax_alpha_beta(([], self.board), depth, False, self.player2.evaluate1, float('-inf'), float('inf'))
            self.make_move1(move_2)
            print('ruch 2')
            self.print_board()
            # move_2 = self.player2.minmax(([], self.board), 1, False)
            # self.make_move1(move_2)
            # print('ruch 2')
            # self.print_board()
            rounds += 1
            print(rounds)
        print(self.check_winner())
        print(rounds)

    def test(self):
        self.player1.minimax_alpha_beta(([], self.board), 4, True, self.player1.evaluate, float('-inf'), float('inf'))


if __name__ == "__main__":
    halma = Halma()
    # halma.read_board_from_file('halmaWinner.txt')
    halma.generate_random_board()
    # halma.possile_moves(4, 0, 0)
    # # print(halma.moves)
    # # print(halma.check_winner())
    # # halma.game()
    # halma.all_possible_moves(1)
    # halma.print_board()# print(len(halma.base1))
    # # halma.make_move((4,0), (5,0))
    # print('nowa')
    # halma.print_board()
    # halma.player.make_move(halma.board, (4,0), (5,0))
    # halma.player.all_possible_moves(halma.board, 1)
    # a = halma.player1.minmax(([], halma.board), 2, True)
    # print(a)
    # alpha = halma.player1.minimax_alpha_beta(([], halma.board),2, True, float('-inf'), float('inf'))
    # print(alpha)

    start_time = time.time()
    a = halma.player1.minmax(([], halma.board), 2, True, halma.player1.evaluate)
    end_time = time.time()
    execution_time_minmax = end_time - start_time
    print(a)
    halma.generate_random_board()

    start_time = time.time()
    alpha = halma.player1.minimax_alpha_beta(([], halma.board), 2, True, halma.player1.evaluate, float('-inf'), float('inf'))
    end_time = time.time()
    execution_time_alpha_beta = end_time - start_time
    print(alpha)
    print("Czas wykonania algorytmu Minimax:", execution_time_minmax)
    print("Czas wykonania algorytmu Minimax z cięciami alfa-beta:", execution_time_alpha_beta)
    # halma.game_alpha_beta(2)
    # halma.player1.minimax_alpha_beta(([],halma.board), 2,True,halma.player1.evaluate, float('-inf'), float('inf'))
    # halma.generate_random_board()
    # halma.player1.test(([],halma.board), halma.player1.evaluate)
