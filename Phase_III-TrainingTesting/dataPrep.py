import os
import pathlib

def checkUnnameColumn(df):

    colNames = list(df.columns.values)
    for i in colNames:
        if i.find('Unnamed') != -1:
            df.drop(df.filter(regex=i),axis=1, inplace=True)
            break
    return df

def find_MR_FTnames(data):
    
    data = checkUnnameColumn(data)
    colNames = list(data.columns)
    MRnames = []
    featureNames = []
    for i in colNames:
        if i.find('MR_') != -1:
            MRnames.append(i)
        
        if i.find('FM_') != -1:
            featureNames.append(i)

        if i.find('NF_') != -1 or i.find('PFS_') != -1 or i.find('PFE_') != -1:
            featureNames.append(i)

    #print(featureNames)
    return MRnames, featureNames

def storage_file(name_dir):

    path = str(pathlib.Path().absolute()) + '\\' + name_dir
    
    if not os.path.exists(path):
        file = name_dir
        os.mkdir(file)

    return os.path


def createDir(mainPath, mr):
    
    try:
        paths = str(pathlib.Path().absolute()) + '\\' + mainPath + '\\' + mr
        if not os.path.exists(paths):
            file =  mainPath + '\\' + mr
            os.mkdir(file)

        return paths
    
    except:
        return paths

def createPickleFile(mainPath, pickleFile, t):
    
    try:
        paths = str(pathlib.Path().absolute()) + mainPath + '\\' + 'TestingX' + pickleFile + '.pkl'
        if not os.path.exists(paths):
            file =  mainPath + '\\'  + 'TestingX' + pickleFile + '.pkl'
            os.mkdir(file)

        return paths
    
    except:
        return paths
