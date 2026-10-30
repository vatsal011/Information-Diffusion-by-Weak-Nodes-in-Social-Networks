# Influence Maximization in Real-Time Social Networks

## Overview

Influence Maximization focuses on identifying a small set of influential nodes that can maximize information spread across a social network. This project investigates how network structure, weak nodes, echo chambers, and influence maximization algorithms affect information diffusion.

## Methodology

### 1. Information Diffusion through Weak Nodes
- Used the **GEMSEC Facebook Page Network dataset**, covering eight categories of Facebook pages.
- Applied **Metropolis-Hastings Random Walk (MHRW)** sampling and Louvain community detection.
- Compared information diffusion from weak nodes against nodes selected using Betweenness and Eigenvector Centrality across different seed set sizes and geodesic distances.

### 2. Echo Chambers and Information Virality
- Generated networks using the **Erdős–Rényi graph model**.
- Implemented **SIR-CA** and ODE-based continuous-time diffusion models.
- Studied the effects of contact rate, environmental intake capacity, network polarization, and opinion polarization on information spread.

### 3. Influence Maximization Algorithms
- Implemented **DHICM** on Erdős–Rényi graphs.
- Implemented and compared **Greedy** and **CELF** algorithms using a Twitter network dataset.
- Evaluated their performance based on information spread and computational time.

## Key Findings

- Betweenness Centrality achieved the highest information diffusion across Facebook network categories, followed closely by the weak-node approach.
- Echo chambers with moderate network polarization (0.5–0.7) enhanced information virality, while polarization above 0.8 restricted information spread.
- Higher contact rates and environmental intake capacity increased oscillations and delayed diffusion stability.
- CELF achieved the highest information spread and significantly reduced computation time compared to the baseline Greedy algorithm.

## Tech Stack

**Python 3.8+ | NetworkX | Matplotlib | Jupyter Notebook | Anaconda | VS Code | Git | GitHub**
