import matplotlib.pyplot as plt
import networkx as nx


from pprint import pprint


class Graph:

    def __init__(self, MATRIX: list[list]):

        if self.validateInput(MATRIX):
            self.createGraph(MATRIX)
            self.cycle_basis()
            self.printGraph()
        else:
            print('Error - validatin failed')

    def createGraph(self, MATRIX):
        self.Graph = nx.Graph()
        players = len(MATRIX)
        id = 0
        str = ""
        items = len(MATRIX[0])
        for key in range(0, items):
            itemName = "item{item} ".format(item=id)
            self.Graph.add_node(id, name=itemName, type='item', color="red")
            id += 1

        for key in range(0, players):
            playerName = "player{player} ".format(player=id)
            str += "{playerName}: {values}\n".format(playerName=playerName,
                                                     values=MATRIX[key])
            self.Graph.add_node(id, name=playerName,
                                data=MATRIX[key], type='player', color="blue")
            item = 0
            for value in MATRIX[key]:
                if (value > 0):
                    self.Graph.add_edge(id, item, weight=value)
                    self.Graph.add_edge(item, id, weight=value)
                item += 1
            item = 0
            id += 1
        print(str)

    def printGraph(self) -> None:
        pos = nx.spring_layout(self.Graph, seed=7)

        listPlayers = [u for (u, v) in self.Graph.nodes(
            data=True) if v["type"] == 'player']
        listItems = [u for (u, v) in self.Graph.nodes(
            data=True) if v["type"] == 'item']

        nx.draw_networkx_nodes(
            self.Graph, pos, nodelist=listPlayers,  node_size=1000, node_color='y')
        nx.draw_networkx_nodes(
            self.Graph, pos, nodelist=listItems,  node_size=500, node_color='g')

        nx.draw_networkx_edges(self.Graph, pos, width=6)

        nx.draw_networkx_labels(
            self.Graph, pos, font_size=20, font_family="sans-serif")
        edge_labels = nx.get_edge_attributes(self.Graph, "weight")
        nx.draw_networkx_edge_labels(self.Graph, pos, edge_labels)

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def validateInput(self, List):
        n = List
        for i in n:
            if len(i) != len(n[0]):
                return False
        return True

    def cycle_basis(self):

        pathNum = 1
        for node in self.Graph.nodes():
            if (self.Graph.nodes[node]["type"] == "player"):

                paths = nx.cycle_basis(self.Graph, node)
                if (len(paths) == 0):
                    print('No path on the graph')
                for path in paths:
                    print('path', path)
                    str = "{node} -> ".format(
                        node=self.Graph.nodes[node]["name"])
                    weight = 0
                    run = 0
                    for n in path:
                        if (run == 0):
                            str += "{n}".format(
                                n=self.Graph.nodes[n]["name"])
                        else:
                            str += " -> {n}".format(
                                n=self.Graph.nodes[n]["name"])

                        if (self.Graph.nodes[n]["type"] == "player"):
                            if (run > 0):
                                weight = self.Graph.get_edge_data(
                                    path[run-1], n)["weight"]

                        run += 1
                    run = 0
                    print("pathNum: {pathNum} ,  weight: {weight}, path: {str}".format(
                        pathNum=pathNum, weight=weight, str=str))
                    str = ""
                    pathNum += 1
                pathNum += 1


MATRIX = [
    [0, 0, 0.9, 0.3, 1, 0.5],
    [1, 0.5, 0, 0.3, 0, 0.5],
    [0, 0.3, 0.1, 0.4, 0, 0],
]


if __name__ == "__main__":
    graph = Graph(MATRIX)