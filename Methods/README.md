The Methods-C ++, Methods-Java, and Methods-Python directories have the source code for 100 methods. The methods are the same in each directory, but they are written in a different programming language. Some of those methods are from our own implementation and others are from the following open source libraries:

- Colt Project (http://acs.lbl.gov/software/colt/): Open-source libraries written for high-performance scientific and technical computing in \textit{Java}.
    \item \textit{Apache Mahout\scriptsize{\footnote{\scriptsize{https://mahout.apache.org/}}}}: ML library written in \textit{Java}. 
    \item \textit{Apache Commons Mathematics\scriptsize{\scriptsize{\footnote{http://commons.apache.org/proper/commons-math/}}}:} Library of mathematics and statistics components written in the \textit{Java}.
    \item \textit{Java Collections\scriptsize{\footnote{https://docs.oracle.com/javase/Collection.html}}:} Framework that provides an architecture to store and manipulate the group of objects.
    \item \textit{NumPy\scriptsize{\scriptsize{\footnote{https://numpy.org/}}}:} Package for scientific computing in Python.
    \item \textit{Blinz++\scriptsize{\scriptsize{\footnote{https://github.com/blitzpp/blitzl}}}:} High-performance multidimensional array library for scientific computing written C++.
\end{itemize}


\Cref{tbl:dataset_with_MRs} details the methods used and specifies the library that they belong to or if is own implementation. Also, it specifies which MR satisfies each method. In \Cref{tbl:dataset_with_MRs}, we use the symbol \cmark~to denote a method that satisfies a given MR, and symbol \xmark~to denote a method that does not fulfil a particular MR. If the change in the output is as predicted after altering the original input, the method $m$ is said to fulfil (or satisfies) an MR.
