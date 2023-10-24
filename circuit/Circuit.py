import pandas as pd


class Circuit:

    def __init__(self):
        self.n_components = 0
        self.adj_matrix = pd.DataFrame([])

    def add_component(self, component_id):
        self.n_components += 1
        self.adj_matrix[component_id] = 0
        self.adj_matrix.loc[component_id] = 0

    def remove_component(self, component_id):
        self.n_components -= 1
        del self.adj_matrix[component_id]
        self.adj_matrix.drop(component_id)

    def add_edge(self, c1, c2, *args):
        self.adj_matrix[c1][c2] = 1

        for e in range(len(args)-1):
            self.adj_matrix[c1][args[e]] = 1

    def remove_edge(self, c1, c2, *args):
        self.adj_matrix[c1][c2] = 0

        for e in range(len(args)-1):
            self.adj_matrix[c1][args[e]] = 0

    def adjacent(self, c1, c2):
        return bool(self.adj_matrix[c1][c2])
