import os
import pickle
import pathlib
import warnings
import glob as gl
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import *
from scipy import interp

from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression

warnings.filterwarnings('ignore')

plt.rc('text', usetex=False)
plt.rc('font', family='serif')
plt.rcParams.update({'font.size': 10})


