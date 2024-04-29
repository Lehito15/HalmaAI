from halma import Halma
from time import perf_counter

def minmax_vs_alpha_beta(file_name, depth):
    halma = Halma()

    with open(file_name, 'w') as file:
        file.write("Iteration,time_minmax,time_alpha,depth\n")
        for i in range(10):
            halma.generate_random_board()
            start_time = perf_counter()
            a = halma.player1.minmax(([], halma.board), depth, True, halma.player1.evaluate)
            end_time = perf_counter()
            execution_time_minmax = end_time - start_time
            halma.generate_random_board()
            start_time = perf_counter()
            alpha = halma.player1.minimax_alpha_beta(([], halma.board), depth, True, halma.player1.evaluate, float('-inf'), float('inf'))
            end_time = perf_counter()
            execution_time_alpha_beta = end_time - start_time
            file.write(f"{i+1},{execution_time_minmax},{execution_time_alpha_beta},{depth}\n")
def number_of_nodes(depth):
    minmax_nodes = []
    alpha_nodes = []
    halma = Halma()
    for i in range(10):
        halma.generate_random_board()
        a = halma.player1.minmax(([], halma.board), depth, True, halma.player1.evaluate)
        minmax_nodes.append(halma.player1.nodes)
        halma.player1.nodes = 0
        alpha = halma.player1.minimax_alpha_beta(([], halma.board), depth, True, halma.player1.evaluate, float('-inf'),
                                                 float('inf'))
        alpha_nodes.append(halma.player1.nodes)
        halma.player1.nodes = 0
    # print(minmax_nodes)
    # print(alpha_nodes)
    print(sum(minmax_nodes) / len(minmax_nodes))
    print(sum(alpha_nodes) / len(alpha_nodes))

def analysis_heurystic(file_name):
    halma = Halma()
    with open(file_name, 'w') as file:
        file.write("Iteration,winner,depth\n")
        for i in range(10):
            # halma.read_board_from_file('halmaWinner.txt')
            halma.generate_random_board()
            halma.print_board()
            winner = halma.game_alpha_beta(2, halma.player1.startegy_all, halma.player1.strategy_go_in_group)
            print(i+1)
            file.write(f"{i + 1},{winner}\n")







if __name__ == "__main__":
    # minmax_vs_alpha_beta('minmax_vs_alpha_3.csv', 3)
    # number_of_nodes(2)
    analysis_heurystic('eall_vs_egroup_2v2_random.csv')