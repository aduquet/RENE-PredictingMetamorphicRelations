import os
import pathlib
import networkx
import glob as gl
import numpy as np
import pandas as pd

from myKernels import *
from scipy.sparse.linalg import lsqr
from scipy.sparse import lil_matrix, kron, identity


def get_names(paths):
    
    dot_name = []
    dot_path_aux = []
    for dot in paths:
        name = dot.split('\\')[-1]
        name = name.split('.dot')[0]
        dot_name.append(name)
        dot_path_aux.append(dot)
    df_main['dot_name'] = dot_name
    df_main['dot_path'] = dot_path_aux

    return df_main

def read_dot(names_paths_df):
    paths = names_paths_df['dot_path']
    cfg_final = []
    for i in paths:
        cfg = networkx.drawing.nx_pydot.read_dot(i)
        cfg_final.append(cfg)
    # print(len(cfg_final))
    return cfg_final

def create_df(matrixK, dot_names, matrixk):

    columnsName = []

    for i in range(np.shape(matrixK)[0]):
        name = 'FM_' + str(i+1)
        columnsName.append(name)
    
    index = list(dot_names['dot_name'])

    df_rwk = pd.DataFrame(matrixK, columns= columnsName, index= index)
    
    return df_rwk 

def saveFile(df, path, output):

    if output.find('.') != -1:
        output = output.split('.')[0]
    
    finalPath = path + '\\' + output + '.csv'
    df.to_csv(finalPath)
    print('\n DONE! File saved in: \n ', finalPath )


if __name__ == '__main__':
    import click
    global df_main
    df_main = pd.DataFrame()


    @click.command()
    @click.option('-i', '--csv input file', 'dot_input', help= 'Path to the dot files')
    @click.option('-o', '--csv output file', 'output', help= 'Name of the csv output file')

    def main(dot_input, output):

        here_iam = str(pathlib.Path().absolute())
        resultsPath = here_iam + '\\RWK_Features'
        
        if not os.path.exists(resultsPath):
            os.mkdir(resultsPath)

        dot_path = gl.glob(dot_input)
        names_paths_df = get_names(dot_path)

        cfg_main = np. asarray(read_dot(names_paths_df))

        matrixK = np.zeros([len(cfg_main), len(cfg_main)])

        for i in range(0, np.shape(matrixK)[0]):
            for j in range(0, np.shape(matrixK)[1]):        
                matrixK[i, j] = RWK(cfg_main[i], cfg_main[j])

        df_rwk = create_df(matrixK, df_main, matrixK)

        saveFile(df_rwk, resultsPath, output)

main()