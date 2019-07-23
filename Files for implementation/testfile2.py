import pandas as pd

df = pd.read_csv("F:\Pycharm\Investment-Predictions\Datasets\Try.csv")
# print(df)
d = {'n': 0, 'y': 1, 'a': 2}
df = df.replace(d)
# print (df)

"""df = pd.read_csv("F:\Pycharm\Investment-Predictions\Datasets\Investment_Prediction(csv).csv")
print(df.shape)
for index, row in df.iterrows():
    # print(row[0], 'is a', row[1])
    pass

columns = list(df)
for column in columns:
    # print("true", df[column][1])
    print(df[column])"""


