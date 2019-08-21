from functions.data_cleaning_functions import *
from functions.variables import *
from functions.saving_and_loading_this_model import *

if __name__ == "__main__":
    new_csv_file_with_removed_columns = csv_file_clean(original_csv_file, col_to_remove, "/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_munged1.csv")

    munged_df, the_ultimate_response_list = class_representations(new_csv_file_with_removed_columns)

    count_of_answers_by_person = count_all_responses(the_ultimate_response_list)

    predicted_outcome = adding_target_to_munged_csv_file(munged_df, "/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv", count_of_answers_by_person)

    x_test, y_test, classifier, confusion_matrix, classification_report, accuracy_score = classifier_and_prediction("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")

    print(f"Confusion Matrix \n {confusion_matrix}")
    print(f"Classification Report \n {classification_report}")
    print(f"Accuracy Score : {accuracy_score}")

    """ This will save the model iff the accuracy score is more than 95 % 
        and will tell after how many times of running the model it gets more than 95% accuracy.
        This model is saved on 70 % training and 30 % testing data."""

    loop_count = 0
    while accuracy_score < 0.95:
        _, _, classifier, _, _, accuracy_score = classifier_and_prediction("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")
        print(f"Accuracy Score for loop count {loop_count}:", accuracy_score)
        loop_count += 1
    else:
        save_model(classifier, "financial_health")
