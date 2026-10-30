import networkx as nx
import numpy as np
from heapq import heappush, heappop
from operator import itemgetter
from informationdiffusion import *

class Greedy():
    def __init__(self, graph):
        self.graph = graph
    
    def greedy_nodes(self, text):
        S = []
        if text == "IC":
            spread = IndependentCascade(self.graph)
        elif text == "SIR":
            spread = SIR(self.graph)
        elif text == "GEMF":
            spread = GEMF(self.graph)
        for _ in range(10):
            best_node = None
            best_spread = 0
            for node in set(self.graph.nodes()) - set(S):
                current_spread = spread.nodes_reached(S + [node])
                if current_spread > best_spread:
                    best_spread = current_spread
                    best_node = node
            S.append(best_node)
        return S

class CELF():
    def __init__(self, graph):
        self.graph = graph
    
    def celf_nodes(self, text):
        S = []
        if text == "IC":
            spread = IndependentCascade(self.graph)
        elif text == "SIR":
            spread = SIR(self.graph)
        elif text == "GEMF":
            spread = GEMF(self.graph)
        nodes = list(self.graph.nodes())
        marg_gain = [(spread.nodes_reached([node]), node) for node in nodes]
        marg_gain.sort(reverse=True, key=itemgetter(0))
        S.append(marg_gain[0][1])
        marg_gain = marg_gain[1:]
        while len(S) < 10:
            best_node = marg_gain[0][1]
            best_spread = spread.nodes_reached(S + [best_node])
            
            for i in range(1, len(marg_gain)):
                node = marg_gain[i][1]
                current_spread = spread.nodes_reached(S + [node])
                if current_spread > best_spread:
                    best_spread = current_spread
                    best_node = node
                    marg_gain[0], marg_gain[i] = marg_gain[i], marg_gain[0]
            S.append(best_node)
            marg_gain = marg_gain[1:]
        return S
