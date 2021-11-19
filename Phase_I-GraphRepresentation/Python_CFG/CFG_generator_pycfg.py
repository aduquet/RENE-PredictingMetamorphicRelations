import os
import re
import sys
import pathlib
import warnings
import glob as gl
import subprocess

warnings.filterwarnings('ignore')


def openTxt(txtPath):
    aux = []
    try:
        txtFile = open(txtPath, 'r')

        for line in txtFile:
            # print(line)
            aux.append(line.replace("\n", ""))
        txtFile.close()
        # print('Done!')
        return aux

    except IOError:
        print("txt file not found or path is incorrect \nCheck and try it again!")
        return -1


def getCFG(methodList, pycfgDefaultPath, py_path, output_dir):
    methodListPath = gl.glob(py_path + '\\*.py')

    for i in methodList:
        for j in methodListPath:
            aux = j.split('\\')[-1]
            aux = aux.split('.')[0]

            if i in aux:
                if len(i) == len(aux):
                    subp = 'python ' + '"' + pycfgDefaultPath + '"' + ' ' + '"' + j + '" ' + '"' + output_dir + '"' + ' -d'
                    subprocess.run(subp)
                    break

    final_path = output_dir.split('pycfg-0.1')[0]

    return final_path


def getCFG_oneFile(methodList, pycfgDefaultPath, py_path, output_dir):
    methodListPath = gl.glob(py_path + '\\*.py')

    for i in methodList:
        for j in methodListPath:
            aux = j.split('\\')[-1]
            aux = aux.split('.')[0]

            if i in aux:
                if len(i) == len(aux):
                    subp = 'python ' + '"' + pycfgDefaultPath + '"' + ' ' + '"' + j + '" ' + '"' + output_dir + '"' + ' -d'
                    subprocess.run(subp)
                    break

    final_path = output_dir.split('pycfg-0.1')[0]

    return final_path


if __name__ == '__main__':

    # To execute:
    #         1. Open anaconda prompt
    #         2. run the command in this way:
    #             CFG_generator_pycfg.py -d F -i "path_to\file.txt" -py "path_to\Python_files" -o "path_to\directory_to_save_outputs"
    #         Example:
    #         CFG_generator_pycfg.py -d F -i "C:\Users\duquet\Documents\GitHub\Pred_MR-Extention\MethodsUsed.txt" -py "C:\Users\duquet\Documents\GitHub\Pred_MR-Extention\Python-Methods" -o "C:\Users\duquet\Documents\GitHub\Pred_MR-Extention\Python_CFG"
    #

    import click


    @click.command()
    @click.option('-d', '--nFile', 'nFiles', help='One file as input press "F" only, "D" for directory')
    @click.option('-i', '--txt file', 'input_path',
                  help='Path for getting Python code, if there are multiple files then provide the .txt path')
    @click.option('-py', '--py file', 'py_path',
                  help='Path for getting Python code, if there are multiple files then provide the .txt path')
    @click.option('-o', '--Path outputs', 'output_dir', help='Path for the outputs')
    @click.option('-pydot', '--Path to nx_pydot', 'pydotPath', help= 'Path to the nx_pydot.py')
    def main(nFiles, input_path, py_path, output_dir, pydotPath):
        print('Processing!')
        # Path to pycfg 
        pycfgDefaultPath = pydotPath
        # "C:\\Users\\duquet\\Anaconda3\\Lib\\site-packages\\pycfg\\pycfg.py"
        # C:\\Users\\duquet\\Documents\\GitHub\\Pred_MR-Extention\\Python CFG\\pycfg-0.1\\pycfg\\pycfg.py"

        methodList = openTxt(input_path)

        if methodList == -1:
            print('Exit')

        else:

            if nFiles == 'D':
                final_path = getCFG(methodList, pycfgDefaultPath, py_path, output_dir)
                print('\n*** Dot files will be saved in ', final_path + '\\dotFiles-pycfgLibrary ***')
                print('*** CFG plot pdf format will be saved in ', final_path + '\\CFG_plotsPDF ***')
                print('*** CFG plot png format will be saved in ', final_path + '\\CFG_plotsPNG ***')

            else:
                try:
                    print('\n*** Dot files will be saved in ', output_dir + '\\dotFiles-pycfgLibrary ***')
                    print('*** CFG plot pdf format will be saved in ', output_dir + '\\CFG_plotsPDF ***')
                    print('*** CFG plot png format will be saved in ', output_dir + '\\CFG_plotsPNG ***')
                    subp = 'python ' + '"' + pycfgDefaultPath + '"' + ' ' + '"' + py_path + '" ' + '"' + output_dir + '"' + ' -d'
                    subprocess.run(subp)

                except IOError:
                    print("txt file not found or path is incorrect \nCheck and try it again!")

main()
