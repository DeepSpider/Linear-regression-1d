# imported matplotlib for plotting
import matplotlib.pyplot as plt

# importing custom libraries
import data_pre_processing
import linreg1d

# file containing synthetically generated data for linear regression 1d
file = 'data/data_1d.csv'

# storing the target array in Y and independent variable in X
X, Y = data_pre_processing.to_np_array(file)

# Calculating predicted target a.k.a Yhat
Yhat = linreg1d.solve(X, Y)

# plotting original data points vs line of best fit using linear regression
plt.scatter(X, Y)
plt.plot(X, Yhat)
plt.show()
