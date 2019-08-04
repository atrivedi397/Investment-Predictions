# for working with csv files and dataframes
import pandas as pd

# this file has answer for binary classifiers
from sklearn import svm
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split

from Datasets.Dictionary import answers

from functions.variables import *


# function requires raw/original csv file and the list of columns to remove from the csv file
def csv_file_clean(csv_file, columns_to_remove, new_csv_file=None):
    df = pd.read_csv(csv_file)

    # filling not available values
    df.fillna(0, inplace=True)

    for column in columns_to_remove:
        df.drop(column, axis=1, inplace=True)
    print(df.shape)

    df.drop(df.index[[0]], inplace=True)
    df.to_csv(new_csv_file, index=False)
    return new_csv_file


# to replace the values by 0 and 1
# csv_file == the cleaned csv file for which the binary mapping has to be done
def class_representations(csv_file):
    munged_df = pd.read_csv(csv_file)
    columns = list(munged_df)
    response_list = []
    num = 0
    the_ultimate_response_list = []

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
    return munged_df, the_ultimate_response_list


# data details for printing
def print_data_details(the_ultimate_response_list):
    for i in range(25):
        print(the_ultimate_response_list[i])

    num = 1
    count_all_responses(the_ultimate_response_list)
    for dictionary in count_of_answers_given_by_person.values():
        print(f"person {num}: ", dictionary,
              f" total sum of zero and one = {dictionary['zeroes_count']+dictionary['ones_count']}")
        num += 1

    print(len(count_of_answers_given_by_person))


# count all the responses for all the persons
def count_all_responses(the_ultimate_response_list):
    for i in range(212):
        for container in the_ultimate_response_list:
            if container[i] == 0:
                count_of_answers_given_by_person[i]["zeroes_count"] += 1
            else:
                count_of_answers_given_by_person[i]["ones_count"] += 1
    return count_of_answers_given_by_person


def adding_target_to_munged_csv_file(munged_csv_df, classified_csv_file, count_of_answers_given_by_person):
    # 0 : these guys must invest
    # 1 : these guys should not invest

    predicted_outcome = []
    for dictionary in count_of_answers_given_by_person.values():
        if dictionary["ones_count"] >= 20:
            predicted_outcome.append(1)
        else:
            predicted_outcome.append(0)

    print(len(predicted_outcome), "\n", predicted_outcome)
    munged_csv_df["target"] = predicted_outcome
    munged_csv_df.to_csv(classified_csv_file, index=False)
    return predicted_outcome


def check_how_many_people_have_more_than_20_correct_answer(predicted_outcome):
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


def classifier_and_prediction(csv_file):
    classified_dataframe = pd.read_csv(csv_file)
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
