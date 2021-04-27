import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

def create_graph(df):
    G = nx.Graph()
    for i, row in df.iterrows():
        G.add_node(row['node'], pos=(row['x'], row['y']))
    return G

def plot_graph(G):
    nx.draw(G, nx.get_node_attributes(G, 'pos'), 
            with_labels=False,
            node_size=100,
            node_color='r')

def main():
    names = ['node', 'x', 'y']
    df = pd.read_csv('data/vm22775.tsp', names=names, delimiter=' ')

    for i in range(0, 1000, 100):
        sub_df = df.iloc[i:i + 100]
        G = create_graph(sub_df)
        plot_graph(G)
        plt.tight_layout()
        plt.savefig(f'plot/{i}.png', dpi=300)
        plt.clf()

if __name__ == '__main__':
    main()