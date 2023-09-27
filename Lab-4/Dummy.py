import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('F:\ThirdSemesterMaterials\DSA-LAB\Lab-4\population_by_country_2020.csv' )
print(df.dtypes)
list1 = df['Country (or dependency)'].values.tolist()
fig, ax = plt.subplots()
list2 = df['Population (2020)'].values.tolist()
ax.bar(list1, list2,width = 1, color = ['red', 'green'])
plt.show()
