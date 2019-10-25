import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('regression.csv')
X=data.iloc[:,0].values
y=data.iloc[:,1].values
theta=[0,0]

def computeCost(X,y):
    E=(1/2)*sum((theta[0]+X*theta[1]-y))**2
    return E
E=computeCost(X,y)

eta=0.01
diff=1

count=200
temp=[0,0]
a=[]
x=[0,1]
for i in range(199):
    x.append(x[-1]+1)
    
for iter in range(1,count+1,1):
    temp0=theta[0]-eta*sum((theta[0]+X*theta[1]-y))  
    temp1=theta[1]-eta*sum(((theta[0]+X*theta[1]-y)*X))

    theta[0]=temp0
    theta[1]=temp1
    E=computeCost(X,y)
    print(E)
    #a=np.array(E)
    
    
plt.plot(x,E,"-")

plt.show()
