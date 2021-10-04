dataAux.py checks consistency between method names in "DS_JK dataset / dot files" and listMeth_labelsMR.csv 

It can be executed from the terminal:

        Python dataAux.py -i Path_to_DS-JK-Dataset\* -o Dataset_name

It'll return a csv file with the name Dataset_name.csv (-o option) 

Method Name	ADD	MUL	PER	INC	EXC	INV
add_values	1	1	1	1	1	1
array_calc	1	1	0	0	0	1
array_copy	1	1	0	0	0	1
autoCorrelation	0	0	0	0	0	0
average	1	1	1	0	0	1
bi_SearchFromTo	0	0	0	1	0	0
bubble	1	1	1	0	0	1
cal_AbsoluteDiff	1	1	0	0	0	1
![image](https://user-images.githubusercontent.com/42596938/135850103-e1b20279-20ce-416c-a4d6-7a1359d06dbc.png)

