import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.model_selection import train_test_split
import numpy as np


df = pd.read_csv('salaries.csv')
inputs = df.iloc[:,:3]
target = df['salary_more_then_100k']

le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_job.fit_transform(inputs['job'])
inputs['degree_n'] = le_degree.fit_transform(inputs['degree'])

inputs_n = inputs.drop(['company','job','degree'],axis='columns')
model = tree.DecisionTreeClassifier()
X_train,X_test,y_train,y_test = train_test_split(inputs_n,target)
model.fit(X_train,y_train)


def predict_classification(x): # x=[[company,job,degree]] 2d array
    m = np.array(x).shape[0]  # row numbers
    for i in range(m):
        if x[i][0] == 'google':
            x[i][0] = 2
        elif x[i][0] == 'abc pharma':
            x[i][0] = 1
        else:
            x[i][0] = '0'

        if x[i][1] == 'sales executive':
            x[i][1] = 2
        elif x[i][1] == 'business manager':
            x[i][1]=0
        else:
            x[i][1]=1

        if x[i][2] == 'bachelors':
            x[i][2] = 0
        elif x[i][2] == 'masters':
            x[i][2] = 1
    predicted = model.predict(x)
    return predicted
