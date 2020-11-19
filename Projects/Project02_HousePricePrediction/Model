import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import json

df = pd.read_csv('Bengaluru_House_Data.csv')
df01 = df.drop(['area_type','availability','balcony','society'],axis='columns')
df01['bhk'] = df01['size'].apply(lambda x: str(x).split(' ')[0])
df01.dropna()
df01.drop('size',axis='columns',inplace=True)

def convert_float(x):
    n = x.split('-')
    if len(n)==2:
        return (float(n[0])+float(n[1]))/2
    for m in n:
        try:
            return float(m)
        except:
            return None
df01['total_sqft'] = df01['total_sqft'].apply(convert_float)
df02 = df01[df01['total_sqft'].notnull()]
df03=df02.copy()
df03['price_sqft'] = df03['price']/df03['total_sqft']*1000000

df03['location'] = df03['location'].apply(lambda x: str(x).strip())
location_stat = df03['location'].value_counts(ascending=False)
loc_less_10 = location_stat[location_stat.values<=10]
df04 = df03.copy()
df04['location'] = df04['location'].apply(lambda x: 'others' if x in loc_less_10 else x)
df05 = df04[df04['bhk'] !='nan']
df05['bhk'] = df05['bhk'].apply(lambda x: float(x))
df06 = df05[(df05['total_sqft']/df05['bhk'])>300]


def remove_outlier(df):
    df_new = pd.DataFrame()
    for key, subdf in df.groupby('location'):
        mean = np.mean(subdf['price_sqft'])
        std = np.std(subdf['price_sqft'])
        new_subdf = subdf[(subdf['price_sqft']>(mean-std)) & (subdf['price_sqft']<(mean+std))]
        df_new = pd.concat([df_new,new_subdf],ignore_index=True)
    return df_new

df07 = remove_outlier(df06)
def remove_bhk_outliers(df):
    exclude_indices = np.array([])
    for location, location_df in df.groupby('location'): # divided into different locations
        bhk_stats = {}
        for bhk, bhk_df in location_df.groupby('bhk'): # for each location, divide into groups based on different bhk numbers
            bhk_stats[bhk] = {                       #create status dictionary for each bhk group, calculate mean 'price_sqft', std, count for each group.
                'mean': np.mean(bhk_df.price_sqft),
                'std': np.std(bhk_df.price_sqft),
                'count': bhk_df.shape[0]
            }
        for bhk, bhk_df in location_df.groupby('bhk'): # so far, for this particular location group, bhk_stats is completed
            stats = bhk_stats.get(bhk-1)      # for current bhk group, get (bhk-1)group's status data
            if stats and stats['count']>5:    # considering only cases where number of apartments (for given bhk) is greater than 5.if (bhk-1)group's status data exists and there are more than 5 records in (bhk-1)group
                exclude_indices = np.append(exclude_indices, bhk_df[bhk_df.price_sqft<(stats['mean'])].index.values) # remove records having 'price_sqft' less than (bhk-1) group mean
    return df.drop(exclude_indices,axis='index')
df08 = remove_bhk_outliers(df07)
df09 = df08[df08['bath']<=(df08['bhk']+2)]
df09.drop('price_sqft',axis='columns',inplace=True)
dummies = pd.get_dummies(df09['location'])
df10 = pd.concat([df09,dummies.drop('others',axis='columns')],axis='columns')
df10.drop('location',axis='columns',inplace=True)
model = linear_model.LinearRegression()
x = df10.drop('price',axis='columns')
y = df10['price']
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=10)
model.fit(X_train,y_train)

columns = {
    'data_columns':[col.lower() for col in x.columns]
    }
with open('columns.json','w') as f:
    f.write(json.dumps(columns))

def predict_price(location,sqft,bath,bhk):
    with open('columns.json','r') as f:
        column_list = json.load(f)['data_columns']
    loc_index = column_list.index(location)  # location index

    yx = np.zeros(len(column_list))
    yx[0] = sqft
    yx[1] = bath
    yx[2] = bhk
    if loc_index >= 0:
        yx[loc_index] = 1

    return model.predict([yx])[0]

