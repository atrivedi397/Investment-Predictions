import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report


def logistic_classifier_and_prediction(csv_file=None, classified_dataframe=None):
    dataset, target_column = None, None
    try:
        if csv_file is not None:
            classified_dataframe = pd.read_csv(csv_file)
            dataset = classified_dataframe.iloc[:, :-1]
            target_column = classified_dataframe['target']
        elif classified_dataframe is not None:
            dataset = classified_dataframe.iloc[:, :-1]
            target_column = classified_dataframe['target']

    except csv_file is None and classified_dataframe is None:
        print("program will terminate as both arguments are empty")
        exit(0)

    x_train, x_test, y_train, y_test = train_test_split(dataset, target_column, shuffle=True, test_size=0.25)
    clf = linear_model.LogisticRegression()

    clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)

    return y_pred, y_train, classification_report(y_test, y_pred), confusion_matrix(y_test, y_pred), accuracy_score(
        y_test, y_pred)


def linear_classifier_and_prediction(csv_file=None, classified_dataframe=None):
    dataset, target_column = None, None
    try:
        if csv_file is not None:
            classified_dataframe = pd.read_csv(csv_file)
            dataset = classified_dataframe.iloc[:, :-1]
            target_column = classified_dataframe['target']
        elif classified_dataframe is not None:
            dataset = classified_dataframe.iloc[:, :-1]
            target_column = classified_dataframe['target']

    except csv_file is None and classified_dataframe is None:
        print("program will terminate as both arguments are empty")
        exit(0)

    x_train, x_test, y_train, y_test = train_test_split(dataset, target_column, shuffle=True, test_size=0.25)
    clf = linear_model.LinearRegression()

    clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)
    print("y_predicted : ", y_pred)

    new_y_pred = []
    for item in y_pred:
        new_y_pred.append(int(item))

    return new_y_pred, y_train, classification_report(y_test, new_y_pred), confusion_matrix(y_test,
                                                                                            new_y_pred), accuracy_score(
        y_test, new_y_pred)


def bayesian_classifier_and_prediction(csv_file=None, classified_dataframe=None):
    dataset, target_column = None, None
    try:
        if csv_file is not None:
            classified_dataframe = pd.read_csv(csv_file)
            dataset = classified_dataframe.iloc[:, :-1]
            target_column = classified_dataframe['target']
        elif classified_dataframe is not None:
            dataset = classified_dataframe.iloc[:, :-1]
            target_column = classified_dataframe['target']

    except csv_file is None and classified_dataframe is None:
        print("program will terminate as both arguments are empty")
        exit(0)

    x_train, x_test, y_train, y_test = train_test_split(dataset, target_column, shuffle=True, test_size=0.25)
    clf = linear_model.BayesianRidge(n_iter=350, compute_score=True)

    clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)

    print("y_predicted : ", y_pred)

    new_y_pred = []
    for item in y_pred:
        new_y_pred.append(int(item))

    return new_y_pred, y_train, classification_report(y_test, new_y_pred), confusion_matrix(y_test, new_y_pred), accuracy_score(y_test, new_y_pred)


_, _, class_report_log, confuse_log, accuracy_log = logistic_classifier_and_prediction(
     "/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")

_, _, class_report_linear, confuse_linear, accuracy_linear = linear_classifier_and_prediction(
     "/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")

_, _, class_report_bayes, confuse_bayes, accuracy_bayes = bayesian_classifier_and_prediction(
     "/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")


print(class_report_log, "\n", confuse_log, "\n", accuracy_log)
print(class_report_linear, "\n", confuse_linear, "\n", accuracy_linear)
print(class_report_bayes, "\n", confuse_bayes, "\n", accuracy_bayes)
