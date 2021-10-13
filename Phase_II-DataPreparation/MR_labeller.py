import os
import sys
import pathlib
import warnings
import glob as gl
import numpy as np
import pandas as pd


warnings.filterwarnings('ignore')

def checkUnnameColumn(df):

    colNames = list(df.columns.values)
    for i in colNames:
        if i.find('Unnamed') != -1:
            df.drop(df.filter(regex=i),axis=1, inplace=True)
            break
    
    return df

def check_methodsNames(df_f, df_mr):

    df_f = checkUnnameColumn(df_f)
    df_mr = checkUnnameColumn(df_mr)

    if len(df_mr) != len(df_f):
        print('WARNING: The number of rows is not the same')

    methods_name = list(df_mr['Method_Name'])

    columNameMR = list(df_mr.columns.values)
    for i in columNameMR:
        if i.find('MR_') != -1:
            df_f[i] = np.nan

    for index, row in df_mr.iterrows():
        name = row.at['Method_Name']
        
        match = list(df_f['dot_name'].str.match(name)).index(True)
        index_keys = list(row.keys())
        for j in index_keys:
            df_f.at[match, j] = row.at[j]
    print(df_mr)
    print(df_f)
    df_f.to_csv('test.csv')



if __name__ == '__main__':

    import click

    global df_main
    df_main = pd.DataFrame()

    @click.command()
    @click.option('-i', '--featuresFile', 'f_file', help='Path for getting the features file')
    @click.option('-mr', '--mrListFile', 'mr_file', help='Path for getting the list of MRs file')
    @click.option('-o', '--output', 'output_file', help='Name of the output csv file')

    def main(f_file, mr_file, output_file):

        here_iam = str(pathlib.Path().absolute())
        resultsPath = here_iam + '\\Labelled-Dataset'
        
        if not os.path.exists(resultsPath):
            os.mkdir(resultsPath)

        df_f = pd.read_csv(f_file)
        df_mr = pd.read_csv(mr_file)

        check_methodsNames(df_f, df_mr)

    
main()

