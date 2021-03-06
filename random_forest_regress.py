# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:27:05 2018

@author: ss960
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 18:13:36 2018

@author: ss960
"""

# Regression Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting the Random Forest Model to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 500, random_state = 0)
regressor.fit(X, y)


# Predicting a new result
y_pred = regressor.predict(6.5)

# Visualising the Regression results
#plt.scatter(X, y, color = 'red')
#plt.plot(X, regressor.predict(X), color = 'blue')
#plt.title('Workforce_Salary_Analysis (Decision Tree Regression)')
#plt.xlabel('Position level')
#plt.ylabel('Salary')
#plt.show()
#not exact representation for a decisiontree coz its non-linear and non-contigous decision model

# Visualising the Regression results(the x-axis needs to be divided into smaller intervals so that we more averages and a model that better represents the working of a decision tree) (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title(' Workforce_Salary_Analysis(Random Forest Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
