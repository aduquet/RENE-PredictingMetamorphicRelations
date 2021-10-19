This directory contains the scripts to perform the phase II of PMR, i.e., "Phase II-Data Preparation" 

Overall, phase II is in charge of extracting a set of features from the CFGs (Control Flow Graph). Also, to each method’s CFG zero to six pre-defined MRs are assigned.

The script _**Requirements.py**_ will install all the necessary libraries and dependencies for the  _**featureExtractor-Node_Paths.py**_, _**featureExtractor-RWK.py**_, _**featureExtractor-GK.py**_, and _**MR_labeller.py**_ scripts. We suggest using Anaconda Prompt

To execute _**Requirements.py**_ follow the command line:
	
	Python Requirements.py

The script **_nx_pydot.py_** needs to be in the same directory as the other scripts, i.e., _**featureExtractor-Node_Paths.py**_, _**featureExtractor-RWK.py**_, _**featureExtractor-GK.py**_, and _**MR_labeller.py**_

For more info about **_nx_pydot.py_** please visit

	PyDotPlus:     https://github.com/carlos-jenkins/pydotplus
	Graphviz:      http://www.research.att.com/sw/tools/graphviz/
	DOT Language:  http://www.graphviz.org/doc/info/lang.html


The script _**featureExtractor-Node_Path.py**_, extracts features related to the CFG's nodes and paths. This script will create the directory _**NodePath_Features**_ (if is not created), and it will save a CSV file with the features extracted.   

To executed _**featureExtractor-Node_Path.py**_ open Anaconda Prompt and follow the command line:

	Python featureExtractor-Node_Path.py -i "Path to the dot files" -o "Name of the csv file"

Example:

	(base) C:> Python featureExtractor-Node_Path.py -i "C:\RENE-PredictingMetamorphicRelations\Java\Java dot files - from Kanewala\*" -o "test"

If everything goes well, the directory _**NodePath_Features**_ will be created and the "Namde of the csv file" file will be there. Also, in the terminal will appear the following message

 	Done! The file has been saved in:  C:\RENE-PredictingMetamorphicRelations\Phase_II-DataPreparation\NodePath_Features\test.csv 

The csv file will looks like:

![image](https://user-images.githubusercontent.com/42596938/137895252-1a87eeac-555e-4180-8a8a-7ee749e36626.png)


The script  _**featureExtractor-RWK.py**_, extracts feature related to CFGs based on similarity measurements. Specifically, it calculates the random walk kernel between all the graphs. The values of the similarity measure are in the range [0-1], 0 means that two graphs have no similarity, 1 means that the two graphs are the same. Therefore, it is expected to have a matrix with a diagonal with ones. This script will create the _ ** RWK_Features ** _ directory (if not already created), and will save a CSV file with the extracted features.

To executed _**featureExtractor-RWK.py**_ open Anaconda Prompt and follow the command line:

	Python featureExtractor-RWK.py -i "Path to the dot files" -o "Name of the csv file"

Example:

	(base) C:\RENE-PredictingMetamorphicRelations\Phase_II-DataPreparation>python featureExtractor-RWK.py -i "C:\RENE-PredictingMetamorphicRelations\Java\Java dot files - from Kanewala\*" -o RWK_DS-JK 

If everything goes well, the directory _**NodePath_Features**_ will be created and the "Namde of the csv file" file will be there. Also, in the terminal will appear the following message

 	 DONE! File saved in: C:\RENE-PredictingMetamorphicRelations\Phase_II-DataPreparation\RWK_Features\RWK_DS-JK.csv  

The _ ** MR_labeller.py ** _ script labels the methods with a set of MR. Its inputs are the characteristics file and the MR list with its values.
The MR list must be a CSV file, specifying the name of the methods and each MR must have the prefix "MR_"

Example:

![image](https://user-images.githubusercontent.com/42596938/137913149-5775901c-0184-496e-857d-51e0b8c3bec4.png)

To executed _ ** MR_labeller.py ** _ open Anaconda Prompt and  follow the command line:

	python MR_labeller.py -i "path to the features.csv file" -mr "path to the list of MRs csv file" -o " Name of the new csv file"
	

Example:

	python MR_labeller.py -i "C:\RENE-PredictingMetamorphicRelations\Phase_II-DataPreparation\NodePath_Features\NF-PF_DS-JK.csv" -mr "C:\RENE-PredictingMetamorphicRelations\listMeth_labelsMR copy.csv" -o test

If everything goes well, the directory _**Labelled-Dataset**_ will be created and the "Namde of the csv file" file will be there. Also, in the terminal will appear the following message.

	 DONE! File saved in: C:\RENE-PredictingMetamorphicRelations\Phase_II-DataPreparation\Labelled-Dataset\test.csv 

If the list of MRs contains less number of methods than the features file (check the file Labelled-Dataset\test2.csv)

	*** WARNING: The number of rows is not the same. 
	If there are empty spaces, they will be filled with NaN *** 

 The csv files used in our paper **"A Replication Study on Predicting MetamorphicRelations at Unit Testing Level"** are:
 	
	NodePath_Features\NF-PF_DS-JK.csv
	Labelled-Dataset\NF-PF_DS_JK-labelled.csv
	
	RWK_Features\RWK_DS-JK.csv
	Labelled-Dataset\RWK_DS_JK-labelled.csv
	
	
