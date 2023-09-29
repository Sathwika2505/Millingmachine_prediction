from data_loading import df

c1 = df

columns = c1.columns
print(columns)

c1.head()
c1.tail()

print('Enter the number of columns: ', c1.shape[1])
print('Enter the number of rows: ', c1.shape[0])

print("total number of null vlaues form the data set --------", c1.isnull().sum())

print('total values in product id column : ', c1['Product ID'].value_counts())
print('total values in Type column : ', c1['Type'].value_counts())
print('total values in 	Air temperature [K] column : ', c1['Air temperature [K]'].value_counts())
print('total values in 	Process temperature [K] column : ', c1['Process temperature [K]'].value_counts())
print('total values in Rotational speed [rpm] column : ', c1['Rotational speed [rpm]'].value_counts())
print('total values in Torque [Nm] column : ', c1['Torque [Nm]'].value_counts())
print('total values in Tool wear [min] column : ', c1['Tool wear [min]'].value_counts())
print('total values in Target column : ', c1['Target'].value_counts())
print('total values in 	Failure Type column : ', c1['Failure Type'].value_counts())

for col in c1.columns:
  print(col, c1[col].nunique())

df = c1
