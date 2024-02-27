from data_cleaning import df
import pandas as pd

from sklearn import preprocessing

c4 = df

label_encoding = preprocessing.LabelEncoder()
c4['Type'] = label_encoding.fit_transform(c4['Type'])
c4['Type'].unique()

Target_0_count, Target_1_count = c4['Fail(Y/N)'].value_counts()
Target_1 = c4[c4['Fail(Y/N)'] == 1]
Target_0 = c4[c4['Fail(Y/N)'] == 0]
Target_1_over = Target_1.sample(Target_0_count,replace=True)
dataset_balanced = pd.concat([Target_1_over,Target_0], axis=0)
dataset_balanced['Fail(Y/N)'].groupby(dataset_balanced['Fail(Y/N)']).count()
data = dataset_balanced.copy()
data = data.reset_index(drop=True)
data.to_csv("predictive_mintenance_artifact.csv", index=False)
df = data
