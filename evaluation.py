def manhatan(point_x, point_y, x, y):
    return abs(point_x - x) + abs(point_y - y)


def random_empty_base(board, base, x, y, player_type):
    if player_type == 1:
        pos_x = 15
        pos_y = 15
    else:
        pos_y = 0
        pos_x = 0

    for field in base:
        x_1, x_2 = field
        if board[x_1][x_2] != 0:
            pos_x = x_1
            pos_y = x_2
            break
    # print(pos_x, pos_y)
    return manhatan(pos_x, pos_y, x, y)


def rival_base(base, x, y):
    if (x, y) in base:
        return 5
    return 0


def leave_base1(player_type, x, y, base):
    if (x, y) in base:
        if player_type == 1:
            d = (abs(-int(x) - int(y) + 6)) / (2 ** 0.5)
            return d * 10
        else:
            d = (abs(-int(x) - int(y) + 24)) / (2 ** 0.5)
            return d * 10
    return 0





def go_in_group1(player_type, board, x, y, base, bonus):
    value = 0
    if (x, y) in base:
        # print('tal')
        return 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            x_new = x + i
            y_new = y + j
            if 0 < x_new < 16 and 0 < y_new < 16:
                if board[1][x_new][y_new] == player_type and (x_new, y_new) not in base:
                    value += bonus
    return value
