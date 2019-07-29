import pandas as pd
from Datasets.Dictionary import answers

col_to_remove = ["Timestamp", "Please state your gender", "Does your household have a budget?",
                 "Who is responsible for day-to-day monetary decisions in your household?",
                 "Money is there to be spent", "If yes, how did you manage to make ends meet?",
                 "What is your view about saving money?"]

df = pd.read_csv("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction(csv).csv")
# print(df.shape)

df.fillna(0, inplace=True)
columns = list(df)

for column in col_to_remove:
    df.drop(column, axis=1, inplace=True)
print(df.shape)

df.drop(df.index[[0]], inplace=True)
# print(df.shape)

df.to_csv("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_munged.csv", index=False)

response_list = []
ans_list = []
num = 0

for questions in range(25):
    for index, row in df.iterrows():
        a = row[questions]
        response_list.append(a)
    # print(questions)
    ans_list.append(answers[questions])

    # print(response_list)
    # print(ans_list)
    """replacing the list of responses with 0 and 1 i.e. good classes or bad classes"""

    for value in response_list:
        if value in answers[num][0]:
            index = response_list.index(value)
            response_list[index] = 0

        elif value in answers[num][1]:
            index = response_list.index(value)
            response_list[index] = 1

    # some answers are having 1.0 (float as their values) .. why?
    print(f"length {len(response_list)} : ques {questions} : ", response_list)

    """for column in range(len(columns)):
        print(columns[column])
        df[columns[column]] = response_list"""

    num += 1
    response_list = []
    ans_list = []


"""to find how many value are nan/NAN"""
# print(df[df.isna().any(axis=1)])

# df.to_csv("F:\Pycharm\Investment-Predictions\Datasets\Investment_Prediction_classified_data.csv", index=False)
