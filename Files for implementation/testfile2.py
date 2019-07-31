import pandas as pd
df = pd.read_csv("F:\Pycharm\Investment-Predictions\Datasets\Investment_Prediction_munged.csv")

print(df[df.isna().any(axis=1)])
print(df)
