import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn import svm
from Datasets.Dictionary import answers

col_to_rem = ["Timestamp", "Please state your gender", "Does your household have a budget?",
              "Who is responsible for day-to-day monetary decisions in your household?",
              "Money is there to be spent"]

df = pd.read_csv("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_munged.csv")

y = df.iloc[:, 4]
X = df.drop(columns=["Marital Status",
                     "Suppose you put ₹10,000 into a <no fee> savings account with a guaranteed interest of 2% per year. You don't make any further payments into this account and you don't withdraw any money. How much would be in the account at the end of the first year, once the interest payment is made?"])

print("x - target class \n", X, type(X))
print("y - target class \n", y, type(y))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

print("\nX_train:\n")
print(X_train.head())
print(X_train.shape)

print("\nX_test:\n")
print(X_test.head())
print(X_test.shape)

clf = svm.SVC(kernel='linear')

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

"""
print(df.shape)

for column in col_to_rem:
    df.drop(column, axis=1, inplace=True)
print(df.shape)

df.drop(df.index[[0]], inplace=True)
print(df.shape)

df.to_csv("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_munged.csv", index=False)

print(answers[1])
df = df.replace(answers[0])
print(type(answers))
print(df.labels)"""