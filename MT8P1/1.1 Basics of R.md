### Experiment 1: Part 1 Basics of R ###
## Basics of R ##
### Getting help ###
For any function, and documents, use ```?CommandName``` to get help with it. For example, ```?c``` or ```?'if'``` shows help for the respective basic functions.

### Types of Single Element Vectors ###
#### Atomic Vector of Type Character ####
```R 
print("abc");
```

#### Atomic Vector of Type Double ####
```R 
print(12.5)
```

#### Atomic Vector of Type Integer ####
```R 
print(63L)
```

#### Atomic Vector of Type Logical ####
```R 
print(FALSE)
print(TRUE)
```

#### Atomic Vector of Type Complex ####
```R 
print(2+3i)
```

### Creating a Vector ###
Arrays or vectors can be created as follows:
* ```R
  a = c(1,2,3,4)
  ```
* ```R
  a = 1:4
  ```
* ```R 
  a = seq(1,4,1)
  ```

All of them create the vector <code>[1 2 3 4]</code>. Changing the step (third parameter) in ```seq``` function helps us generate sequences with different step values.

### Vector Arithmetic ###
Adding/multiplying vectors with equal dimension are done componentwise as in mathematics. 
* ```R 
  c(1,2,3)+c(.5,.2,.2)
  ```
> \[1.5,2.2,3.2]
* ```R 
  2*c(1,2,3)
  ```
> \[2,4,6]

When it comes to vectors with unequal dimensions, the shorter vector is recursively used. For example,
* ```R 
  c(1,2,3)+c(.3, .2)
  ```
> \[1.3, 2.2, 3.3]
* ```R 
  c(1, 2, 3, 4)+ c(.3, .1)
  ```
> \[1.3, 2.1, 3.3, 4.1]


## Managing Datasets ##
### Inbuilt Sample Datasets ###
There are many inbuilt datasets in R. To see the list, run:
```R
  data()
```

To load the dataset, if it's not already pre-loaded, run 
```R
  d = data(DatasetName)
  ```

If your dataframe is a table, we can choose each row/column using
```R
  d$ColumnName
```

or 
```R
  d[ColumnNumber]
```

### Filtering Data ###
Say you're using ```trees``` dataset, and want to know the Girth of trees with Height less than 81. You can do it with:

```R
  show(trees$Girth[trees['Height'] < 80])
  ```

Suppose you want to filter the entire table, to give Girth, Height and Volume of trees with Girth < 18:

```R
  show(trees[trees$Girth<18,])
  ```

Alternatively, you can use:
```R
  subset(trees, Girth<18)
  ```
  
To achieve the same.

### Reading CSV Files ###
You can open a CSV file locally saved using ```read.csv``` and ```read.csv2``` functions. If the file is saved in the forlder /folder/filename.csv, then it can be loaded using

```R
  data = read.csv("/folder/filename.csv")
  ```
