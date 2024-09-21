import pandas as pd

def outlier_detect(df: pd.DataFrame) -> None:
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1*IQR
    upper = Q3 + 1*IQR
    print('Before data preprocess:')
    print('Skewness:\n', df.skew())
    print(df.describe())
    print('Median:\n', df.median())
    print('IQR:\n', IQR)
    print("Lower - Uppeer bound", lower,'-',upper)