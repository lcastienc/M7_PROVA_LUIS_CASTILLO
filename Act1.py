import pandas as pd
import matplotlib.pyplot as plt

def Act1():
    df = pd.read_csv('Llistat.csv', usecols=('NAME', 'NOTES')).dropna()
    media = df.groupby(by='NAME').mean()

    plt.xlabel("ALUMNAT")
    plt.ylabel("NOTES")
    plt.legend("LUIS CASTILLO")
    plt.bar(df.NAME, df.NOTES, color='blue')

    plt.show()

    return media


