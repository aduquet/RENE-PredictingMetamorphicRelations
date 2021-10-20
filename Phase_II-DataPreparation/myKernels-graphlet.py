import networkx as nx
import itertools
#import SootUtilities as sutil
import sys
import os

def nodeLabelExactMatch(nodeMap,labels):

	check=True
	for i in nodeMap:
		if labels[i]!=labels[nodeMap[i]]:
			check=False
	return check

def getSubgraphs(graph,size):

	nodes = graph.nodes()
	labels = nx.nodes(graph) 
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

#calculate the kernel value k_subgraph(subg1,subg2) for two subgraphs 
def calcSubgraphKernelVal(subg1,subg1NodeLabels,subg2,subg2NodeLabels):

	DiGM = nx.isomorphism.DiGraphMatcher(subg1,subg2)
	if DiGM.is_isomorphic():
		nodeMap=DiGM.mapping
		k_subgraph=1
		for n in nodeMap:
			k_subgraph=k_subgraph*getNodeKernelValExactEqual(subg1NodeLabels[n],subg2NodeLabels[nodeMap[n]])
	else:
		k_subgraph=0
	return k_subgraph

def getNodeKernelValExactEqual(l1,l2):

	if(l1 == l2): 
		return 1

	else:
		return 0

def getNodeKernelVal(l1,l2):
	
	if(l1==l2):
		return 1
		

	else:
		return 0.001


g1=nx.drawing.nx_pydot.read_dot('C:/Users/duquet/Documents/GitHub/RENE-PredictingMetamorphicRelations/Java/Java dot files - from Kanewala/clip.dot')
g2=nx.drawing.nx_pydot.read_dot('C:/Users/duquet/Documents/GitHub/RENE-PredictingMetamorphicRelations/Java/Java dot files - from Kanewala/sum.dot')
g1NodeLabels=nx.nodes(g1,)
g1Graphlets = getSubgraphs(g1, 1)
g2NodeLabels = nx.nodes(g2)
g2Graphlets = getSubgraphs(g2, 1)
val=calcGraphletKernelVal(g1Graphlets,g1NodeLabels,g2Graphlets,g2NodeLabels)
print(val)
# create_graphlet_kernel_matrix(sys.argv[1],sys.argv[2],int(sys.argv[3]))
