# from halma import Halma
import copy
import random
import evaluation


class Player:
    def __init__(self):
        # self.type = type
        self.nodes = 0
        self.moves = set()

        self.base1 = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1),
                      (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1)}
        self.base2 = {(15, 15), (15, 14), (15, 13), (15, 12), (15, 11), (14, 15), (14, 14), (14, 13), (14, 12),
                      (14, 11),
                      (13, 15), (13, 14), (13, 13), (13, 12), (12, 15), (12, 14), (12, 13), (11, 15), (11, 14)}

    def strategy_offensive(self, state):
        heuristic_value_1 = 0
        heuristic_value_2 = 0

        point_x_2, point_y_2 = 15, 15
        point_x_1, point_y_1 = 0, 0

        x = 0
        y = 0
        for row in state[1]:
            for element in row:
                if element == 1:
                    heuristic_value_1 += evaluation.manhatan(point_x_1, point_y_1, x, y)

                elif element == 2:
                    heuristic_value_2 += evaluation.manhatan(point_x_2, point_y_2, x, y)
                y += 1
            x += 1
            y = 0
        return heuristic_value_1 - heuristic_value_2

    def evaluation_random(self, state):
        heuristic_value_1 = 0
        heuristic_value_2 = 0
        x = 0
        y = 0

        point_x_2, point_y_2 = 15, 15
        point_x_1, point_y_1 = 0, 0

        for row in state[1]:
            for element in row:
                if element == 1:
                    heuristic_value_1 += evaluation.random_empty_base(state[1], self.base2, x, y, 1)
                    heuristic_value_1 += evaluation.leave_base1(1, x, y, self.base1)


                elif element == 2:
                    heuristic_value_2 += evaluation.random_empty_base(state[1], self.base1, x, y, 2)
                    heuristic_value_2 += evaluation.leave_base1(2, x, y, self.base2)

                y += 1
            x += 1
            y = 0
        return heuristic_value_2 - heuristic_value_1

    def strategy_ofensivev2(self, state):
        heuristic_value_1 = 0
        heuristic_value_2 = 0
        x = 0
        y = 0

        point_x_2, point_y_2 = 15, 15
        point_x_1, point_y_1 = 0, 0

        for row in state[1]:
            for element in row:
                if element == 1:
                    heuristic_value_1 += evaluation.manhatan(point_x_1, point_y_1, x, y)
                    # heuristic_value_1 += evaluation.rival_base(self.base2, x, y)
                    heuristic_value_1 -= evaluation.leave_base1(1, x, y, self.base1)

                elif element == 2:
                    heuristic_value_2 += evaluation.manhatan(point_x_2, point_y_2, x, y)
                    # heuristic_value_2 += evaluation.rival_base(self.base1, x, y)
                    heuristic_value_2 -= evaluation.leave_base1(2, x, y, self.base2)
                y += 1
            x += 1
            y = 0
            # print(heuristic_value_2)
            # print(heuristic_value_1 - heuristic_value_2)
        return heuristic_value_1 - heuristic_value_2

    def strategy_go_in_group(self, state):
        heuristic_value_1 = 0
        heuristic_value_2 = 0

        point_x_2, point_y_2 = 15, 15
        point_x_1, point_y_1 = 0, 0
        x = 0
        y = 0
        for row in state[1]:
            for element in row:
                if element == 1:
                    heuristic_value_1 += evaluation.go_in_group1(1, state, x, y, self.base1, 0.5)
                    heuristic_value_1 += evaluation.manhatan(point_x_1, point_y_1, x, y)
                    # heuristic_value_1 += evaluation.rival_base(self.base2, x, y)
                    heuristic_value_1 -= evaluation.leave_base1(1, x, y, self.base1)
                elif element == 2:
                    heuristic_value_2 += evaluation.go_in_group1(2, state, x, y, self.base2, 0.5)
                    heuristic_value_2 += evaluation.manhatan(point_x_2, point_y_2, x, y)
                    # heuristic_value_2 += evaluation.rival_base(self.base1, x, y)
                    heuristic_value_2 -= evaluation.leave_base1(2, x, y, self.base2)

                y += 1
            x += 1
            y = 0
        # print(heuristic_value, ' heyrestyka')
        # print(state[0])
        # print(heuristic_value_1)
        # print(heuristic_value_2)
        return heuristic_value_1 - heuristic_value_2

    def startegy_all(self, state):
        heuristic_value_1 = 0
        heuristic_value_2 = 0

        point_x_2, point_y_2 = 15, 15
        point_x_1, point_y_1 = 0, 0
        x = 0
        y = 0
        for row in state[1]:
            for element in row:
                if element == 1:
                    heuristic_value_1 -= evaluation.go_in_group1(1, state, x, y, self.base1, 0.5)
                    # heuristic_value_1 += evaluation.manhatan(point_x_1, point_y_1, x, y)
                    heuristic_value_1  += evaluation.random_empty_base(state[1],  self.base2, x, y,1)
                    heuristic_value_1 -= evaluation.rival_base(self.base2, x, y)
                    heuristic_value_1 += evaluation.leave_base1(1, x, y, self.base1)
                elif element == 2:
                    heuristic_value_2 -= evaluation.go_in_group1(2, state, x, y, self.base2, 0.5)
                    # heuristic_value_2 += evaluation.manhatan(point_x_2, point_y_2, x, y)
                    heuristic_value_2 += evaluation.random_empty_base(state[1], self.base1, x, y, 2)
                    heuristic_value_2 -= evaluation.rival_base(self.base1, x, y)
                    heuristic_value_2 += evaluation.leave_base1(2, x, y, self.base2)

                y += 1
            x += 1
            y = 0
        return heuristic_value_2 - heuristic_value_1

    def minmax(self, game, depth, is_maximizing, evaluation):
        self.nodes += 1
        if depth == 0:
            return game[0], evaluation(game)
        if self.check_winner(game[1]):
            return game[0], evaluation(game)

        if is_maximizing:
            moves = self.all_possible_moves(game, 1)
        else:
            moves = self.all_possible_moves(game, 2)

        if is_maximizing:
            max_eval = (None, float('-inf'))
            for move in moves:
                new_board = self.make_move(game, move[0], move[1])
                eval = self.minmax(new_board, depth - 1, False, evaluation)

                if eval[-1] > max_eval[-1]:
                    max_eval = eval
                if eval[-1] == max_eval[-1]:
                    max_eval = random.choice([max_eval, eval])

            return max_eval
        else:
            min_eval = (None, float('inf'))
            for move in moves:
                new_board = self.make_move(game, move[0], move[1])
                eval = self.minmax(new_board, depth - 1, True, evaluation)
                if eval[-1] < min_eval[-1]:
                    min_eval = eval
                if eval[-1] == min_eval[-1]:
                    min_eval = random.choice([min_eval, eval])
            return min_eval

    def minimax_alpha_beta(self, game, depth, is_maximizing, evaluation, alpha, beta):
        self.nodes += 1
        if depth == 0:
            return game[0], evaluation(game)
        if self.check_winner(game[1]):
            print('winn')
            return game[0], evaluation(game)

        if is_maximizing:
            moves = self.all_possible_moves(game, 1)
        else:
            moves = self.all_possible_moves(game, 2)
        if len(moves) > 100:
            if depth > 2:
                depth -= 1
                print(depth)

        if is_maximizing:
            max_eval = (None, float('-inf'))
            for move in moves:
                new_board = self.make_move(game, move[0], move[1])
                eval = self.minimax_alpha_beta(new_board, depth - 1, False, evaluation, alpha, beta)

                if eval[-1] > max_eval[-1]:
                    max_eval = eval
                if eval[-1] == max_eval[-1]:
                    max_eval = random.choice([max_eval, eval])
                alpha = max(alpha, max_eval[-1])
                if beta <= alpha:
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
                    break
            return min_eval

    def possile_moves(self, board, x, y, jump=0):
        list_of_boards = []

        if board[1][x][y] == 0 and jump == 0:
            return []
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_y = y + j
                new_x = x + i
                if 0 <= new_y < 16 and 0 <= new_x < 16:
                    if board[1][new_x][new_y] == 0 and jump == 0:
                        if (board[1][x][y] == 1 and (x, y) in self.base2 and (new_x, new_y) not in self.base2) or (
                                board[1][x][y] == 2 and (x, y) in self.base1 and (new_x, new_y) not in self.base1):
                            pass
                        else:
                            self.moves.add((new_x, new_y))
                            list_of_boards.append(
                                ((x, y), (new_x, new_y)))
                    elif board[1][new_x][new_y] != 0 and jump == 0 and 0 <= new_x + i < 16 and 16 > new_y + j >= 0 == \
                            board[1][new_x + i][new_y + j] and (new_x + i, new_y + y) not in self.moves:
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
                        for move in self.possile_moves(board, i, j):
                            if move[0] is not None:
                                all_moves.append(move)
                        self.moves = set()
                    j += 1

                i += 1
                j = 0
        return all_moves

    def make_move(self, board, old_pos, new_pos):
        new_board = copy.deepcopy(board)
        list_of_moves = new_board[0]
        x, y = old_pos
        x_new, y_new = new_pos

        temp = new_board[1][x][y]
        new_board[1][x][y] = new_board[1][x_new][y_new]
        new_board[1][x_new][y_new] = temp
        list_of_moves.append((old_pos, new_pos))
        new_board = (list_of_moves, new_board[1])
        return new_board

    def check_winner(self, board):
        win2 = all(board[x][y] == 2 for x, y in self.base1)
        win1 = all(board[x][y] == 1 for x, y in self.base2)
        if win2:
            return True
        if win1:
            return True
        return False

    def count_pawns_in_base(self, board, base, player_type):
        count = 0
        for position in base:
            x, y = position
            if board[x][y] == player_type:
                count += 1
        return count

