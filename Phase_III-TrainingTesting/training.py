import pickle
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from dataPrep import *
from sklearn.svm import SVC
from sklearn.metrics import *
from scipy import interp
from sklearn.model_selection import StratifiedKFold

warnings.filterwarnings('ignore')

plt.rc('text', usetex=False)
plt.rc('font', family='serif')
plt.rcParams.update({'font.size': 10})

def saveTrainTesting(mainPath, x, y, mr, j, ns, t):

    if t == 'tr':
        pkl_name_train_x = mainPath + '\\' + 'TrainingX_' + mr + '_' + j + '_' + ns +'folds.pkl'
        with open(pkl_name_train_x, 'wb') as file:
            pickle.dump(x, file)

        pkl_name_train_y = mainPath + '\\' + 'TrainingY_' + mr + '_' + j + '_' + ns +'folds.pkl'

        with open(pkl_name_train_y, 'wb') as file:
            pickle.dump(y, file)

    if t == 'ts':
        pkl_name_test_x = mainPath + '\\' + 'TestingX_' + mr + '_' + j + '_' + ns + 'folds.pkl'

        with open(str(pkl_name_test_x), 'wb') as file:
            pickle.dump(x, file)

        pkl_name_test_y = mainPath + '\\' + 'TestingY_' + mr + '_' + j + '_' + ns + 'folds.pkl'
        with open(pkl_name_test_y, 'wb') as file:
            pickle.dump(y, file)


def saveModel(mainPath, model, mr, j, ns):
    pkl_name_train_x = mainPath + '\\' + 'model_' + mr + '_' + j + '_' + ns +'folds.pkl'
    
    with open(pkl_name_train_x, 'wb') as file:
        pickle.dump(model, file)

if __name__ == '__main__':  
    import click

    @click.command()
    @click.option('-i', '--file', 'data', help='Path of labelled Dataset')
    @click.option('-ns', '--nSplits', 'ns', help='Number of splits')

    def main(data, ns):
        
        mainPath_name = data.split('\\')[-1]
        mainPath_name = mainPath_name.split('.')[0]
        mainPath = storage_file(mainPath_name)

        random_state = np.random.RandomState(0)

        SVM = SVC(C=1000, probability=True, random_state=random_state)
        skf = StratifiedKFold(n_splits=int(ns))

        df = pd.read_csv(data)
        MR_names, FT_names = find_MR_FTnames(df)
      
        data=np.asarray(df[FT_names])

        if len(MR_names) > 1: 
            for i in MR_names:    
                mainPath2 = createDir(mainPath_name, i)
                nameModel = 'Models_' + i
                modelPath = createDir(mainPath_name, nameModel)
                labels = np.asarray(df[i])
                j = 0
                for train_index, test_index in skf.split(data, labels):
                    x_train, x_test = data[train_index], data[test_index]
                    y_train, y_test = labels[train_index], labels[test_index]
                    j = j + 1
                    saveTrainTesting(mainPath2, x_train, y_train, i, str(j), ns, t='tr')
                    saveTrainTesting(mainPath2, x_test, y_test, i, str(j), ns , t='ts')
                    model_RWK = SVM.fit(x_train, y_train)
                    saveModel(modelPath, model_RWK, i, str(j), ns)

                    prediction = model_RWK.predict_proba(x_test)
                    predic = prediction[:, 1]
                    precision, recall, thresholds = precision_recall_curve(y_test, predic)
                    auc1 = roc_auc_score(y_test, predic)
                    print(auc1)
                    #print(classification_report(y_test, predic))
                    #print(precision, recall, thresholds)

# python training.py -i "C:\Users\duquet\Documents\GitHub\RENE-PredictingMetamorphicRelations\Phase_II-DataPreparation\Labelled-Dataset\RWK_DS_JK.csv" -ns 10 

main()
