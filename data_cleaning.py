from data_analysis import df

c2 = df
# col1 = "UDI"
# c2.drop(columns = col1, inplace=True)

# col2 = "Product ID"
# c2.drop(columns = col2, inplace=True)

# col3 = "Failure Type"
# c2.drop(columns = col3, inplace=True)

c2.drop(['UDI','Product ID','Failure Type'], axis = 1, inplace = True)

column_rename = {'Target': 'Fail(Y/N)'}
c2 = c2.rename(columns = column_rename)                     
df = c2
