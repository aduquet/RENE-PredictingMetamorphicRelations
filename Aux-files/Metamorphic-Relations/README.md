dataAux.py checks consistency between method names in "DS_JK dataset / dot files" and listMeth_labelsMR.csv wich contains the labels of the Metamorphic Relation (MR). We use the number 1 to denote a method that satisfies a given MR, and  0 to denote a method that does not fulfil a particular MR. 

It can be executed from the terminal:

        Python dataAux.py -i Path_to_DS-JK-Dataset\* -o Dataset_name

It'll return a csv file with the name Dataset_name.csv (-o option) 

Example:

![image](https://user-images.githubusercontent.com/42596938/135850103-e1b20279-20ce-416c-a4d6-7a1359d06dbc.png)

