import networkx as nx
import random
import numpy as np

class MetropolisHastingsRandomWalk:
    def __init__(self, graph):
        self.graph = graph
        self.sampled_graph = nx.Graph()

    def _acceptance_probability(self, current_node, neighbor):
        return min(1, self.graph.degree(neighbor) / self.graph.degree(current_node))

    def get_mhrw_sample(self, num_nodes_in_sample):
        current_node = random.choice(list(self.graph.nodes()))
        self.sampled_graph.add_node(current_node)
        while self.sampled_graph.number_of_nodes() < num_nodes_in_sample:
            neighbor = random.choice(list(self.graph.neighbors(current_node)))
            acceptance_probability = self._acceptance_probability(current_node, neighbor)
            if random.random() < acceptance_probability:
                self.sampled_graph.add_node(neighbor)
                self.sampled_graph.add_edge(current_node, neighbor)
                current_node = neighbor
        return self.sampled_graph
    
class ForestFire:
    def __init__(self, graph):
        self.graph = graph

    def get_forestfire_sample(self, n):
        sampled_graph = nx.Graph()
        visited = set()
        frontier = set()
        start_node = random.choice(list(self.graph.nodes()))
        sampled_graph.add_node(start_node)
        visited.add(start_node)
        frontier.add(start_node)
        while len(sampled_graph) < n:
            current_node = frontier.pop()
            neighbors = list(self.graph.neighbors(current_node))
            for neighbor in neighbors:
                if neighbor not in visited:
                    sampled_graph.add_node(neighbor)
                    visited.add(neighbor)
                    frontier.add(neighbor)
                    sampled_graph.add_edge(current_node, neighbor)
            if not frontier:
                unvisited_nodes = list(set(self.graph.nodes()) - visited)
                if unvisited_nodes:
                    new_start_node = random.choice(unvisited_nodes)
                    sampled_graph.add_node(new_start_node)
                    visited.add(new_start_node)
                    frontier.add(new_start_node)
        return sampled_graph

class MultiDimensionalRandomWalk:
    def __init__(self, graph):
        self.graph = graph

    def get_mdrw_sample(self, n):
        sample_graph = nx.Graph()
        nodes = list(self.graph.nodes())
        start_node = np.random.choice(nodes)
        sample_graph.add_node(start_node)
        while len(sample_graph) < n:
            current_node = np.random.choice(list(sample_graph.nodes()))
            neighbors = list(self.graph.neighbors(current_node))
            if not neighbors:
                continue
            next_node = np.random.choice(neighbors)
            sample_graph.add_node(next_node)
            sample_graph.add_edge(current_node, next_node)
        return sample_graph

class Snowball:
    def __init__(self, graph):
        self.graph = graph

    def get_snowball_sample(self, n):
        seed_node = random.choice(list(self.graph.nodes))
        sample_graph = nx.Graph()
        sample_graph.add_node(seed_node)
        frontier = [seed_node]
        visited = set([seed_node])
        while len(sample_graph) < n:
            if len(frontier) == 0:
                break
            current_node = frontier.pop(0)
            neighbors = list(self.graph.neighbors(current_node))
            random.shuffle(neighbors)
            for neighbor in neighbors:
                if neighbor not in visited:
                    sample_graph.add_node(neighbor)
                    sample_graph.add_edge(current_node, neighbor)
                    visited.add(neighbor)
                    frontier.append(neighbor)
        return sample_graph
