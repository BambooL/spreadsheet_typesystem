# Type system for spreadsheet

## 1. Motivation
* Panko, R. (2016). What We Don't Know About Spreadsheet Errors Today: The Facts, Why We Don't Believe Them, and What We Need to Do. arXiv preprint arXiv:1602.02601.

### 1.1 Popular spreadsheet errors
* logical errors (45%): mathematical and domain knowledge
* mechanical errors (23%): pointing to wrong cell and typing errors
* omission errors (31%): leaving out a necessary component

### 1.2 Fact
* 14 laboratories spreadsheet development studies involving 967 individuals working alone on a variety of tasks. These numbers come from the Panko spreadsheet research website. The average across these studies is a cell error rate of 3.9%
* the probability of an error increases rapidly when there are many calculations that depend on precedent cells

## 2. Literature
* See bibtex file
* To be summarized (For each one, present the motivation, research question, method, evaluation and key contribution

## 3. Method description

## 4. Implementation
### 4.1 Parser
* http://ewbi.blogs.com/develops/popular/excelformulaparsing.html

### 4.2 Type System
* ``Basic``: Abraham, R., & Erwig, M. (2007). UCheck: A spreadsheet type checker for end users. Journal of Visual Languages & Computing, 18(1), 71-95.
* ``Advanced``: Abraham, R., & Erwig, M. (2006, July). Type inference for spreadsheets. In Proceedings of the 8th ACM SIGPLAN international conference on Principles and practice of declarative programming (pp. 73-84). ACM.

### 4.3 Spatial Analysis
* ``Basic``: Abraham, R., & Erwig, M. (2004, September). Header and unit inference for spreadsheets through spatial analyses. In Visual Languages and Human Centric Computing, 2004 IEEE Symposium on (pp. 165-172). IEEE.
* ``Advanced``: Chambers, C., & Erwig, M. (2009). Combining spatial and semantic label analysis.

### 4.4 Evaluation
* ``Spreadsheet Corpus``: http://openscience.us/repo/spreadsheet/euses.html

### 4.5 Possible improvements
* Encoding typing rules with operational semantics of more spreadsheet functions;
* Automatic fix errors by pbe (creating a fixing language and do syntactical heuristic search).