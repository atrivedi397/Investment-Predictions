import pandas as pd
from sklearn import svm
# for plotting features
import seaborn as sns
import matplotlib.pyplot as plt
from Datasets.Dictionary import answers
from sklearn.metrics import confusion_matrix,classification_report, accuracy_score
from sklearn.model_selection import train_test_split

# these are the columns / questions that are to be removed from the csv file.
# these are hence irrelevant questions
col_to_remove = ["Timestamp", "Please state your gender", "Does your household have a budget?",
                 "Who is responsible for day-to-day monetary decisions in your household?",
                 "Money is there to be spent", "If yes, how did you manage to make ends meet?",
                 "What is your view about saving money?"]


df = pd.read_csv("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction(csv).csv")
# print(df.shape)

"""Variable dataset declared for the counting of zeroes and ones in the answers"""

"""--- structure = {person1 : {count_zeroes : number1, count_ones : number2}, ......}"""
count_of_answers_given_by_person = {}

for i in range(0, 212):
    count_of_answers_given_by_person[i] = {"zeroes_count": 0, "ones_count": 0}

print(count_of_answers_given_by_person)

the_ultimate_response_list = []
""""""

df.fillna(0, inplace=True)

for column in col_to_remove:
    df.drop(column, axis=1, inplace=True)
print(df.shape)

df.drop(df.index[[0]], inplace=True)
# print(df.shape)

df.to_csv("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_munged.csv", index=False)

munged_df = pd.read_csv("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_munged.csv")
# print(munged_df)
columns = list(munged_df)
print(columns)

response_list = []
num = 0

for questions in range(25):
    for index, row in munged_df.iterrows():
        a = row[questions]
        response_list.append(a)
    # print(questions)

    # print(response_list)
    """replacing the list of responses with 0 and 1 i.e. good classes or bad classes"""

    for value in response_list:
        if value in answers[num][0]:
            index = response_list.index(value)
            response_list[index] = 0

        elif value in answers[num][1]:
            index = response_list.index(value)
            response_list[index] = 1

    # some answers are having 1.0 (float as their values) .. why?
    # print(f"length {len(response_list)} : ques {questions} : ", response_list)
    the_ultimate_response_list.append(response_list)

    """for column in range(len(columns)):
        print(columns[column])
        df[columns[column]] = response_list"""

    print(response_list)
    # print(columns[questions])
    munged_df[columns[questions]] = response_list

    num += 1
    response_list = []
    ans_list = []


"""---------------------------------------------------------------------------------------------------------"""
for i in range(25):
    print(the_ultimate_response_list[i])


for i in range(212):
    for container in the_ultimate_response_list:
        if container[i] == 0:
            count_of_answers_given_by_person[i]["zeroes_count"] += 1
        else:
            count_of_answers_given_by_person[i]["ones_count"] += 1

num = 1
for dictionary in count_of_answers_given_by_person.values():
    print(f"person {num}: ", dictionary,
          f" total sum of zero and one = {dictionary['zeroes_count']+dictionary['ones_count']}")
    num += 1

print(len(count_of_answers_given_by_person))


# print(munged_df)

"""to find how many value are nan/NAN"""
# print(df[df.isna().any(axis=1)])


"""----------------------------------------------------------------------------------------------"""
# 0 : these guys must invest
# 1 : these guys should not invest

predicted_outcome = []
for dictionary in count_of_answers_given_by_person.values():
    if dictionary["ones_count"] >= 20:
        predicted_outcome.append(1)
    else:
        predicted_outcome.append(0)


print(len(predicted_outcome), "\n", predicted_outcome)

"""------------------- Checking the persons which have "ones" more than 20 """
new_temp_list = predicted_outcome[:]
for val in new_temp_list:
    if val == 1:
        print(new_temp_list.index(val))
        new_temp_list.remove(val)

num = 0
for val in count_of_answers_given_by_person.values():
    if val["ones_count"] >= 20:
        print(f"person {num} : ", val)
    else:
        num += 1

munged_df["target"] = predicted_outcome
munged_df.to_csv("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data.csv", index=False)


"""""""------------------------------------------------------------------------------------------------"""""""
classified_dataframe = pd.read_csv("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data.csv")
x = classified_dataframe.iloc[:, :-1]
y = classified_dataframe['target']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.8)

clf = svm.SVC(kernel='linear')

clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

# for model evaluation
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("Accuracy of the model : ", accuracy_score(y_pred=y_pred, y_true=y_test))



