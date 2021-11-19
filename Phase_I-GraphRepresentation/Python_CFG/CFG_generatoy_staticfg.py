
import os
import re
import sys
import pathlib
import warnings
import glob as gl
import subprocess

# from py2cfg import CFGBuilder
# from add_values import add_values



def cfgGenerator(main_path, method, name):
    #print(main_path)
    cfg = CFGBuilder().build_from_file("prueba","C:/Users/duquet/Documents/GitHub/Pred_MR-Extention/Python-Methods/add_two_array_values.py" )
    cfg.build_visual(name, 'dot')
