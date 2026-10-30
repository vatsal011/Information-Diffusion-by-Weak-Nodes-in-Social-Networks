import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import pi
from informationdiffusion import Geodesic
from matplotlib.ticker import FuncFormatter

class BarGraph10():
    def __init__(self, main_graph):
        self.main_graph = main_graph

    def plot_bar_graph(self, twn, tbn, tcn, tdn, ten, thn, tlon, tpagen, tpern, tsn):
        main_id = Geodesic(self.main_graph)
        wn = []
        bn = []
        cn = []
        dn = []
        en = []
        hn = []
        lon = []
        pagen = []
        pern = []
        sn = []

        value = self.main_graph.number_of_nodes()

        for inf in [1,2,3]:
            wn.append((main_id.nodes_reached(twn[1], inf)*100)/value)
            bn.append((main_id.nodes_reached(tbn[1], inf)*100)/value)
            cn.append((main_id.nodes_reached(tcn[1], inf)*100)/value)
            dn.append((main_id.nodes_reached(tdn[1], inf)*100)/value)
            en.append((main_id.nodes_reached(ten[1], inf)*100)/value)
            hn.append((main_id.nodes_reached(thn[1], inf)*100)/value)
            lon.append((main_id.nodes_reached(tlon[1], inf)*100)/value)
            pagen.append((main_id.nodes_reached(tpagen[1], inf)*100)/value)
            pern.append((main_id.nodes_reached(tpern[1], inf)*100)/value)
            sn.append((main_id.nodes_reached(tsn[1], inf)*100)/value)

        values = [wn, bn, cn, dn, en, hn, lon, pagen, pern, sn]
        plt.figure(figsize=(12,6))
        categories = ['1', '2', '3']
        barWidth = 0.08

        r1 = np.arange(len(values[0]))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]
        r4 = [x + barWidth for x in r3]
        r5 = [x + barWidth for x in r4]
        r6 = [x + barWidth for x in r5]
        r7 = [x + barWidth for x in r6]
        r8 = [x + barWidth for x in r7]
        r9 = [x + barWidth for x in r8]
        r10 = [x + barWidth for x in r9]

        plt.bar(r1, values[0], color='#FF6B6B', width=barWidth, edgecolor='black', label='Weak Nodes Approach', zorder=2)
        plt.bar(r2, values[1], color='#8B4513', width=barWidth, edgecolor='black', label='Betweenness Centrality', zorder=2)
        plt.bar(r3, values[2], color='#FFA500', width=barWidth, edgecolor='black', label='Closeness Centrality', zorder=2)
        plt.bar(r4, values[3], color='#00CED1', width=barWidth, edgecolor='black', label='Degree Centrality', zorder=2)
        plt.bar(r5, values[4], color='#9370DB', width=barWidth, edgecolor='black', label='Eigenvector Centrality', zorder=2)
        plt.bar(r6, values[5], color='#FF69B4', width=barWidth, edgecolor='black', label='Harmonic Centrality', zorder=2)
        plt.bar(r7, values[6], color='#4169E1', width=barWidth, edgecolor='black', label='Load Centrality', zorder=2)
        plt.bar(r8, values[7], color='#FFD700', width=barWidth, edgecolor='black', label='Pagerank Centrality', zorder=2)
        plt.bar(r9, values[8], color='#7B68EE', width=barWidth, edgecolor='black', label='Percolation Centrality', zorder=2)
        plt.bar(r10, values[9], color='#00FA9A', width=barWidth, edgecolor='black', label='Subgraph Centrality', zorder=2)

        def to_percent(y, position):
            return f'{y:.0f}%'
        
        plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
        plt.grid(True, linewidth=0.5, zorder=1)
        plt.xlabel('Geodesic Distance', fontsize=14)
        plt.ylabel('Percent Nodes Reached', fontsize=14)
        plt.xticks([r + 4*barWidth for r in range(len(values[0]))], categories)
        plt.legend()
        plt.show()


class SpiderChart10():
    def __init__(self, main_graph):
        self.main_graph = main_graph
    
    def plot_spider_chart(self, twn, tbn, tcn, tdn, ten, thn, tlon, tpagen, tpern, tsn):
        main_id = Geodesic(self.main_graph)
        wn = []
        bn = []
        cn = []
        dn = []
        en = []
        hn = []
        lon = []
        pagen = []
        pern = []
        sn = []

        value = self.main_graph.number_of_nodes()

        for inf in [1,2,3]:
            wn.append(main_id.nodes_reached(twn[1], inf)/value)
            bn.append(main_id.nodes_reached(tbn[1], inf)/value)
            cn.append(main_id.nodes_reached(tcn[1], inf)/value)
            dn.append(main_id.nodes_reached(tdn[1], inf)/value)
            en.append(main_id.nodes_reached(ten[1], inf)/value)
            hn.append(main_id.nodes_reached(thn[1], inf)/value)
            lon.append(main_id.nodes_reached(tlon[1], inf)/value)
            pagen.append(main_id.nodes_reached(tpagen[1], inf)/value)
            pern.append(main_id.nodes_reached(tpern[1], inf)/value)
            sn.append(main_id.nodes_reached(tsn[1], inf)/value)

        g1 = [wn[0], bn[0], cn[0], dn[0], en[0], hn[0], lon[0], pagen[0], pern[0], sn[0]]
        g2 = [wn[1], bn[1], cn[1], dn[1], en[1], hn[1], lon[1], pagen[1], pern[1], sn[1]]
        g3 = [wn[2], bn[2], cn[2], dn[2], en[2], hn[2], lon[2], pagen[2], pern[2], sn[2]]

        index_names = ["Weak Nodes", "Betweenness Nodes", "Closeness Nodes",
                      "Degree Nodes", "Eigenvector Nodes", "Harmonic Nodes",
                      "Load Nodes", "Pagerank Nodes", "Percolation Nodes",
                      "Subgraph Nodes"]
        
        data = {
            'Geodesic 1': g1,
            'Geodesic 2': g2,
            'Geodesic 3': g3
        }

        df = pd.DataFrame(data, index=index_names)
        num_vars = len(df.index)
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        angles += angles[:1]
        _, ax = plt.subplots(figsize=(12, 6), subplot_kw=dict(polar=True))
        for column in df.columns:
            values = df[column].tolist()
            values += values[:1] 
            ax.plot(angles, values, label=column)
            ax.fill(angles, values, alpha=0.25)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(index_names)
        for label, angle in zip(ax.get_xticklabels(), angles):
            if angle == 0:
                label.set_horizontalalignment('left')
                label.set_verticalalignment('center')
            elif angle < pi/2:
                label.set_horizontalalignment('left')
                label.set_verticalalignment('bottom')
            elif (angle < pi) and (angle > pi/2):
                label.set_horizontalalignment('right')
                label.set_verticalalignment('bottom')
            elif angle == pi:
                label.set_horizontalalignment('right')
                label.set_verticalalignment('center')
            elif (angle > pi) and (angle < 3*pi/2):
                label.set_horizontalalignment('right')
                label.set_verticalalignment('top')
            else:
                label.set_horizontalalignment('left')
                label.set_verticalalignment('top')
        ax.set_rlabel_position(30)
        plt.yticks(np.linspace(0, 1, num=6), [str(i*100/5)+"%" for i in range(6)], color="black", size=8)
        plt.ylim(0, 1)
        ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.05))
        plt.show()
