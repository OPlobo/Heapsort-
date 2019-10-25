from sklearn.datasets import load_diabetes

data=load_diabetes()
data.keys()

import pandas as pd
feature=pd.DataFrame(data['data'],columns=data['feature_names'])
target=pd.DataFrame(data['target'],columns=['target'])
df=pd.concat([feature,target],axis=1)

import matplotlib.pyplot as plt
import seaborn as sns

cols=['age','bmi','s1','s5','target']

sns.pairplot(df[cols])
plt.tight_layout()
plt.savefig('scatterplot.png',dpi=300)
plt.show()

import numpy as np
cm=np.corrcoef(df[cols].values.T)
hm=sns.heatmap(cm,
               cbar=True,
               annot=True,
               square=True,
               fmt='.2f',
               annot_kws={'size':15},
               yticklabels=cols,
               xticklabels=cols)
plt.tight_layout()
plt.savefig('correlation.png',dpi=300)
plt.plot(cm)
plt.show()

