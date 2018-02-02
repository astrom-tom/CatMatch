# CatMatch

Cat Match is a very simple open source tool (GNU3.0) that matches 2 different catalogs with one common column. It is written in python3.6 and requires numpy and [tqdm](https://github.com/tqdm/tqdm) (installable via pip).

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

*`catmatch cat1 cat2 ID`*

Wich takes the generic form of `catmatch file1 file2 common_column_Header`

To make it work you have to follow few requirements:  
* Each columns in both catalogs must have a name at the very firts row of the file  
* The header line of the catalog (containing column names) must start with '#'  
* Obviously, the number of column names must match the number of columns
* The column you want to match must have the same name in both catalog
