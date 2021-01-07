import pandas as pd
import pickle
data=pd.read_csv('C:\\Users\\jubyj\\Desktop\\data science\\mushrooms.csv')
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
for i in range(len(data.columns)):
    data[data.columns[i]]=le.fit_transform(data[data.columns[i]])
y=data['class']
x=data.drop(['class','veil-type'],axis=1) 
from sklearn.model_selection import train_test_split   
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
from sklearn.ensemble import RandomForestClassifier
rfmodel=RandomForestClassifier()
rfmodel.fit(x_train,y_train)
y_pred=rfmodel.predict(x_test)
pickle.dump(rfmodel,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))
