from player import Player
class Halma:
    def __init__(self):

        self.board = []
        self.player = Player(1)
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
        print(type(self.board[0][0]))

    # def test(self, x, y, jump):
    #     moves = set()
    #     possile_moves1(x,y,jump)
    #
    #         # print(self.moves)
    #
    # def possile_moves1(self,x, y, jump):
    #     # moves = set()
    #     base1 = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1),
    #              (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1)}
    #     base2 = {(15, 15), (15, 14), (15, 13), (15, 12), (15, 11), (14, 15), (14, 14), (14, 13), (14, 12), (14, 11),
    #              (13, 15), (13, 14), (13, 13), (13, 12), (12, 15), (12, 14), (12, 13), (11, 15), (11, 14)}
    #
    #     # print(x,' ', y)
    #     if self.board[x][y] == 0 and jump == 0:
    #         return []
    #     for i in range(-1, 2):
    #         for j in range(-1, 2):
    #             new_y = y + j
    #             new_x = x + i
    #             if 0 <= new_y < 16 and 0 <= new_x < 16:
    #                 if self.board[new_x][new_y] == 0 and jump == 0:
    #                     print('dadaje 1 ', new_x, ' ', new_y)
    #                     # if self.board[x][y] == 1 and (x, y) in base2 and (new_x, new_y) not in base2:
    #
    #                     moves.add((new_x, new_y))
    #                 elif self.board[new_x][
    #                     new_y] != 0 and jump == 0 and 0 <= new_x + i < 16 and 16 > new_y + j >= 0 == \
    #                         self.board[new_x + i][new_y + j] and (new_x + i, new_y + y) not in self.moves:
    #                     print('dadaje 2 ', new_x + i, ' ', new_y + j)
    #                     moves.add((new_x + i, new_y + j))
    #                     possile_moves1(new_x + i, new_y + j, 1)
    #                 elif jump == 1 and self.board[new_x][
    #                     new_y] != 0 and 0 <= new_x + i < 16 and 16 > new_y + j >= 0 == \
    #                         self.board[new_x + i][new_y + j] and (new_x + i, new_y + j) not in self.moves:
    #                     print('skok ', new_x + i, ' ', new_y + j)
    #                     moves.add((new_x + i, new_y + j))
    #                     possile_moves1(new_x + i, new_y + j, 1)
    #                 else:
    #                     pass
    def possile_moves(self, x, y, jump=0):
        # moves = set()

        print(x,' ', y)

        if self.board[x][y] == 0 and jump == 0:
            return []
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_y = y + j
                new_x = x + i
                if 0 <= new_y < 16 and 0 <= new_x < 16:
                    if self.board[new_x][new_y] == 0 and jump == 0:
                        print('dadaje 1 ', new_x, ' ', new_y)
                        if (self.board[x][y] == 1 and (x, y) in self.base2 and (new_x, new_y) not in self.base2) or (
                                self.board[x][y] == 2 and (x, y) in self.base1 and (new_x, new_y) not in self.base1):
                            pass
                        else:
                            self.moves.add((new_x, new_y))
                    elif self.board[new_x][new_y] != 0 and jump == 0 and 0 <= new_x + i < 16 and 16 > new_y + j >= 0 == \
                            self.board[new_x + i][new_y + j] and (new_x + i, new_y + y) not in self.moves:
                        print('dadaje 2 ', new_x + i, ' ', new_y + j)
                        if (self.board[x][y] == 1 and (x, y) in self.base2 and (new_x, new_y) not in self.base2) or (
                                self.board[x][y] == 2 and (x, y) in self.base1 and (new_x, new_y) not in self.base1):
                            pass
                        else:
                            self.moves.add((new_x + i, new_y + j))
                        self.possile_moves(new_x + i, new_y + j, 1)
                    elif jump == 1 and self.board[new_x][new_y] != 0 and 0 <= new_x + i < 16 and 16 > new_y + j >= 0 == \
                            self.board[new_x + i][new_y + j] and (new_x + i, new_y + j) not in self.moves:
                        print('skok ', new_x + i, ' ', new_y + j)
                        if (self.board[x][y] == 1 and (x, y) in self.base2 and (new_x, new_y) not in self.base2) or (
                                self.board[x][y] == 2 and (x, y) in self.base1 and (new_x, new_y) not in self.base1):
                            pass
                        else:
                            self.moves.add((new_x + i, new_y + j))
                        self.possile_moves(new_x + i, new_y + j, 1)
                    else:
                        pass
        # print(self.moves)
    def all_possible_moves(self,player):
        i = 0
        j = 0
        self.moves = set()
        all_moves = {}
        for row in self.board:
            for element in row:
                if element == player:
                    self.possile_moves(i, j)
                    all_moves[(i, j)] = self.moves
                    self.moves = set()
                j += 1

            i += 1
            j = 0
        print(all_moves)

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

    def print_board(self):
        for row in self.board:
            print(' '.join(str(cell) for cell in row))




halma = Halma()

halma.read_board_from_file('halma1.txt')
# halma.possile_moves(4, 0, 0)
# # print(halma.moves)
# # print(halma.check_winner())
# # halma.game()
# halma.all_possible_moves(1)
halma.print_board()# print(len(halma.base1))
halma.make_move((4,0), (5,0))
print('nowa')
halma.print_board()
halma.player.evaluate(halma.board)
