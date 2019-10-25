#1.1
import numpy as np
x=[0,1]
for i in range(18):
    x.append(x[-2]+x[-1])
print(x)


#1.2
import numpy as np
x=[0,1]
i=1
while i<19:
    i+=1
    x.append(x[i-1]+x[i-2])
print(x)

#1.3
x = 0
y = 1
print(x,end=',');print(y,end=',')
for i in range(3,21):
        z = x + y
        print(z,end=',')
        x = y
        y = z
.....................................................

#2
import numpy as np
import matplotlib.pyplot as plt

#%matplotlib inline

x=np.linspace(-5,5,100)
y=3*x**3-2*x**2+1
plt.plot(x,y,"-")

plt.title("y=3x^3-2x^2+1")

plt.xlabel("x")
plt.ylabel("y")
plt.show()
...................................................

#3
import numpy as np
import matplotlib.pyplot as plt

grades=np.array([75,89,82,71,70,58,65,92,46,50,48,58,83,75,70])
plt.hist(grades,bins=[40,60,80,100],edgecolor='black')

plt.xlabel("groups")
plt.ylabel("numbers of groups")
plt.show()
...................................................

#4
import numpy as np
import matplotlib.pyplot as plt

x=[300,400,500,500,800,1000,1000,1300]
y=[9500,10300,11000,12000,12400,13400,14500,15300]
labels=['A','B','C','D','E','F','G','H']

plt.scatter(x,y)

for label,x_count,y_count in zip(labels,x,y):
    plt.annotate(label,
    xy=(x_count,y_count),
    xytext=(5,3),
    textcoords='offset points')

plt.xlabel("outcomes of ad")
plt.ylabel("annual sales")
plt.show()




