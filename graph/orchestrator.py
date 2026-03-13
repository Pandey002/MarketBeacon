# Orchestrator
# This module wires all components together using a custom graph implementation.

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, name, func):
        self.nodes[name] = func
        self.edges[name] = []

    def add_edge(self, from_node, to_node):
        if from_node in self.edges:
            self.edges[from_node].append(to_node)
        else:
            raise ValueError(f"Node {from_node} does not exist in the graph.")

    def execute(self):
        executed = set()

        def execute_node(node):
            if node in executed:
                return
            for dependency in self.edges.get(node, []):
                execute_node(dependency)
            print(f"Executing: {node}")
            self.nodes[node]()
            executed.add(node)

        for node in self.nodes:
            execute_node(node)

def build_graph():
    graph = Graph()

    # Define nodes
    graph.add_node("Scrape Website", lambda: print("Scraping website..."))
    graph.add_node("Fetch News", lambda: print("Fetching news..."))
    graph.add_node("Extract Pricing Data", lambda: print("Extracting pricing data..."))
    graph.add_node("Extract Changelog Data", lambda: print("Extracting changelog data..."))
    graph.add_node("Scrape LinkedIn", lambda: print("Scraping LinkedIn..."))
    graph.add_node("Store Embeddings", lambda: print("Storing embeddings..."))
    graph.add_node("Query Embeddings", lambda: print("Querying embeddings..."))
    graph.add_node("Analyze with Gemini", lambda: print("Analyzing with Gemini..."))

    # Define edges
    graph.add_edge("Scrape Website", "Store Embeddings")
    graph.add_edge("Fetch News", "Store Embeddings")
    graph.add_edge("Extract Pricing Data", "Store Embeddings")
    graph.add_edge("Extract Changelog Data", "Store Embeddings")
    graph.add_edge("Scrape LinkedIn", "Store Embeddings")
    graph.add_edge("Store Embeddings", "Query Embeddings")
    graph.add_edge("Query Embeddings", "Analyze with Gemini")

    return graph

if __name__ == "__main__":
    graph = build_graph()
    print("Custom orchestrator graph built successfully.")
    graph.execute()
