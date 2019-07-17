# MeanShift
Implementation of Mean-shift outlier detection (MOD) [1].

# Pseudo-Code
## Algorithm 1: Mean-shift process
```
Data structures: 
-----------------
X     Input data, array of d n-dimensional vectors
Y     Output data, array of d n-dimensional vectors
k     the kNN parameter

Algorithm: 
-----------------
Step 1: Find its k-nearest neighbors kNN(x)
Step 2: Calculate the mean M of the neighbors kNN(x)
Step 3: Replace the point x by the mean M and save it to Y
```
## Algorithm 2: Mean-shift outlier detection (MOD)
```
Data structures: 
-----------------
X     Input data, array of d n-dimensional vectors
Y     Output data, array of d n-dimensional vectors
k     the kNN parameter

Algorithm: 
-----------------
Step 1: Repeat Algorithm 1 three times to get Y
Step 2: For every point x_i∈X and its shifted version y_i∈Y calculate distance D_i = |x_i-y_i|
Step 3: Calculate the standard deviation (SD) of all D_i
Step 4: For a point x_i∈X if D_i > SD, then x_i is detected as an outlier; save it to N
```
# References
[1] J.W.Yang，S. Rahardja, and P. Fränti, "Mean-shift outlier detection," Int. Conf. Fuzzy Systems and Data Mining (FSDM), Nov, 2018. http://cs.uef.fi/sipu/pub/FSDM2595.pdf
