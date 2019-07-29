import pandas as pd
from Datasets.Dictionary import answers

df = pd.read_csv("F:\Pycharm\Investment-Predictions\Datasets\Investment_Prediction_munged.csv")
columns = list(df)

"""for column in range(len(columns)):
    print(columns[column])"""
col_index = 0
# print(columns[0])
list1 = []

for index, row in df.iterrows():
    a = row[col_index]
    list1.append(a)
print(list1)

print(answers[0])
# print([answers[0].get(n, n) for n in list1])
