# RENE-PredictingMetamorphicRelations: Replication Package 
Metamorphic Test (MT) is a software testing technique that addresses the test oracle issue. It differs from traditional testing techniques in that it looks at the relations between the inputs and outputs of different test cases executions rather than specific test results. Such relations are known as Metamorphic Relationships (MRs), and they are the MT core aspect. In MT, testers may indirectly test the System Under Test (SUT) by looking at whether the inputs and outputs meet the MRs. If a particular MR is not violated, it does not guarantee that the program will be implemented correctly. However, if an MR is violated for certain test cases, then there must be a fault in the SUT. MRs are currently discovered manually, which necessitates a thorough grasp of the SUT and the application domain. As a result, MT might take a long time and be prone to errors. To mitigate this problem, the metamorphic relationship prediction (PMR) approach was proposed. PMR uses a classification model based on features gathered from the SUT source code, at the method level, to predict whether a  new method would exhibit a particular predefined MR. The goal of our research is to investigate how effectively the suggested PMR approach, which has been tested on Java methods, may be applied to other programming languages. To do this, we first replicated the prior work and then expanded the PMR to Python and C++.

This repository contains the scripts and dataset used in the paper A Replication Study on Predicting Metamorphic Relations. Contains four main files

    Java experimentations

    Python experimentations
    
    C++ Experimentations
