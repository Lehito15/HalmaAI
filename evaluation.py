def manhatan(point_x, point_y, x, y):
    return abs(point_x - x) + abs(point_y - y)


def manhatan_2(point_x, point_y, x, y, board, base, player_type):
    if player_type == 1:
        empty_base = all(board[x][y] == 0 or board[x][y] == 2 for x, y in base)
    else:
        empty_base = all(board[x][y] == 0 or board[x][y] == 1 for x, y in base)
    if empty_base:
       # print('empty',player_type)
       return manhatan(point_x, point_y, x, y)
    else:
        if board[x][y] in base:
            return abs(point_x - x) + abs(point_y - y)
        else:
            return abs(point_x - x) + abs(point_y - y) *5

def if_in_base(player_type, base, board, x, y):
    if (x, y) in base:
        if player_type == 1:
            return -100
        else:
            return 100
    return 0
def leave_base(player_type, state, base):
    if state[0]:
        if state[0][0][0] in base:
            if state[0][0][1] not in base:
                if player_type == 1:
                    return 4
                else:
                    return -4
        return  0
    return 0

def rival_base(player_type, board, base, x, y):
    if (x, y) in base:
        if player_type == 1:
            return  5
        else:
            return -5
    return  0

def go_in_group(player_type, board, base, x, y):
    value = 0
    if (x,y) not in base:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if board[i][j] == player_type:
                    if player_type == 1:
                        value += 1
                    else:
                        value -= 1
                else:
                    if player_type == 1:
                        value -= 1
                    else:
                        value += 1
    # else:
    #     value = 4
    return value



