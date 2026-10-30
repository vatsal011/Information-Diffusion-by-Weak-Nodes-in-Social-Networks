import time
from weaknodes import *
from centrality import *

class CentralityNodes():
    def __init__(self, main_graph):
        self.main_graph = main_graph

    def get_centrality_nodes(self):
        val = 10000

        twn = []
        tbn = []
        tcn = []
        tdn = []
        ten = []
        thn = []
        tlon = []
        tpagen = []
        tpern = []
        tsn = []

        start_time = time.time()
        print("Weak: ", end=" ")
        wn_obj = WeakNodes(self.main_graph)
        end_time = time.time()
        print(end_time - start_time)
        for i in [5,10,15]:
            twn.append(wn_obj.top_weak_nodes(i))
        print("twn = ", twn)

        start_time = time.time()
        print("Betweenness: ", end=" ")
        bn_obj = Betweenness(self.main_graph)
        end_time = time.time()
        print(end_time - start_time)
        for i in [5,10,15]:
            tbn.append([t[0] for t in bn_obj.top_betweenness_nodes(i)])
        print("tbn = ", tbn)

        start_time = time.time()
        print("Closeness: ", end=" ")
        cn_obj = Closeness(self.main_graph)
        end_time = time.time()
        print(end_time - start_time)
        for i in [5,10,15]:
            tcn.append([t[0] for t in cn_obj.top_closeness_nodes(i)])
        print("tcn = ", tcn)

        start_time = time.time()
        print("Degree: ", end=" ")
        dn_obj = Degree(self.main_graph)
        end_time = time.time()
        print(end_time - start_time)
        for i in [5,10,15]:
            tdn.append([t[0] for t in dn_obj.top_degree_nodes(i)])
        print("tdn = ", tdn)

        start_time = time.time()
        print("Eigen: ", end=" ")
        en_obj = Eigen(self.main_graph, val)
        end_time = time.time()
        print(end_time - start_time)
        for i in [5,10,15]:
            ten.append([t[0] for t in en_obj.top_eigen_nodes(i)])
        print("ten = ", ten)

        start_time = time.time()
        print("Harmonic: ", end=" ")
        hn_obj = Harmonic(self.main_graph)
        end_time = time.time()
        print(end_time - start_time)
        for i in [5,10,15]:
            thn.append([t[0] for t in hn_obj.top_harmonic_nodes(i)])
        print("thn = ", thn)

        start_time = time.time()
        print("Load: ", end=" ")
        lon_obj = Load(self.main_graph)
        end_time = time.time()
        print(end_time - start_time)
        for i in [5,10,15]:           
            tlon.append([t[0] for t in lon_obj.top_load_nodes(i)])
        print("tlon = ", tlon)

        start_time = time.time()
        print("Page: ", end=" ")
        pagen_obj = Pagerank(self.main_graph)
        end_time = time.time()
        print(end_time - start_time)
        for i in [5,10,15]:           
            tpagen.append([t[0] for t in pagen_obj.top_pagerank_nodes(i)])
        print("tpagen = ", tpagen)

        start_time = time.time()
        print("Percolation: ", end=" ")
        pern_obj = Percolation(self.main_graph)
        end_time = time.time()
        print(end_time - start_time)
        for i in [5,10,15]:           
            tpern.append([t[0] for t in pern_obj.top_percolation_nodes(i)])
        print("tpern = ", tpern)

        start_time = time.time()
        print("Subgraph: ", end=" ")
        sn_obj = Subgraph(self.main_graph)
        end_time = time.time()
        print(end_time - start_time)
        for i in [5,10,15]:           
            tsn.append([t[0] for t in sn_obj.top_subgraph_nodes(i)])
        print("tsn = ", tsn)

        return twn, tbn, tcn, tdn, ten, thn, tlon, tpagen, tpern, tsn
