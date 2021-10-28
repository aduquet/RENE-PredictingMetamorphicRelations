import os
import pathlib
import glob as gl
import numpy as np
import pandas as pd

def dive(df,div):
    for column in df.columns[1:]:
        print(df[column])



if __name__ == '__main__':
    import click
    global df_main
    df_main = pd.DataFrame()


    @click.command()
    @click.option('-i', '--csv input file', 'data_input', help= 'Path to the dot files')
    @click.option('-o', '--csv output file', 'output_file', help= 'Name of the csv output file')

    def main(data_input, output_file):

        here_iam = str(pathlib.Path().absolute())
        resultsPath = here_iam + '\\'
        data = pd.read_csv(data_input, index_col= False)
        size = len(data)
        df = data.copy()
        count = 1
        for index, row in data.iterrows():
            a = 'FM_' + str(count)
            div = row[a]
            count += 1
            count2 = 1
            for i in row:
                a2 = 'FM_' + str(count2)
                if type(i) != str:   
                    b = i/div
                    df.at[index, a2] = b
                    count2 += 1
           
        df.to_csv('test.csv')
        
        #print(output_file)
    
main()