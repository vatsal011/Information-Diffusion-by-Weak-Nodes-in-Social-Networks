import networkx as nx

class Centrality():
    def __init__(self, graph):
        self.graph = graph
    
    def top_nodes(self, n, val):
        betweenness_centrality = nx.betweenness_centrality(self.graph)
        betweennes = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:n]

        closeness_centrality = nx.closeness_centrality(self.graph)
        closeness = sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)[:n]

        degree_centrality = nx.degree_centrality(self.graph)
        degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:n]

        eigenvector_centrality = nx.eigenvector_centrality(self.graph, max_iter=val)
        eigen = sorted(eigenvector_centrality.items(), key=lambda x: x[1], reverse=True)[:n]

        harmonic_centrality = nx.harmonic_centrality(self.graph)
        harmonic = sorted(harmonic_centrality.items(), key=lambda x: x[1], reverse=True)[:n]

        load_centrality = nx.load_centrality(self.graph)
        load = sorted(load_centrality.items(), key=lambda x: x[1], reverse=True)[:n]

        pagerank_centrality = nx.pagerank(self.graph)
        pagerank = sorted(pagerank_centrality.items(), key=lambda x: x[1], reverse=True)[:n]

        percolation_centrality = nx.percolation_centrality(self.graph)
        percolation = sorted(percolation_centrality.items(), key=lambda x: x[1], reverse=True)[:n]

        subgraph_centrality = nx.subgraph_centrality(self.graph)
        subgraph = sorted(subgraph_centrality.items(), key=lambda x: x[1], reverse=True)[:n]

        return betweennes, closeness, degree, eigen, harmonic, load, pagerank, percolation, subgraph

class Betweenness():
    def __init__(self, graph):
        self.graph = graph
        self.betweenness_centrality = nx.betweenness_centrality(self.graph)

    def top_betweenness_nodes(self, n):
        top_nodes = sorted(self.betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:n]
        return top_nodes
    
class Closeness():
    def __init__(self, graph):
        self.graph = graph
        self.closeness_centrality = nx.closeness_centrality(self.graph)

    def top_closeness_nodes(self, n):
        top_nodes = sorted(self.closeness_centrality.items(), key=lambda x: x[1], reverse=True)[:n]
        return top_nodes
    
class Degree():
    def __init__(self, graph):
        self.graph = graph
        self.degree_centrality = nx.degree_centrality(self.graph)

    def top_degree_nodes(self, n):
        top_nodes = sorted(self.degree_centrality.items(), key=lambda x: x[1], reverse=True)[:n]
        return top_nodes

class Eigen():
    def __init__(self, graph, val):
        self.graph = graph
        self.eigenvector_centrality = nx.eigenvector_centrality(self.graph, max_iter=val)

    def top_eigen_nodes(self, n):
        top_nodes = sorted(self.eigenvector_centrality.items(), key=lambda x: x[1], reverse=True)[:n]
        return top_nodes

class Harmonic():
    def __init__(self, graph):
        self.graph = graph
        self.harmonic_centrality = nx.harmonic_centrality(self.graph)

    def top_harmonic_nodes(self, n):
        top_nodes = sorted(self.harmonic_centrality.items(), key=lambda x: x[1], reverse=True)[:n]
        return top_nodes

class Load():
    def __init__(self, graph):
        self.graph = graph
        self.load_centrality = nx.load_centrality(self.graph)

    def top_load_nodes(self, n):
        top_nodes = sorted(self.load_centrality.items(), key=lambda x: x[1], reverse=True)[:n]
        return top_nodes

class Pagerank():
    def __init__(self, graph):
        self.graph = graph
        self.pagerank_centrality = nx.pagerank(self.graph)

    def top_pagerank_nodes(self, n):
        top_nodes = sorted(self.pagerank_centrality.items(), key=lambda x: x[1], reverse=True)[:n]
        return top_nodes

class Percolation():
    def __init__(self, graph):
        self.graph = graph
        self.percolation_centrality = nx.percolation_centrality(self.graph)

    def top_percolation_nodes(self, n):
        top_nodes = sorted(self.percolation_centrality.items(), key=lambda x: x[1], reverse=True)[:n]
        return top_nodes

class Subgraph():
    def __init__(self, graph):
        self.graph = graph
        self.subgraph_centrality = nx.subgraph_centrality(self.graph)

    def top_subgraph_nodes(self, n):
        top_nodes = sorted(self.subgraph_centrality.items(), key=lambda x: x[1], reverse=True)[:n]
        return top_nodes
