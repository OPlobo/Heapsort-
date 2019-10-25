import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

iris=load_iris()

feature=pd.DataFrame(iris['data'],columns=iris['feature_names'])
target=pd.DataFrame(iris['target'],columns=['class'])

data=pd.concat([feature,target],axis=1)
df=data[data['class']!=2]

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
g=sns.FacetGrid(df,hue="class",height=5)
g.map(plt.scatter,"sepal length (cm)","sepal width (cm)")
g.add_legend()
#plt.show()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X=df.iloc[:,:2].values
y=df.iloc[:,4].values

sc=StandardScaler()
sc.fit(X)
X_std=sc.transform(X)

from sklearn.linear_model import LogisticRegression
from matplotlib.colors import ListedColormap

lr=LogisticRegression(C=100.0,random_state=1)
lr.fit(X_std,y)

print(lr.coef_)
print(lr.intercept_)

def plot_decision_regions(X,y,classifier,test_idx=None,resolution=0.02):
    markers=('s','x','o','^','v')
    colors=('red','blue','lightgreen','gray','cyan')
    cmap=ListedColormap(colors[:len(np.unique(y))])

    x1_min,x1_max=X[:,0].min()-1,X[:,0].max()+1
    x2_min,x2_max=X[:,1].min()-1,X[:,1].max()+1
    xx1,xx2=np.meshgrid(np.arange(x1_min,x1_max,resolution),
                        np.arange(x2_min,x2_max,resolution))
    Z=classifier.predict(np.array([xx1.ravel(),xx2.ravel()]).T)
    Z=Z.reshape(xx1.shape)
    plt.contourf(xx1,xx2,Z,alpha=0.3,cmap=cmap)
    plt.xlim(x1_min,x1_max)
    plt.ylim(x2_min,x2_max)

    for idx,cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl,0],
                    y=X[y==cl,1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=cl,
                    edgecolor='black')

    if test_idx:
        X_test,y_test=X[test_idx,:],y[test_idx,:]

        plt.scatter(X_test[:,0],
                    X_test[:,1],
                    c='',
                    edgecolor='black',
                    alpha=1.0,
                    linewidth=1,
                    marker='o',
                    s=100,
                    label='test set')

plot_decision_regions(X_std,y,classifier=lr)
plt.xlabel('sepal length [standarized]')
plt.xlabel('sepal width [standarized]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
        
