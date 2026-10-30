import networkx as nx

class WeakNodes():
    def __init__(self, graph):
        self.graph = graph
        self.m_communities = self.modular_communities()
        self.m_weak_nodes = self.weak_nodes(self.m_communities)
        self.l_communities = self.louvain_communities()
        self.l_weak_nodes = self.weak_nodes(self.l_communities)

    def modular_communities(self):
        communities = nx.community.greedy_modularity_communities(self.graph)
        return list(communities)

    def louvain_communities(self):
        communities = nx.community.louvain_communities(self.graph)
        return list(communities)

    def weak_nodes(self, communities):
        weak_nodes = set()
        for community in communities:
            for node in community:
                neighbors = set(self.graph.neighbors(node))
                for other_community in communities:
                    if other_community != community:
                        intersection = neighbors.intersection(other_community)
                        if intersection:
                            weak_nodes.add(node)
        return list(weak_nodes)

    def top_weak_nodes(self, n):
        top_weak_nodes = set()
        m_sorted_weak_nodes = sorted(self.m_weak_nodes, key=lambda x: self.graph.degree(x), reverse=True)
        top_weak_nodes.update(m_sorted_weak_nodes[:n])
        l_sorted_weak_nodes = sorted(self.l_weak_nodes, key=lambda x: self.graph.degree(x), reverse=True)
        top_weak_nodes.update(l_sorted_weak_nodes[:n])
        return list(top_weak_nodes)[:n]
