import os
import sys
import networkx as nx


from myKernels import *



g1=nx.drawing.nx_pydot.read_dot('C:/Users/duquet/Documents/GitHub/RENE-PredictingMetamorphicRelations/Java/Java dot files - from Kanewala/sum.dot')
g2=nx.drawing.nx_pydot.read_dot('C:/Users/duquet/Documents/GitHub/RENE-PredictingMetamorphicRelations/Java/Java dot files - from Kanewala/sum.dot')
g1NodeLabels=nx.nodes(g1)
g1Graphlets = getSubgraphs(g1, 1)
print(len(g1NodeLabels))
g2NodeLabels = nx.nodes(g2)
g2Graphlets = getSubgraphs(g2, 1)
val=calcGraphletKernelVal(g1Graphlets,g1NodeLabels,g2Graphlets,g2NodeLabels)
print(val)
# create_graphlet_kernel_matrix(sys.argv[1],sys.argv[2],int(sys.argv[3]))
