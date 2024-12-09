from src.model.graph_manager import GraphManager

# Initialize the GraphManager
graph_manager = GraphManager()

def add_application(name: str, description: str = ""):
    node_id = f"application:{name}"
    graph_manager.add_node(node_id, "application", name, description)

def get_applications():
    return graph_manager.get_nodes_by_type("application")

def add_business_capability(name: str, description: str = ""):
    node_id = f"business_capability:{name}"
    graph_manager.add_node(node_id, "business_capability", name, description)

def get_business_capabilities():
    return graph_manager.get_nodes_by_type("business_capability")

def add_relationship(source_name: str, target_name: str, relation_type: str):
    source_id = find_node_id_by_name(source_name)
    target_id = find_node_id_by_name(target_name)
    if source_id and target_id:
        graph_manager.add_edge(source_id, target_id, relation_type)
    else:
        print(f"Cannot add relationship: '{source_name}' or '{target_name}' not found.")

def find_node_id_by_name(name: str):
    for node_id, data in graph_manager.graph.nodes(data=True):
        if data.get("name") == name:
            return node_id
    return None
