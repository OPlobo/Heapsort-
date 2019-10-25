'''
import numpy as np
import matplotlib.pyplot as plt

x=[30,63,66,78,82,96,106,270]
y=[64,82,88,90,96,108,128,166]

a2=sum(x)/len(x)
b2=sum(y)/len(y)


if len(x)%2==0:
    
'''
'''
import pandas as pd

names=['sepal_length','sepal_width','petal_length','petal_width','class']
df=pd.read_csv('iris.data.txt',header=None,names=names)

df.head()

df.info()
df.describe()

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')
sns.lmplot("sepal_length","sepal_width",data=df,fit_reg=False,hue='class')
sns.lmplot("petal_length","petal_width",data=df,fit_reg=False,hue='class')
plt.show()

import numpy as np
from sklearn.model_selection import train_test_split

x=df.iloc[:,:-1].values
y=df.iloc[:,4].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state42)

from sklearn.neighbors import KNeighborClasifier

knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)
pred=knn.predict(x_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test,pred)
'''

from sklearn.model_selection import cross_val_score
neighbors=[x for x in range(1,50) if x%2!=0]
cv_score=[]

for k in neighbors:
    knn=KNeighborsClass
    scores=cross_val_score(knn,x_train,y_train,cv=10,scoring='accuracy')

