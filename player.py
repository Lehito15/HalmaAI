# from halma import Halma
import copy
import random
import evaluation


class Player:
    def __init__(self, type):
        self.type = type
        self.moves = set()

        self.base1 = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1),
                      (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1)}
        self.base2 = {(15, 15), (15, 14), (15, 13), (15, 12), (15, 11), (14, 15), (14, 14), (14, 13), (14, 12),
                      (14, 11),
                      (13, 15), (13, 14), (13, 13), (13, 12), (12, 15), (12, 14), (12, 13), (11, 15), (11, 14)}

    def evaluate(self, state):
        heuristic_value = 0
        point_x, point_y = -1, -1

        x = 0
        y = 0
        if self.type == 1:
            base = self.base1
            rival_base = self.base2
        else:
            base = self.base2
            rival_base = self.base1
        # print('evalu')
        # print(len(state))
        for row in state[1]:
            for element in row:
                # print(element)
                if (element == self.type):
                    # print(x, ' ', y)
                    # print(abs(point_x - x) + abs(point_y - y))
                    heuristic_value += evaluation.manhatan(point_x,point_y, x, y)
                y += 1
            x += 1
            y = 0
        # print(heuristic_value, ' heyrestyka')
        # print(state[0])
        return heuristic_value

    def evaluate1(self, state):
        heuristic_value = 0
        point_x, point_y = 0, 0

        x = 0
        y = 0
        if self.type == 1:
            base = self.base1
            rival_base = self.base2
        else:
            base = self.base2
            rival_base =  self.base1
        if state:

            heuristic_value += evaluation.leave_base(self.type, state, base)

            for row in state[1]:
                for element in row:
                    if element == self.type:
                        heuristic_value += evaluation.if_in_base(self.type, base, state[1], x, y)
                        heuristic_value += evaluation.manhatan(point_x,point_y, x, y)
                        heuristic_value += evaluation.rival_base(self.type,state[1], rival_base, x, y)
                    y += 1
                x += 1
                y = 0
            # print(heuristic_value, ' heyrestyka')
            # print(state[0])
        return heuristic_value

    def evaluate3(self, state):
        heuristic_value = 0
        point_x, point_y = 0, 0
        if self.type == 1:
            base = self.base1
            rival_base = self.base2
        else:
            base = self.base2
            rival_base = self.base1

        x = 0
        y = 0
        heuristic_value += evaluation.leave_base(self.type, state, base)
        # print('evalu')
        # print(len(state))
        for row in state[1]:
            for element in row:
                # print(element)
                if (element == self.type):

                    heuristic_value += evaluation.go_in_group(self.type, state[1], base, x, y)
                    heuristic_value += evaluation.manhatan(point_x,point_y, x, y)
                    heuristic_value += evaluation.if_in_base(self.type, base, state[1], x, y)
                    # heuristic_value += evaluation.rival_base(self.type, state[1], rival_base, x, y)
                y += 1
            x += 1
            y = 0
        # print(heuristic_value, ' heyrestyka')
        # print(state[0])
        return heuristic_value

    def minmax(self, game, depth, is_maximizing, evaluation):
        # if game.check_winner() == None:
        #     return self.evaluate(game)
        # print(type(game))
        # print('elo320')
        # print(game)

        if depth == 0:
            # print('koniec')
            # print(game)
            return game[0], evaluation(game)
        if self.check_winner(game[1]):
            print('winn')
            return game[0], evaluation(game)

        if is_maximizing:
            moves = self.all_possible_moves(game, 1)
        else:
            moves = self.all_possible_moves(game, 2)

        # moves = self.all_possible_moves(game, self.type)
        best_move = None
        if is_maximizing:
            max_eval = (None, float('-inf'))
            # print('pruntyje grę')
            # print(game)
            for move in moves:
                # print(move, 'move')
                new_board = self.make_move(game, move[0], move[1])
                eval = self.minmax(new_board, depth - 1, False, evaluation)

                if eval[-1] > max_eval[-1]:
                    max_eval = eval
                if eval[-1] == max_eval[-1]:
                    max_eval = random.choice([max_eval, eval])

            return max_eval
        else:
            min_eval = (None, float('inf'))

            # print('pruntyje grę min')
            # print(game)
            if self.type == 1:
                opponent = 2
            else:
                opponent = 1
            for move in moves:
                # print(move, 'move')
                new_board = self.make_move(game, move[0], move[1])
                # print('new')
                # print(new_board)
                eval = self.minmax(new_board, depth - 1, True, evaluation)
                # print('eval')
                # print(eval[-1])
                # print(min_eval)
                if eval[-1] < min_eval[-1]:
                    min_eval = eval
                if eval[-1] == min_eval[-1]:
                    min_eval = random.choice([min_eval, eval])
                    best_move = move
                # min_eval = min(min_eval[0], eval[0])
            # print(best_move, 'best')
            # print(min_eval)
            return min_eval

    def minimax_alpha_beta(self, game, depth, is_maximizing, evaluation, alpha, beta):
        if depth == 0:
            return game[0], evaluation(game)
        if self.check_winner(game[1]):
            print('winn')
            return game[0], evaluation(game)

        if is_maximizing:
            moves = self.all_possible_moves(game, 1)
        else:
            moves = self.all_possible_moves(game, 2)

            # moves = self.all_possible_moves(game, self.type)
        best_move = None
        if is_maximizing:
            max_eval = (None, float('-inf'))
            for move in moves:
                # print(move, 'move')
                new_board = self.make_move(game, move[0], move[1])
                eval = self.minimax_alpha_beta(new_board, depth - 1, False, evaluation, alpha, beta)

                if eval[-1] > max_eval[-1]:
                    max_eval = eval
                if eval[-1] == max_eval[-1]:
                    max_eval = random.choice([max_eval, eval])
                alpha = max(alpha, max_eval[-1])
                if beta <= alpha:
                    # print('alpha')
                    break
            return max_eval
        else:
            min_eval = (None, float('inf'))
            for move in moves:
                new_board = self.make_move(game, move[0], move[1])
                eval = self.minimax_alpha_beta(new_board, depth - 1, True, evaluation, alpha, beta)
                if eval[-1] < min_eval[-1]:
                    min_eval = eval
                if eval[-1] == min_eval[-1]:
                    min_eval = random.choice([min_eval, eval])
                beta = min(beta, min_eval[-1])
                if beta <= alpha:
                    # print('beta')
                    break
            return min_eval

    def possile_moves(self, board, x, y, jump=0):
        # moves = set()
        list_of_boards = []

        # print(x, ' ', y)
        # print(type(board))
        # # if type(board) == int:
        # print(board)
        # board = board[1]

        if board[1][x][y] == 0 and jump == 0:
            return []
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_y = y + j
                new_x = x + i
                if 0 <= new_y < 16 and 0 <= new_x < 16:
                    if board[1][new_x][new_y] == 0 and jump == 0:
                        # print('dadaje 1 ', new_x, ' ', new_y)
                        if (board[1][x][y] == 1 and (x, y) in self.base2 and (new_x, new_y) not in self.base2) or (
                                board[1][x][y] == 2 and (x, y) in self.base1 and (new_x, new_y) not in self.base1):
                            pass
                        else:
                            self.moves.add((new_x, new_y))
                            list_of_boards.append(
                                ((x, y), (new_x, new_y)))
                    elif board[1][new_x][new_y] != 0 and jump == 0 and 0 <= new_x + i < 16 and 16 > new_y + j >= 0 == \
                            board[1][new_x + i][new_y + j] and (new_x + i, new_y + y) not in self.moves:
                        # print('dadaje 2 ', new_x + i, ' ', new_y + j)
                        if (board[1][x][y] == 1 and (x, y) in self.base2 and (new_x, new_y) not in self.base2) or (
                                board[1][x][y] == 2 and (x, y) in self.base1 and (new_x, new_y) not in self.base1):
                            pass
                        else:
                            self.moves.add((new_x + i, new_y + j))
                            list_of_boards.append(
                                ((x, y), (new_x + i, new_y + j)))
                        self.possile_moves(board, new_x + i, new_y + j, 1)
                    elif jump == 1 and board[1][new_x][new_y] != 0 and 0 <= new_x + i < 16 and 16 > new_y + j >= 0 == \
                            board[1][new_x + i][new_y + j] and (new_x + i, new_y + j) not in self.moves:
                        # print('skok ', new_x + i, ' ', new_y + j)
                        if (board[1][x][y] == 1 and (x, y) in self.base2 and (new_x, new_y) not in self.base2) or (
                                board[1][x][y] == 2 and (x, y) in self.base1 and (new_x, new_y) not in self.base1):
                            pass
                        else:
                            self.moves.add((new_x + i, new_y + j))
                            list_of_boards.append(
                                ((x, y), (new_x + i, new_y + j)))

                        self.possile_moves(board, new_x + i, new_y + j, 1)
                    else:
                        pass
        # print('dlu')
        # print(list_of_boards)
        return list_of_boards

    def all_possible_moves(self, board, player):
        i = 0
        j = 0
        self.moves = set()
        all_moves = []
        if board is not None:
            # print(board)
            for row in board[1]:
                for element in row:
                    if element == player:
                        # self.possile_moves(i, j)
                        # all_moves[(i, j)] = self.moves
                        for move in self.possile_moves(board, i, j):
                            if move[0] is not None:
                                all_moves.append(move)
                        # all_moves.append(self.possile_moves(board, i, j))
                        self.moves = set()
                    j += 1

                i += 1
                j = 0
            # print('elo')
            # print(all_moves)
            # print(all_moves)
            # print(player(all_moves[0]))
        return all_moves

    def make_move(self, board, old_pos, new_pos):
        new_board = copy.deepcopy(board)
        list_of_moves = new_board[0]
        x, y = old_pos
        x_new, y_new = new_pos
        # if board is None:
        #     # print('none')

        # print(x, ' ee ee ', y)
        temp = new_board[1][x][y]
        new_board[1][x][y] = new_board[1][x_new][y_new]
        new_board[1][x_new][y_new] = temp
        list_of_moves.append((old_pos, new_pos))
        new_board = (list_of_moves, new_board[1])
        # print(new_board)

        # for row in board:
        #     print(' '.join(str(cell) for cell in row))
        # print('elo')
        # for row in new_board:
        #     print(' '.join(str(cell) for cell in row))
        return new_board

    def check_winner(self, board):
        win2 = all(board[x][y] == 2 for x, y in self.base1)
        win1 = all(board[x][y] == 1 for x, y in self.base2)
        if win2:
            return True
        if win1:
            return True
        return False

    def test(self, state, evaluation):
        print(evaluation(state))
