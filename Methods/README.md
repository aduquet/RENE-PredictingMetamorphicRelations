\begin{table*}[!ht]
	\caption{List of methods with their MRs label}
	\label{tbl:dataset_with_MRs}
	\centering
	\resizebox{\linewidth}{!} {
	\begin{tabular}{c|l|lll|cccccc|c|l|lll|cccccc}
		\toprule
		\textbf{ID}& \textbf{Method Name}& \multicolumn{3}{c}{\textbf{Library}}&\multicolumn{6}{c|} {\textbf{Metamorphic Relation}}&
		\textbf{ID}& \textbf{Method Name}& \multicolumn{3}{c}{\textbf{Library}}&\multicolumn{6}{c} {\textbf{Metamorphic Relation}}\\
		&& \textbf{JV} & \textbf{PY} &\textbf{C++} &\textbf{ADD}&\textbf{MUL}&\textbf{PER}&\textbf{INC}&\textbf{EXC}&\textbf{INV}&
		&&\textbf{JV} & \textbf{PY} &\textbf{C++}
		&\textbf{ADD}&\textbf{MUL}&\textbf{PER}&\textbf{INC}&\textbf{EXC}&\textbf{INV}\\
		\midrule
		1	&	add\_values         & Colle & Own & Own     &	1	&	1	&	1	&	1	&	1	&	1	&	
		51	&	find\_median	    & Colle & Num & Blinz   &    1	&	1	&	1	&	0	&	0	&	1	\\
        
        2	&	array\_calc 	    & Colle & Num & Own     &	1	&	1	&	0	&	0	&	0	&	1	&	
        52	&	find\_min	        & Colle & Num & Blinz   &	1	&	1	&	1	&	0	&	0	&	1	\\
        
        3	&	array\_copy	        & Colle & Num & Own     &	1	&	1	&	0	&	0	&	0	&	1	&	
        53	&	g\_Test	            & Math  & Own & Own     &	0	&	1	&	0	&	1	&	1	&	1	\\
        
        4	&	autoCorrelation	    & Colt  & Num & Own     &	0	&	0	&	0	&	0	&	0	&	0	&	
        54	&	geometric\_mean	    & Colle & Own & Blinz   &	1	&	1	&	1	&	0	&	0	&	1	\\
        
        5	&	average	            & Colle & Num & Blinz   &	1	&	1	&	1	&	0	&	0	&	1	&	
        55	&	get\_array\_value	& Colle & Num & Own     &	1	&	1	&	0	&	1	&	1	&	1	\\
        
        6	&	bi\_SearchFromTo	& Colt & Num & Own      &	0	&	0	&	0	&	1	&	0	&	0	&	
        56	&	hamming\_dist	    & Colle& Num & Own      &	0	&	0	&	0	&	1	&	1	&	1	\\
        
        7	&	bubble	            & Math & Num & Own      &	1	&	1	&	1	&	0	&	0	&	1	&	
        57	&	harmonicMean	    & Colt & Num & Own      &	1	&	1	&	1	&	0	&	0	&	1	\\
        
        8	&	cal\_AbsoluteDiff	& Math & Num & Blinz    &	1	&	1	&	0	&	0	&	0	&	1	&	
        58	&	insertion\_sort	    & Colle& Num & Own      &	1	&	1	&	1	&	0	&	0	&	1	\\
        
        9	&	cal\_Diff           & Math & Num & Blinz    &	0	&	0	&	0	&	0	&	0	&	0	&	
        59	&	kurtosis	        & Colt & Own & Own      &	1	&	1	&	1	&	0	&	0	&	0	\\
        
        10	&	chebyshevDist	    & Maho & Num & Own      &	0	&	1	&	0	&	1	&	1	&	1	&	
        60	&	lag 	            & Colt & Own & Own      &	0	&	1	&	0	&	0	&	0	&	0	\\
        
        11	&	checkNonNegative	& Math & Own & Own      &	0	&	1	&	1	&	1	&	0	&	1	&	
        61	&	manhattanDist	    & Maho & Num & Own      &	0	&	1	&	0	&	1	&	1	&	1	\\
        
        12	&	checkPositive	    & Math & Own & Own      &	0	&	1	&	1	&	1	&	0	&	1	&	
        62	&	manhattanDist2	    & Colle& Own & Own      &	0	&	1	&	0	&	1	&	1	&	1	\\
        
        13	&	check\_equal	    & Colle& Own & Own      &	0	&	0	&	0	&	0	&	0	&	0	&	
        63	&	max	                & Colt & Num & Blinz    &	1	&	1	&	1	&	1	&	1	&	1	\\
        
        14	&	check\_eq\_tolerance& Colle& Num & Own      &	0	&	0	&	0	&	0	&	0	&	0	&	
        64	&	meanDeviation	    & Colt & Num & Blinz    &	1	&	0	&	1	&	0	&	0	&	0	\\
        
        15	&	chiSquare	        & Math & Num & Own      &	0	&	1	&	0	&	0	&	0	&	1	&	
        65	&	mean\_Diff	        & Math & Num & Blinz    &	0	&	0	&	0	&	0	&	0	&	0	\\
        
        16	&	clip	            & Colle & Num & Own     &	0	&	0	&	0	&	0	&	0	&	0	&	
        66	&	mean\_abs\_error	& Colle & Num & Blinz   &	0	&	1	&	0	&	0	&	0	&	1	\\
        
        17	&	cnt\_zeroes	        & Colle & Own & Own     &	0	&	0	&	1	&	1	&	1	&	0	&	
        67	&	min	                & Colt & Num & Blinz    &	1	&	1	&	1	&	0	&	0	&	1	\\
        
        18	&	canberraDist	    & Math & Num & Own      &	0	&	0	&	0	&	1	&	1	&	1	&	
        68	&	partition	        & Math & Own & Own      &	0	&	0	&	0	&	0	&	0	&	0   \\
        
        19	&	cal\_DividedDiff	& Own  & Own & Own      &	1	&	0	&	0	&	0	&	0	&	0	&	
        69	&	polevl	            & Colt & Num & Own      &	1	&	1	&	0	&	1	&	1	&	1	\\
        
        20	&	cosineDist	        & Maho & Num & Own      &	0	&	1	&	0	&	0	&	0	&	0	&	
        70	&	pooledMean	        & Colt & Num & Own      &	1	&	1	&	1	&	0	&	0	&	1	\\
        
        21	&	count\_k            & Colle & Num & Own     &	0	&	0	&	1	&	1	&	1	&	0	&	
        71	&	pooledVariance	    & Colt & Num & Blinz    &	1	&	1	&	1	&	0	&	0	&	1	\\
        
        22	&	count\_non\_zeroes	& Colle & Num & Blinz   &	1	&	1	&	1	&	1	&	1	&	1	&	
        72	&	power	            & Colt & Num & Own      &	0	&	1	&	0	&	0	&	0	&	1	\\
        
        23	&	covariance	        & Colt & Num & Own      &	1	&	0	&	0	&	0	&	0	&	0	&	
        73	&	product	            & Colt & Num & Own      &	1	&	1	&	1	&	1	&	1	&	1	\\
        
        24	&	dec	                & Maho & Own & Own      &	0	&	0	&	0	&	0	&	0	&	0	&	
        74	&	quantile	        & Colt & Num & Own      &	1	&	1	&	0	&	0	&	1	&	1	\\
        
        25	&	dec\_array	        & Colle & Own & Own     &	1	&	1	&	0	&	0	&	0	&	1	&	
        75	&	reverse	            & Colle & Num & Own     &	1	&	1	&	0	&	0	&	0	&	1	\\
        
        26	&	Dist                & Math & Num & Own      &	0	&	1	&	0	&	1	&	1	&	1	&	
        76	&	safeNorm	        & Colle & Num & Blinz   & 	1	&	1	&	1	&	1	&	1	&	1	\\
        
        27	&	DistInf	            & Math & Num & Own      &	0	&	1	&	0	&	1	&	1	&	1	&	
        77	&	sampleKurtosis	    & Math & Num & Own      &	1	&	0	&	1	&	0	&	0	&	1	\\
        
        28	&	dot\_product	    & Colle & Num & Own     &	1	&	1	&	0	&	1	&	1	&	1	&	
        78	&	sampleSkew	        & Colt & Own & Own      &	1	&	0	&	1	&	0	&	0	&	0	\\
        
        29	&	durbinWatson	    & Colt & Own & Own      &	0	&	1	&	0	&	0	&	0	&	0	&	
        79	&	sampleVariance	    & Colt & Num & Own      &	1	&	1	&	1	&	0	&	0	&	1	\\
        
        30	&	ebeAdd	            & Math & Num & Own      &	1	&	1	&	0	&	0	&	0	&	1	&	
        80	&	sampleWeightedVar	& Colt & Num & Own      &	0	&	0	&	0	&	0	&	0	&	1	\\
        
        31	&	ebeDivide	        & Math & Own & Own      &	0	&	0	&	0	&	0	&	0	&	0	&	
        81	&	scale	            & Colt & Num & Own      &	1	&	1	&	0	&	0	&	0	&	1	\\
        
        32	&	ebeMultiply	        & Math & Num & Own      &	1	&	1	&	0	&	0	&	0	&	1	&	
        82	&	s\_add	            & Maho & Own & Own      &	1	&	0	&	0	&	1	&	1	&	0	\\
        
        33	&	ebeSubtract	        & Math & Num & Own      &	0	&	0	&	0	&	0	&	0	&	0	&	
        83	&	selection\_sort	    & Colle& Num & Own      &	1	&	1	&	1	&	0	&	0	&	1	\\
        
        34	&	elemtWise\_equal	& Colle& Num & Blinz    &	0	&	0	&	0	&	0	&	0	&	0	&	
        84	&	sequential\_search	& Colle& Num & Own      &	0	&	0	&	0	&	1	&	1	&	0	\\
        
        35	&	elemtWise\_max	    & Colle& Num & Blinz    &	1	&	1	&	0	&	0	&	0	&	1	&	
        85	&	set\_min\_val	    & Colle& Num & Own      &	1	&	1	&	0	&	0	&	0	&	1	\\
        
        36	&	elemtWise\_min	    & Colle& Num & Blinz    &	1	&	1	&	0	&	0	&	0	&	1	&	
        86	&	shell\_sort	        & Colle& Num & Own      &	1	&	1	&	1	&	0	&	0	&	1	\\
        
        37	&	elemtWise\_not\_eq  & Colle& Num & Blinz    &	0	&	0	&	0	&	0	&	0	&	0	&	
        87	&	skew	            & Colle& Num & Own      &	1	&	1	&	1	&	0	&	0	&	0	\\
        
        38	&	entropy	            & Math & Num & Own      &	1	&	1	&	1	&	1	&	1	&	0	&	
        88	&	square          	& Colle& Num & Blinz    &	1	&	1	&	0	&	0	&	0	&	1	\\
        
        39	&	equals	            & Math & Num & Blinz    &	0	&	0	&	0	&	0	&	0	&	0	&	
        89	&	standardize	        & Colle& Num & Own      &	1	&	1	&	0	&	0	&	0	&	0	\\
        
        40	&	errorRate           & Maho & Own & Own      &	0	&	0	&	0	&	0	&	0	&	0	&	
        90	&	sum	                & Maho & Own & Own      &	1	&	1	&	1	&	1	&	1	&	1	\\
        
        41	&	euc\_Dist   	    & Own  & Own & Own      &	0	&	1	&	0	&	1	&	1	&	1	&	
        91	&	sumOfLogarithms	    & Colle& Num & Own      &	1	&	1	&	1	&	1	&	1	&	1	\\
        
        42	&	evaluateHoners	    & Math & Own & Own      &	1	&	1	&	0	&	1	&	1	&	1	&	
        92	&	sum\_Power\_Deviat	& Colt & Num & Own      &	0	&	0	&	0	&	0	&	0	&	0	\\
        
        43	&	eval\_Internal	    & Math & Num & Own      &	0	&	0	&	0	&	0	&	0	&	0	&	
        93	&	sum\_labeled	    & Colt & Num & Own      &	0	&	0	&	0	&	0	&	0	&	0	\\
        
        44	&	evalNewton	        & Math & Num & Own      &	0	&	0	&	0	&	1	&	0	&	0	&	
        94	&	tanimotoDist	    & Maho & Own & Own      &	0	&	0	&	0	&	0	&	0	&	0	\\
        
        45	&	evalWeightedProd    & Math & Own & Own      &	1	&	1	&	0	&	1	&	1	&	1	&	
        95	&	variance	        & Colle& Num & Own      &	1	&	1	&	1	&	0	&	0	&	1	\\
        
        46	&	find\_diff	        & Colle& Num & Blinz    &	0	&	0	&	0	&	0	&	0	&	0	&	
        96	&	var\_Difference	    & Colt & Num & Own      &	1	&	1	&	0	&	0	&	0	&	1	\\
        
        47	&	find\_euc\_Dist	    & Colle& Num & Own      &	0	&	1	&	0	&	1	&	1	&	1	&	
        97	&	weightedMean	    & Colt & Num & Own      &	1	&	1	&	0	&	0	&	0	&	1	\\
        
        48	&	find\_magnitude	    & Colle& Num & Own      &	1	&	1	&	1	&	1	&	1	&	1	&	
        98	&	weightedRMS	        & Colt & Num & Own      &	0	&	0	&	0	&	0	&	0	&	0	\\
        
        49	&	find\_max	        & Colle& Num & Own      &	1	&	1	&	1	&	1	&	1	&	1	&	
        99	&	weighted\_average	& Colle& Num & Own      &	1	&	1	&	0	&	0	&	0	&	1	\\
        
        50	&	find\_max2	        & Colle& Own & Own      &	1	&	1	&	0	&	1	&	1	&	1	&	
        100	&	winsorizedMean	    & Colt & Own & Own      &	1	&	1	&	0	&	0	&	1	&	1	\\
        \bottomrule
        \multicolumn{22}{l}{\textbf{Colle:} \textit{Java Collection}, \textbf{Maho:} \textit{Apache Mahout}, \textbf{Math:} \textit{Apache  Commons Mathematics}, \textbf{Num:} \textit{NumPy}}
	\end{tabular}
    }
\end{table*}
