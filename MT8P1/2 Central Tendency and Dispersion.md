### Experiment 2 ###
# Computation of Central Tendency and Dispersion #
## Measures of Central Tendency ##
### Mean ###
Arithmetic mean, or simply referred to as Mean for the data $X = (x_1,x_2,...,x_n)$ is given by 
 $$\bar{X} = \left({\sum_{i=1}^n x_i}\right)/{n}$$
 
If the data is a frequency table, $X = ((x_1,f_1),(x_2,f_2),...,(x_n,f_n))$, then 
$$\bar{X} = \left({\sum_{i=1}^n x_i\times f_i}\right)/{\sum_{i=1}^n f_i}$$

#### R Programming ####
Mean of a dataset ```X``` can be found using:
```R
  X = c(...)
  m = mean(X)
 ```
 
Alternatively, given how the vectors work in R, we can simply give the formula directly:
```R
  X = c(...)
  m = sum(X)/length(X)
  ```
  
Or if you have frequency data,
```R
  f = c(...)
  X = c(...)
  d = rep(X,f)
  m = mean(X)
  ```
  
Alternatively,
```R
  f = c(...)
  X = c(...)
  m = sum(X*f)/sum(f)
  ```