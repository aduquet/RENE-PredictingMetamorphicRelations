import networkx as nx
import numpy as np
from scipy.sparse.linalg import lsqr
from scipy.sparse import lil_matrix, kron, identity

def get_norm(adj_mat):
    norm = adj_mat.sum(axis=0)
    norm[norm == 0] = 1

    return adj_mat / norm


def RWK(X, Y):
    step = 10
    lmb = 1.2
    weighted_sum = 0
    weighted_sum_1 = 0
    weighted_sum_2 = 0
    graph_A = get_norm(nx.adjacency_matrix(X))
    graph_B = get_norm(nx.adjacency_matrix(Y))
    g_prod = kron(lil_matrix(graph_A), lil_matrix(graph_B))
    g_prod_1 = kron(lil_matrix(graph_A), lil_matrix(graph_A))
    g_prod_2 = kron(lil_matrix(graph_B), lil_matrix(graph_B))

    for n in range(step):
        weighted_sum += (g_prod ** n).dot(lmb ** n)
        weighted_sum_1 += (g_prod_1 ** n).dot(lmb ** n)
        weighted_sum_2 += (g_prod_2 ** n).dot(lmb ** n)

    rwk = weighted_sum.sum()
    rwk_1 = weighted_sum_1.sum()
    rwk_2 = weighted_sum_2.sum()
    rwk_norm = rwk / np.sqrt(rwk_1 * rwk_2)

    return rwk_norm

