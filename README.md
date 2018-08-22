# Workforce Salary Prediction for HR
## Goal is to predict the salary of a new hire 

#### Handling and Preprocessing your dataset before analysis and visualization

1.	Reading the dataset (csv format)
2.	Spiltting the dataset into training and test set
based on a dataset providing us 
#### Description of dataset
The dataset provides us with level number corresponding to the employee position in a finance firm and the respective salary for that level.  

## Created models using Polynomial, SVR, Decision tree and Random Forest regression

![workforce_salary_polynomial_regression](https://user-images.githubusercontent.com/40129527/44492060-2dfd8d80-a631-11e8-9c79-f96c5e586f64.png)

![workforce_salary support vector machine](https://user-images.githubusercontent.com/40129527/44492082-381f8c00-a631-11e8-9e54-7a43db722dc6.png)

![workforce_salary decision_tree_regression](https://user-images.githubusercontent.com/40129527/44492085-4077c700-a631-11e8-9132-cb46b3088e34.png)

![workforce_salary random_forest_regression](https://user-images.githubusercontent.com/40129527/44492094-47063e80-a631-11e8-8f1f-3914a8179675.png)


#### Result - Model comparision(All prediction values are for employee position level 6.5)

Random Forest Salary Prediction value - $160,600.00

Decision Tree Prediction value - $150,000.00

SVR Prediction value - $170,370.02

Polynomial Prediction value - $158,862

Random forest and polynomial regression models provided best predictions. The salary value obtained from these 2 models was the closest to the test set data values. The 2 models were used predict salary for future employees by the HR department.
