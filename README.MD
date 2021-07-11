# easygplot
`easygplot` is a python package to visualize a csv file's data with few commands (i.e. 2 or 3 commands). It is convenient to understand data if different kind of graphs are plotted.

# Usage

To use easygplot in a project:

`import easygplot`

## Read csv file

Here is an example of loading a data from file. Check out the [read file using easygplot guide](https://github.com/gsharansingh/easygplot/blob/main/read_file.ipynb) for more imformation.

```
from easygplot import read
data_obj = read.CSV("gasprices.csv")
```

Additionally to get specific data, indexing can be used as

```
print(data_obj[:3])
```

Printing the object, will result in outputting the columns names

```
print(data_obj)
```

Whereas, printing the length will give the number of rows in the data

```
print(len(data_obj))
```

#### Features

1. Reading file with/without labels: Set 'True', if you want to set any column in the file as x-axis. Set 'False', if you want indexing of x-axis from 0 to length(rows).

```
data_obj = read.CSV("gasprices.csv", labels = False)
```

2. Reading a file with missing values: In the case, some values are missing in the file, then either replace the values or drop the row/column.

```
data_obj = read.CSV("gasprices.csv", missing_data_handling_strategy = 'drop_row')
```

**Stratergies for missing_data_handling_strategy**

|Type|Description|
|:-----|:-------|
|'mean'|it will replace missing value using mean along column.|
|'median'|it will replace missing value using median along column.|
|'most_frequent'|it will replace missing value using the most frequent value along column.|
|'constant'|it will replace missing value with fill_value.|
|'drop_row'|it will drop the whole row containing missing value.|
|'drop_column'|it will drop the whole column containing missing value.|

3. If you want x-axis' column index to be other than ${0^{th}}$ column, pass that column index. If you do not want any column index to be x-axis, pass 'None'.

```
data_obj = read.CSV("gasprices.csv", set_index = 3)
```

4. If some empty line(s) or description present in the beginning of the file, input the number of lines to discard the lines. 

```
data_obj = read.CSV("gasprices.csv", skip_lines = 2)
```

## Plot All Graphs

Here is an [example](https://github.com/gsharansingh/easygplot/blob/main/plot_all.ipynb) of plotting all graphs with `easygplot.read.CSV(...filename...)` object.

We can plot all the graphs with all indexes as following:

```
from easygplot import read
data_obj = read.CSV("gasprices.csv")
Plot.plot_all(data_obj[:])
```

We can use indexing to plot all graphs for specific index(es), like this:

`Plot.plot_all(data_obj[2])` for data at index = 2

`Plot.plot_all(data_obj[3:6])` for data at indexes = 3, 4, 5

