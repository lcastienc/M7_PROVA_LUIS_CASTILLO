import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Llistat.csv', usecols= ('NAME','NOTES')).dropna()
media = df.groupby(by='NAME').mean()

'''name = list(media.keys())
values = list(media.values())'''

plt.xlabel("ALUMNAT")
plt.ylabel("NOTES")
plt.legend("LUIS CASTILLO")
plt.bar(df.NAME, df.NOTES, color='blue', width=5)

plt.show()

