import networkx as nx
import numpy as np
from scipy.sparse.linalg import lsqr
from scipy.sparse import lil_matrix, kron, identity
import itertools

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

def nodeLabelExactMatch(nodeMap,labels):
	check=True
	for i in nodeMap:
		if labels[i]!=labels[nodeMap[i]]:
			check=False
	return check

def getSubgraphs(graph,size):

	nodes = graph.nodes()
	labels = nx.get_node_attributes(graph, 'label') 
	combs = itertools.combinations(nodes,size)
	connectedSubgs = []
	subgs = {}

	for i in combs:
		subg=graph.subgraph(i)
		if nx.is_weakly_connected(subg):
			connectedSubgs.append(subg)   

	for i in connectedSubgs:
		cnt=1	
		for j in connectedSubgs:
			#print j
			if i!=j:
				DiGM = nx.isomorphism.DiGraphMatcher(i,j)
				if DiGM.is_isomorphic():
					nodeMap=DiGM.mapping
					if nodeLabelExactMatch(nodeMap, labels):
						cnt+=1
						connectedSubgs.remove(j)
		
		subgs[i]=float(cnt)/float(len(connectedSubgs)) 
	
	return subgs


#calculates the k_graph(G,G') for two graphs 
def calcGraphletKernelVal(g1Graphlets,g1NodeLabels,g2Graphlets,g2NodeLabels):

	k_graph=0
	for i in g1Graphlets:
		for j in g2Graphlets:
			k_graph += calcSubgraphKernelVal(i,g1NodeLabels,j,g2NodeLabels)*g1Graphlets[i]*g2Graphlets[j]
	return k_graph			 

def getNodeKernelValExactEqual(l1,l2):
    if(l1 == l2): 
        return 1
    else:
        return 0

#calculate the kernel value k_subgraph(subg1,subg2) for two subgraphs 
def calcSubgraphKernelVal(subg1,subg1NodeLabels,subg2,subg2NodeLabels):
    
    DiGM = nx.isomorphism.DiGraphMatcher(subg1,subg2)

    if DiGM.is_isomorphic():
        nodeMap=DiGM.mapping
        k_subgraph=1
        for n in nodeMap:
            k_subgraph=k_subgraph*getNodeKernelValExactEqual(subg1NodeLabels[n],subg2NodeLabels[n])
    else:
        k_subgraph = 0
	
    return k_subgraph

def GK(g1, g2, s):
    # g1=nx.drawing.nx_pydot.read_dot('C:/Users/duquet/Documents/GitHub/RENE-PredictingMetamorphicRelations/Java/Java dot files - from Kanewala/pooledVariance.dot')
    # g2=nx.drawing.nx_pydot.read_dot('C:/Users/duquet/Documents/GitHub/RENE-PredictingMetamorphicRelations/Java/Java dot files - from Kanewala/add_values.dot')
    
    if len(nx.get_node_attributes(g1, 'label')) < len(nx.get_node_attributes(g2, 'label')):
        # print('****')
        g1Graphlets = getSubgraphs(g1, s)
        g2Graphlets = getSubgraphs(g2, s)
        g1NodeLabels = nx.get_node_attributes(g1, 'label')
        g2NodeLabels = nx.get_node_attributes(g2, 'label')
    else:
        g1Graphlets = getSubgraphs(g2, s)
        g2Graphlets = getSubgraphs(g1, s)
        g1NodeLabels = nx.get_node_attributes(g2, 'label')
        g2NodeLabels = nx.get_node_attributes(g1, 'label')

    
    val=calcGraphletKernelVal(g1Graphlets,g1NodeLabels,g2Graphlets,g2NodeLabels)
    # print(val) 
    return val
    # create_graphlet_kernel_matrix(sys.argv[1],sys.argv[2],int(sys.argv[3]))