"""
===========================================================
QuantumSecureNet
Network Visualization Module

Creates a conceptual Quantum Key Distribution network
using NetworkX.

Author:
===========================================================
"""

import networkx as nx
import matplotlib.pyplot as plt


class QuantumNetwork:

    def __init__(self):

        self.graph = nx.Graph()

    def build_network(self):

        self.graph.clear()

        self.graph.add_node(
            "Alice",
            node_type="sender"
        )

        self.graph.add_node(
            "Relay-1",
            node_type="relay"
        )

        self.graph.add_node(
            "Relay-2",
            node_type="relay"
        )

        self.graph.add_node(
            "Bob",
            node_type="receiver"
        )

        self.graph.add_node(
            "Eve",
            node_type="attacker"
        )

        self.graph.add_edge("Alice", "Relay-1")
        self.graph.add_edge("Relay-1", "Relay-2")
        self.graph.add_edge("Relay-2", "Bob")

        return self.graph

    def draw_network(self):

        self.build_network()

        pos = {
            "Alice": (0, 0),
            "Relay-1": (1.5, 0),
            "Relay-2": (3, 0),
            "Bob": (4.5, 0),
            "Eve": (2.2, 1.2)
        }

        node_colors = []

        for node in self.graph.nodes():

            node_type = self.graph.nodes[node]["node_type"]

            if node_type == "sender":
                node_colors.append("green")

            elif node_type == "receiver":
                node_colors.append("blue")

            elif node_type == "relay":
                node_colors.append("orange")

            elif node_type == "attacker":
                node_colors.append("red")

            else:
                node_colors.append("gray")

        plt.figure(figsize=(9,4))

        nx.draw_networkx_nodes(
            self.graph,
            pos,
            node_color=node_colors,
            node_size=1700
        )

        nx.draw_networkx_labels(
            self.graph,
            pos,
            font_size=11,
            font_weight="bold"
        )

        nx.draw_networkx_edges(
            self.graph,
            pos,
            width=2
        )

        plt.title(
            "Conceptual Multi-Node Quantum Key Distribution Network",
            fontsize=13,
            fontweight="bold"
        )

        plt.axis("off")

        return plt.gcf()