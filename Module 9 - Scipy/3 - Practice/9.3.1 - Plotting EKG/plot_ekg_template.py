
import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = 'C:\Users\asian\Downloads\ENGR265-spring2023\data\ekg\mitdb_100.csv'

# load data in matrix from CSV file; skip first two rows

### Your code here ###
opener = np.loadtxt(path,delimiter=',',skiprows=2)

# save each vector as own variable
### Your code here ###
time = opener

# use matplot lib to generate a single

### Your code here ###
