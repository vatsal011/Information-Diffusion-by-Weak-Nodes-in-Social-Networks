import networkx as nx
import random
from collections import deque

class Geodesic():
    def __init__(self, graph):
        self.G = graph
    
    def nodes_reached(self, nodes, num):
        unique_nodes = set()
        for n in nodes:
            neighbors = nx.single_source_shortest_path_length(self.G, n, cutoff=num)
            unique_nodes.update(neighbors.keys())
        return len(unique_nodes)

class SIR():
    def __init__(self, graph):
        self.graph = graph

    def nodes_reached(self, seeds):
        infection_rate = 0.3
        recovery_rate = 0.1
        infected = set(seeds)
        recovered = set()
        while True:
            current_infected = infected.copy()
            for node in current_infected:
                neighbors = set(self.graph.neighbors(node))
                for neighbor in neighbors:
                    if neighbor not in infected and neighbor not in recovered:
                        if random.random() < infection_rate:
                            infected.add(neighbor)
            newly_recovered = set()
            for node in infected:
                if random.random() < recovery_rate:
                    newly_recovered.add(node)
            recovered |= newly_recovered
            infected -= newly_recovered
            if len(infected) == 0:
                break
        return len(infected) + len(recovered)

class IndependentCascade():
    def __init__(self, graph):
        self.graph = graph

    def nodes_reached(self, seeds):
        activated = set(seeds)
        new_activated = set(seeds)
        while new_activated:
            current_activated = new_activated.copy()
            new_activated.clear()
            for node in current_activated:
                neighbors = set(self.graph.neighbors(node)) - activated
                for neighbor in neighbors:
                    if random.random() <= 0.5: 
                        new_activated.add(neighbor)
            activated |= new_activated
        return len(activated)

class GEMF():
    def __init__(self, graph):
        self.graph = graph
    
    def nodes_reached(self, seeds):
        infection_rate = 0.3
        recovery_rate = 0.1
        states = {node: 0 for node in self.graph.nodes()}
        for seed in seeds:
            states[seed] = 1
        infected = set(seeds)
        recovered = set()
        while infected:
            new_infected = set()
            new_recovered = set()
            for node in infected:
                for neighbor in self.graph.neighbors(node):
                    if states[neighbor] == 0 and random.random() < infection_rate:
                        new_infected.add(neighbor)
                        states[neighbor] = 1
                if random.random() < recovery_rate:
                    new_recovered.add(node)
                    states[node] = 2
            infected = (infected | new_infected) - new_recovered
            recovered |= new_recovered
        return len([node for node, state in states.items() if state != 0])
