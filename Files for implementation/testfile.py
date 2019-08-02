import pandas as pd
from Datasets.Dictionary import answers

col_to_rem = ["Timestamp", "Please state your gender", "Does your household have a budget?",
              "Who is responsible for day-to-day monetary decisions in your household?",
              "Money is there to be spent"]

df = pd.read_csv("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction(csv).csv")
df.fillna(0, inplace=True)
print(df.shape)

for column in col_to_rem:
    df.drop(column, axis=1, inplace=True)
print(df.shape)

df.drop(df.index[[0]], inplace=True)
print(df.shape)

df.to_csv("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_munged.csv", index=False)
print("True")

print(answers[1])
df = df.replace(answers[0])
print(type(answers))
