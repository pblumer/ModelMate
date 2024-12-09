import networkx as nx
import json
import os

GRAPH_FILE = "model_graph.json"

class GraphManager:
    def __init__(self, graph_file=GRAPH_FILE):
        self.graph_file = graph_file
        self.graph = nx.MultiDiGraph()
        self.load_graph()

    def load_graph(self):
        if os.path.exists(self.graph_file):
            try:
                with open(self.graph_file, "r") as f:
                    data = json.load(f)
                    self.graph = nx.node_link_graph(data)
                print(f"Graph loaded from {self.graph_file}.")
            except Exception as e:
                print(f"Error loading graph from {self.graph_file}: {e}")
        else:
            print(f"No existing graph file found. Starting with an empty graph.")

    def save_graph(self):
        try:
            data = nx.node_link_data(self.graph)
            with open(self.graph_file, "w") as f:
                json.dump(data, f, indent=4)
            print(f"Graph saved to {self.graph_file}.")
        except Exception as e:
            print(f"Error saving graph to {self.graph_file}: {e}")

    def add_node(self, node_id, node_type, name, description=""):
        self.graph.add_node(node_id, type=node_type, name=name, description=description)
        self.save_graph()

    def get_nodes_by_type(self, node_type):
        return [data["name"] for node_id, data in self.graph.nodes(data=True) if data.get("type") == node_type]

    def add_edge(self, source_id, target_id, relation_type):
        self.graph.add_edge(source_id, target_id, type=relation_type)
        self.save_graph()
