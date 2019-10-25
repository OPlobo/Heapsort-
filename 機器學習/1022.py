from sklearn.datasets import load_diabetes

data=load_diabetes()
data.keys()

import pandas as pd
feature=pd.DataFrame(data['data'],columns=data['feature_names'])
target=pd.DataFrame(data['target'],columns=['target'])
df=pd.concat([feature,target],axis=1)

from sklearn.model_selection import train_test_split
X,y=load_diabetes().data,load_diabetes().target
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=8)

from sklearn.linear_model import Ridge
ridge=Ridge(alpha=1).fit(X_train,y_train)
#print(ridge.coef_)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

slr=LinearRegression()

slr.fit(X_train,y_train)
#print(slr.coef_)
y_train_pred=slr.predict(X_train)
y_test_pred=slr.predict(X_test)
#print('MSE train:%.3f, test: %.3f'% (mean_squared_error(y_train,y_train_pred),mean_squared_error(y_test,y_test_pred)))
print('R^2 train:%.3f, test: %.3f'% (r2_score(y_train,y_train_pred),r2_score(y_test,y_test_pred)))
'''
y_train_pred=ridge.predict(X_train)
y_test_pred=ridge.predict(X_test)
print('MSE train:%.3f, test: %.3f'% (mean_squared_error(y_train,y_train_pred),mean_squared_error(y_test,y_test_pred)))
print('R^2 train:%.3f, test: %.3f'% (r2_score(y_train,y_train_pred),r2_score(y_test,y_test_pred)))

from sklearn.linear_model import Lasso
lasso=Lasso(alpha=0.1).fit(X_train,y_train)
#print(lasso.coef_)
y_train_pred=lasso.predict(X_train)
y_test_pred=lasso.predict(X_test)
#print('MSE train:%.3f, test: %.3f'% (mean_squared_error(y_train,y_train_pred),mean_squared_error(y_test,y_test_pred)))
print('R^2 train:%.3f, test: %.3f'% (r2_score(y_train,y_train_pred),r2_score(y_test,y_test_pred)))
'''
from sklearn.linear_model import ElasticNet
elanet=ElasticNet(alpha=1,l1_ratio=0.5).fit(X_train,y_train)
#print(lasso.coef_)
y_train_pred=elanet.predict(X_train)
y_test_pred=elanet.predict(X_test)
#print('MSE train:%.3f, test: %.3f'% (mean_squared_error(y_train,y_train_pred),mean_squared_error(y_test,y_test_pred)))
print('R^2 train:%.3f, test: %.3f'% (r2_score(y_train,y_train_pred),r2_score(y_test,y_test_pred)))
