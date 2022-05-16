import sys
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("101916056-output.csv")

print(df.head())
df.iloc[:, 1:].hist()
fig , ax = plt.subplots()
for i in df.columns[1:]:
    df[i].value_counts().sort_index().plot(ax=ax,kind='line')
plt.legend()
plt.savefig('101916056-pie.png')