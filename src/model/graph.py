import networkx as nx

# In-memory graph instance
G = nx.MultiDiGraph()

def add_application(name: str):
    # Add a node representing an application
    # For simplicity, we use "application:<name>" as the node identifier
    node_id = f"application:{name}"
    G.add_node(node_id, type="application", name=name)

def get_applications():
    # Return all nodes of type application
    apps = []
    for node_id, data in G.nodes(data=True):
        if data.get("type") == "application":
            apps.append(data["name"])
    return apps
