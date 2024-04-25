# from halma import Halma

class Player:
    def __init__(self, type):
        self.type = type
    def evaluate(self, state):
        heuristic_value = 0
        if self.type == 1:
            point_x, point_y = 0, 0
        else:
            point_x , point_y = 0, 0
        x = 0
        y = 0
        for row in state:
            for element in row:
                if(int(element) == self.type):
                    print(x, ' ', y)
                    print(abs(point_x - x) + abs(point_y - y))
                    heuristic_value += (abs(point_x - x) + abs(point_y - y))
                y += 1
            x += 1
            y = 0
        print(heuristic_value)
        return  heuristic_value



    def minmax(self, game, depth, is_maximizing):
        if game.check_winner() == None:
            return self.evaluate(game)
        if depth == 0:
            return None
        if is_maximizing:
            max_eval = float('-inf')
            for child_state in game.all_possible_moves(self.type):
                eval = self.minmax(child_state, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            for child_state in game.all_possible_moves(self.type):
                min_eval = float('inf')
                eval = self.minmax(child_state, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval
