"""Order of files to be run --

1. Run main.py in functions module
--> this will create 3 files namely:

    (a) Datasets/Investment_Prediction_classified_data1.csv
    (b) Datasets/Investment_Prediction_munged1.csv
    (c) functions/financial_health0.13.2.pkl

    1. Investment_Prediction_classified_data1.csv is the file which has the final details with "target" class added
    2. Investment_Prediction_munged1.csv can be removed after running the main.py
    3. Model is saved in financial_health0.13.2.pkl.

2.   Now run this "prediction_by_saved_model.py"

    (a). Now to test your saved model, copy the path of the following files
            (i) Datasets/Investment_Prediction_classified_data1.csv
            (ii) functions/financial_health0.13.2.pkl

         and paste them below as mentioned in line 29 and 35

"""

import joblib
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd
from sklearn.model_selection import train_test_split

# here provide the  path of "Datasets/Investment_Prediction_classified_data1.csv"
df = pd.read_csv("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")
x = df.iloc[:, :-1]
y = df['target']
_, x_test, _, y_test = train_test_split(x, y, test_size=0.99)

# here provide the path of "functions/financial_health0.13.2.pkl"
clf = joblib.load("/home/atrivedi/Investment-Predictions/functions/financial_health0.13.2.pkl")
print("x test: \n ", x_test)
y = clf.predict(x_test)
print(confusion_matrix(y_test, y))
print(accuracy_score(y_test, y))
print(classification_report(y_test, y))
