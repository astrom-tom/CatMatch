# CatMatch

[![DOI](https://zenodo.org/badge/120015982.svg)](https://zenodo.org/badge/latestdoi/120015982)

Cat Match is a very simple open source tool (GNU3.0) that matches 2 different catalogs with one common column. It is written in python3.6 and requires numpy and [tqdm](https://github.com/tqdm/tqdm), and [catscii](https://github.com/astrom-tom/catscii) (installable via pip).

You can install it on your python distribution with

`pip install catmatch`

Assuming you have two catalogs:  
Cat1:  

ID | Col1 | Col2 | Col3| ....
------------ | ------------- | --------- |  ------- |----
ID#1 | X1 |Y1|Z1|....
ID#2 | X2 |Y3|Z2|....
ID#3 | X3 |Y3|Z3|....
ID#4 | X4 |Y4|Z4|....
ID#5 | X5 |Y5|Z5|....


And Cat2:  

ID | ColA | ColB | ColC| ....
------------ | ------------- | --------- |  ------- |----
ID#1 | A1 |B1|C1|....
ID#2 | A2 |B3|C2|....
ID#3 | A3 |B3|C3|....
ID#4 | A4 |B4|C4|....
ID#5 | A5 |B5|C5|....

And you want to match them by there ID: You must do:

*`catmatch cat1 cat2 ID out.txt`*

Wich takes the generic form of `catmatch file1 file2 common_column_Header outputfile_name`

To make it work you have to follow few requirements:  
* Each columns in both catalogs must have a name at the very first row of the file  
* The header line of the catalog (containing column names) must start with '#'  
* Obviously, the number of column names must match the number of columns
* The column you want to match must have the same name in both catalog


The output of code is a **match.txt** file with the following format. Assuming you used the two catalogs above:

ID | Col1 | Col2 | Col3| ....|ID|ColA | ColB | ColC| ....
------------ | ------------- | --------- |  ------- |----|------------ | ------------- | --------- |  ------- |----
ID#1 | X1 |Y1|Z1|....|ID#1 | A1 |B2|C2|....
ID#2 | X2 |Y3|Z2|....|ID#2 | A2 |B2|C2|....
ID#3 | X3 |Y3|Z3|....|ID#3 | A3 |B3|C3|....
ID#4 | X4 |Y4|Z4|....|ID#4 | A4 |B4|C4|....
ID#5 | X5 |Y5|Z5|....|ID#5 | A5 |B5|C5|....


Citation
========

If you are willing to cite catmatch please use:

	@misc{catmatch, 
	  author    = {Thomas ,R},
	  title		 = {CatMatch v1.3, 10.5281/zenodo.2626564}, 
	  version   = {1.3},
	  publisher = {Zenodo},
	  month     = Apr,
	  year		= 2019,
	  doi		= {10.5281/zenodo.2626564},
	  url		= {https://doi.org/10.5281/zenodo.2626564}
	}
