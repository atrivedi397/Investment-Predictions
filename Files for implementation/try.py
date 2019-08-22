import pandas as pd
from Datasets.Dictionary import answers
from functions.data_cleaning_functions import *
""""
df = pd.read_csv("F:\Pycharm\Investment-Predictions\Datasets\Investment_Prediction_munged.csv")
columns = list(df)

for column in range(len(columns)):
    print(columns[column])
col_index = 0
# print(columns[0])
list1 = []

for index, row in df.iterrows():
    a = row[col_index]
    list1.append(a)
print(list1)

print(answers[0])
# print([answers[0].get(n, n) for n in list1])
"""


dataframe = pd.read_csv("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")
questions = list(dataframe)
questions.remove('target')
accuracy = []

i = 1
for question in questions:
    dataframe.drop(columns=question)
    x_test, y_test, clf, confusion_matrix, classification_report, accuracy_score \
        = classifier_and_prediction(classified_dataframe=dataframe)
    print(f"for question {question} : ", accuracy_score)
    # print("classification report : \n", classification_report)
    i += 1
    accuracy.append(accuracy_score)


print((sum(accuracy)/len(accuracy))*100)




