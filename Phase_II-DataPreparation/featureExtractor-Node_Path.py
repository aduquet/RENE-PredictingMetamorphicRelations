import os
import pathlib
import warnings
import glob as gl
from collections import defaultdict

import numpy as np
import pandas as pd
import networkx as nx
import nx_pydot as pydot

import networkx.algorithms.simple_paths as simple_paths

warnings.filterwarnings('ignore')


def getOp(myName):
    if myName.find('=') == -1:
        # print(myName)
        return 'ERROR'
    else:
        if myName.find('+') != -1:
            return 'add'
        elif myName.find('-') != -1:
            return 'sub'
        elif myName.find('&') != -1:
            return 'and'
        elif myName.find('cmp') != -1:
            return 'cmp'
        elif myName.find('cmpg') != -1:
            return 'cmpg'
        elif myName.find('cmpl') != -1:
            return 'cmpl'
        elif myName.find('/') != -1:
            return 'div'
        elif myName.find('==') != -1:
            return 'eql'
        elif myName.find('>=') != -1:
            return 'geql'
        elif myName.find('>') != -1:
            return 'gt'
        elif myName.find('<=') != -1:
            return 'leql'
        elif myName.find('<') != -1:
            return 'lt'
        elif myName.find('*') != -1:
            return 'mul'
        elif myName.find('!=') != -1:
            return 'neqlL'
        elif myName.find('|') != -1:
            return 'or'
        elif myName.find('%') != -1:
            return 'rem'
        elif myName.find('<<') != -1:
            return 'shl'
        elif myName.find('>>') != -1:
            return 'shr'
        elif myName.find('xor') != -1:
            return 'xor'
        else:
            return 'assi'


def get_node_labels(cfg):
    # print(cfg.edges())
    nodes = cfg.nodes()
    node_names = nx.get_node_attributes(cfg, 'label')
    # print(node_names)
    node_labels = {}

    for n in nodes:
        myName = node_names[n]
        if myName.find('if') != -1:
            nodeLabel = 'If'
        elif myName.find(':=') != -1:
            nodeLabel = 'eqltostmt'
        elif myName.find('goto') == 0 or myName.find('goto') == 1:
            nodeLabel = 'goto'
        elif myName.find('exit') != -1:
            nodeLabel = 'exit'
        elif myName.find('return') != -1:
            nodeLabel = 'return'
        elif (myName.find('(') != -1 and myName.find(')') != -1 and (
                myName.find('double') != -1 or myName.find('float') != -1 or myName.find('int') != -1)):
            nodeLabel = 'assi'
        elif myName.find('(') != -1 and myName.find(')') != -1:
            nodeLabel = 'fcall'
        else:
            nodeLabel = getOp(myName)
        node_labels[n] = nodeLabel
    return node_labels


def cfg_preprocess(fileName):
    cfg = pydot.read_dot(fileName)
    cfg2 = pydot.read_dot(fileName)
    # Find the number of weakly connected components in the CFG
    c = nx.number_weakly_connected_components(cfg)

    # create a list node,indegree,outdegree
    data = []
    # n : list of nodes
    n = cfg.nodes()
    edge = cfg.edges()
    # print(edge)
    aux = []
    for i in edge:
        a = cfg.get_edge_data(*i)
        if str(a).find('DD') != -1:
            cfg2.remove_edge(*i)

            if str(a).find('cfg') != -1:
                aux.append(i)
    aux = list(set(aux))

    for i in aux:
        cfg2.add_edge(*i)

    return cfg2


def find_node_counts(fileName):
    # print(fileName)
    cfg2 = cfg_preprocess(fileName)
    data = []
    node_labels = get_node_labels(cfg2)
    # print(node_labels)

    for x in node_labels:
        y = str(node_labels[x]) + '-' + str(cfg2.in_degree(x)) + '-' + str(cfg2.out_degree(x))
        data.append(y)
    # print(data)

    # create a set from the list to get the non repeating features
    feature = set(data)
    # create a dictionary with the feature node, indegree, outdegree and the counmt
    feature_counts = {}

    for i in feature:
        feature_counts[i] = 0
    # print(feature_counts)

    for i in data:
        feature_counts[i] = feature_counts[i] + 1

    # print(feature_counts)
    return feature_counts


def get_node_counts(paths):
    node_data = {}
    # print(paths)
    count = 0
    for file in paths:
        name = file.split('\\')[-1]
        name = name.split('.dot')[0]
        node_data[name] = find_node_counts(file)
        # print(node_data)
        # if count == 4:
        #     break
        #
        # count += 1
    return node_data
    # print node_data


def get_path_in_labels(path, node_labels):
    # print('', path, '\n')
    path_labels = ''
    for n in path:
        label = node_labels[n]
        path_labels += str(label) + '-'
    return path_labels


def find_paths_from_start(file):
    global start
    # print(file)
    cfg = cfg_preprocess(file)
    nodes = cfg.nodes()

    start_name_path_counts = {}
    # nx.draw_kamada_kawai(cfg,with_labels=True)
    # plt.show()

    node_labels = get_node_labels(cfg)
    # print('Nodes: ', nodes)
    # print('Nodel Labels: ', node_labels)

    for n in nodes:
        if len(list(cfg.predecessors(n))) == 0:
            start = n

    paths_from_start = nx.shortest_path(cfg, start)
    # print(paths_from_start)

    all_paths_from_start_names = []
    for i in paths_from_start:
        all_paths_from_start_names.append(get_path_in_labels(paths_from_start[i], node_labels))

    start_path_names = set(all_paths_from_start_names)

    # for i in all_paths_from_start_names:
    #     print('\n', i)

    for i in start_path_names:
        start_name_path_counts[i] = 0

    for i in all_paths_from_start_names:
        start_name_path_counts[i] += 1

    # print(start_name_path_counts)
    return start_name_path_counts


def find_paths_to_end(file):
    # print(file)
    cfg = cfg_preprocess(file)
    nodes = cfg.nodes()

    ends = []
    for n in nodes:
        succ = list(cfg.successors(n))
        if len(succ) == 0:
            ends.append(n)

    all_paths_to_end = []
    for i in ends:
        for n in nodes:
            if n != '0':
                # print('**', n)
                try:
                    path = nx.shortest_path(cfg, source=n, target=i)
                    all_paths_to_end.append(path)
                except nx.exception.NetworkXNoPath:
                    var = 1

    node_labels = get_node_labels(cfg)

    all_paths_to_end_names = []
    for i in all_paths_to_end:
        all_paths_to_end_names.append(get_path_in_labels(i, node_labels))

    end_path_names = set(all_paths_to_end_names)
    end_name_path_counts = {}

    for i in end_path_names:
        end_name_path_counts[i] = 0

    for i in all_paths_to_end_names:
        end_name_path_counts[i] += 1
    return end_name_path_counts


def get_name_dot(paths):
    name = paths.split('\\')[-1]
    name = name.split('.dot')[0]
    return name


def get_start_to_node_path_data(paths):
    start_to_node_path_name_data = {}

    for file in paths:
        name = get_name_dot(file)
        f_paths = find_paths_from_start(file)
        # print(f_paths)
        start_to_node_path_name_data[name] = f_paths
        # print(start_to_node_path_name_data)
    return start_to_node_path_name_data


def get_node_to_end_path_data(paths):
    node_to_end_path_name_data = {}

    for file in paths:
        name = get_name_dot(file)
        end_paths = find_paths_to_end(file)
        node_to_end_path_name_data[name] = end_paths
        # print(node_to_end_path_name_data)
    return node_to_end_path_name_data


def update_df_main(ind, node_data, ft):
    for index, row in df_main.iterrows():
        a = row.at['dot_name']
        if a == ind:
            # print(a)
            for j in node_data:
                # print(node_data[j])
                new_colum = ft + j
                df_main.at[index, new_colum] = node_data[j]


if __name__ == '__main__':

    import click

    global df_main
    df_main = pd.DataFrame()

    @click.command()
    @click.option('-i', '--dotFile', 'dot_file', help='Path for getting the dot file')
    @click.option('-o', '--output', 'output_file', help='Name of the output csv file ')

    def main(dot_file, output_file):

        global df_main
        df_main = pd.DataFrame()

        here_iam = str(pathlib.Path().absolute())
        resultsPath = here_iam + '\\NodePath_Features'
        
        if not os.path.exists(resultsPath):
            os.mkdir(resultsPath)

        dot_path = gl.glob(dot_file)
        # input_file = gl.glob(input_file)

        df_main = pd.DataFrame(columns=['dot_name', 'dot_path'], index=None)

        dot_name = []
        dot_path_aux = []

        ''' Node feature '''
        for dot in dot_path:
            name = dot.split('\\')[-1]
            name = name.split('.dot')[0]
            dot_name.append(name)
            dot_path_aux.append(dot)
        df_main['dot_name'] = dot_name
        df_main['dot_path'] = dot_path_aux
        #print(df_main)
        node_data = get_node_counts(dot_path)
        # print(node_data)

        '''Path feature'''
        start_path_name_data = get_start_to_node_path_data(dot_path)
        # print(start_path_name_data)

        end_path_name_data = get_node_to_end_path_data(dot_path)
        # print(end_path_name_data)

        for i in node_data:
            update_df_main(i, node_data[i], 'NF_')

        for i in start_path_name_data:
            update_df_main(i, start_path_name_data[i], 'PFS_')

        for i in end_path_name_data:
            update_df_main(i, end_path_name_data[i], 'PFE_')

        df_main = df_main.fillna(0)
        
        if output_file.find('.') != -1:
            output_file = output_file.split('.')[0]

        resultsPath = resultsPath + '\\' + output_file + '.csv'
        df_main.to_csv(resultsPath)
        print('\n Done! The file has been saved in: ', resultsPath )

main()
