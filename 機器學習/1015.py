import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('regression1.csv')
X=data.iloc[:,0].values
y=data.iloc[:,-1].values

from sklearn.preprocessing import StandardScaler

sc_x=StandardScaler()
X1=X.reshape(-1,1)
X_std=sc_x.fit_transform(X1)

from sklearn.linear_model import LinearRegression

lr=LinearRegression()
lr.fit(X_std,y)
y_pred=lr.predict(X_std)
print('Slope:%.3f'% lr.coef_[0])
print('Intercept:%.3f'% lr.intercept_)

import sklearn.metrics as sm
print('MSE:%.3f'% sm.mean_squared_error(y,y_pred))
print('R^2:%.3f'% sm.r2_score(y,y_pred))

from sklearn.preprocessing import PolynomialFeatures

pr=LinearRegression()
quadratic=PolynomialFeatures(degree=2)
X_quad=quadratic.fit_transform(X_std)

pr.fit(X_quad,y)
y_quad_pred=pr.predict(X_quad)
print('theta1:%.3f'% pr.coef_[1])
print('theta2:%.3f'% pr.coef_[2])
print('Intercept:%.3f'% pr.intercept_)

import sklearn.metrics as sm
print('MSE:%.3f'% sm.mean_squared_error(y,y_quad_pred))
print('R^2:%.3f'% sm.r2_score(y,y_quad_pred))

x=np.linspace(-3,3,100)
plt.plot(X_std,y,'o')
plt.plot(x,lr.intercept_+lr.coef_[0]*x)
plt.plot(x,pr.intercept_+pr.coef_[1]*x+pr.coef_[2]*x**2)
plt.show()
