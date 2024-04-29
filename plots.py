import matplotlib.pyplot as plt
import pandas as pd



def box_plot(file):
    data = pd.read_csv(file)

    # Utwórz boxplot
    plt.figure(figsize=(8, 6))
    plt.boxplot([data['time_minmax'], data['time_alpha']], labels=['Minimax Time (s)', 'Alpha-beta Time (s)'])
    plt.title('Comparison of Minimax and Alpha-beta pruning')
    plt.ylabel('Execution Time (s)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    box_plot('minmax_vs_alpha_3.csv')


