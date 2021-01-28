# importing numpy for converting python list to numpy array which is more efficient
import numpy as np


# reading the CSV file (format X, Y) where X is the independent variable and Y is the target variable
def to_np_array(csv_file):
    X = []
    Y = []
    # reading the file line by line, could have used pandas which will be more efficient if the file is large
    # however used std python for simplicity
    for line in open(csv_file):
        x, y = line.split(",")
        X.append(float(x))
        Y.append(float(y))
    # converting the python lists to numpy arrays
    X = np.array(X)
    Y = np.array(Y)
    return X, Y
