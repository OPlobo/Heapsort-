'''
import pandas as pd

df=pd.read_csv("data.csv")
df1=df.isnull()

from sklearn.preprocessing import Imputer
imr=Imputer(missing_values='NaN',strategy='mean',axis=0)
imr=imr.fit(df.values)
imputed_data=imr.transform(df.values)
imputed_data
'''
import pandas as pd
df = pd.DataFrame([['green','M',10.1,'class1'],['red','L',13.5,'class2'],
                   ['blue','XL',15.3,'class1']])
df.columns = ['color','size','price','classlabel']
size_mapping={'XL':3,'L':2,'M':1}
df['size']=df['size'].map(size_mapping)
