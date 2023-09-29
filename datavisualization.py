import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
import numpy as np
from feature_engineering import df  # Make sure to import the DataFrame from the correct source

# Create a copy of the DataFrame
copy_df3 = df.copy()

categ = []
numer = []
for col in copy_df3.columns:
    if copy_df3[col].dtypes == object:
        categ.append(col)
    else:
        numer.append(col)
plt.figure(figsize=(10,8))
sns.heatmap(copy_df3.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.show()


for x in numer:
        q75,q25 = np.percentile(copy_df3.loc[:,x],[75,25])
        intr_qr = q75-q25 
        max = q75+(1.5*intr_qr)
        min = q25-(1.5*intr_qr) 
        copy_df3.loc[copy_df3[x] < min,x] = np.nan
        copy_df3.loc[copy_df3[x] > max,x] = np.nan

# Box plots
for num in numer:
    plt.figure(figsize=(5, 5))
    sns.boxplot(data=copy_df3, x=num)
    plt.xlabel(num)
plt.show()

# Violin plots
for num in numer:
    plt.figure(figsize=(5, 5))
    sns.violinplot(data=copy_df3, x=num)
    plt.xlabel(num)
plt.show()
# print(df)
df = copy_df3
