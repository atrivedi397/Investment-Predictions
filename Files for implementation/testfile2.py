import pandas as pd

df = pd.read_csv("/home/atrivedi/Investment-Predictions/Datasets/Try.csv")
# print(df)
d = [{'n': 0, 'y': 1, 'a': 2}]
df = df.replace(d)
# print (df)

df = pd.read_csv("F:\Pycharm\Investment-Predictions\Datasets\Investment_Prediction(csv).csv")
print(df.shape)
"""for index, row in df.iterrows():
    a = (row[1])  # prints the data second row or the values of the second column"""

columns = list(df)
print(columns)
"""for column in columns:
    print("true", df[column])"""

