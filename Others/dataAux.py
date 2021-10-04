import os
import sys
import pathlib
import warnings
import glob as gl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.base import NoNewAttributesMixin


data = pd.read_csv('listMeth_labelsMR.csv')

def methNames(dot_path):

    methodsName = []
    for i in dot_path:
        methodsName_aux = i.split('\\')[-1]
        methodsName_aux = methodsName_aux.split('.dot')[0]
        methodsName.append(methodsName_aux)

    return methodsName

def dsFinal(methodsName, df):

    df['same'] = 'NO'
    
    for index, row in df.iterrows():

        mName = row.at['Method Name']
        if mName in methodsName:
            df.at[index, 'same'] = 'yes'

    aux = []
    for i in methodsName:
        exist = i in df.values
        if exist == False:
            aux.append(i)

    if len(aux) >= 1:
        with open('warning.txt', 'w') as f:
            f.write('These methods have a different name or they are not in the files :\n')        
            f.write('\n'.join(aux))

    return df

def save_csv(df):

    df = df.sort_values(by='Method Name', ascending=True)
    df.to_csv('ds_labelled.csv')


if __name__ == '__main__':
    import click

    @click.command()
    @click.option('-i', '--file', 'input', help='Path file')

    def main(input):

       here_iam = str(pathlib.Path().absolute())
       dot_path = gl.glob(input)

       methodsName = methNames(dot_path)
       # print(methodsName)
       finalDataLabelled = dsFinal(methodsName, data)
       save_csv(finalDataLabelled)

main()
