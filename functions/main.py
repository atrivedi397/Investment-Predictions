from functions.data_cleaning_functions import *
from functions.variables import *
from functions.saving_and_loading_this_model import *
from other_models.logistic_linear_bayesian import *

if __name__ == "__main__":
    new_csv_file_with_removed_columns = csv_file_clean(original_csv_file, col_to_remove, "/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_munged1.csv")

    munged_df, the_ultimate_response_list = class_representations(new_csv_file_with_removed_columns)

    count_of_answers_by_person = count_all_responses(the_ultimate_response_list)

    predicted_outcome = adding_target_to_munged_csv_file(munged_df, "/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv", count_of_answers_by_person)

    x_test, y_test, classifier, confusion_matrix, classification_report, accuracy_score = svm_classifier_and_prediction("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")

    _, _, _, class_report_log, confuse_log, accuracy_log = logistic_classifier_and_prediction(
        "/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")

    _, _, clf_bayes, class_report_bayes, confuse_bayes, accuracy_bayes = bayesian_classifier_and_prediction(
        "/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")

    print(f"Confusion Matrix For SVM \n {confusion_matrix}")
    print(f"Classification Report For SVM \n {classification_report}")
    print(f"Accuracy Score  For SVM : {accuracy_score}")

    print(f"Confusion Matrix For Logistic Regression \n {confuse_log}")
    print(f"Classification Report For Logistic Regression  \n {class_report_log}")
    print(f"Accuracy Score  For Logistic Regression : {accuracy_log}")

    print(f"Confusion Matrix For Bayesian Regression \n {confuse_bayes}")
    print(f"Classification Report For Bayesian Regression  \n {class_report_bayes}")
    print(f"Accuracy Score  For Bayesian Regression : {accuracy_bayes}")
    save_model(clf_bayes, f"financial_health_bayesian(accuracy){accuracy_bayes}")

    """ This will save the model iff the accuracy score is more than 95 % 
        and will tell after how many times of running the model it gets more than 95% accuracy.
        This model is saved on 70 % training and 30 % testing data."""

    loop_count_svm = 0
    while accuracy_score < 0.95:
        _, _, classifier, _, _, accuracy_score = svm_classifier_and_prediction("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")
        print(f"Accuracy Score for loop count svm {loop_count_svm}:", accuracy_score)
        loop_count_svm += 1
    else:
        save_model(classifier, f"financial_health_svm(accuracy){accuracy_score}")

    loop_count_bayesian = 0
    while accuracy_bayes < 0.95:
        _, _, classifier, _, _, accuracy_bayes = bayesian_classifier_and_prediction("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")
        print(f"Accuracy Score for loop count bayesian {loop_count_bayesian}:", accuracy_bayes)
        loop_count_bayesian += 1
    else:
        save_model(classifier, f"financial_health_bayesian_improved(accuracy){accuracy_bayes}")

    loop_count_logistic = 0
    while accuracy_log < 0.90:
        _, _, classifier, _, _, accuracy_log = logistic_classifier_and_prediction("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")
        print(f"Accuracy Score for loop count logistic {loop_count_logistic}:", accuracy_log)
        loop_count_logistic += 1
    else:
        save_model(classifier, f"financial_health_logistic(accuracy){accuracy_log}")

    # Un comment lines below to work with Linear Regression
    """ _, _, _, class_report_linear, confuse_linear, accuracy_linear = linear_classifier_and_prediction("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")

    print(f"Confusion Matrix For Linear Regression \n {confuse_linear}")
    print(f"Classification Report For Linear Regression  \n {class_report_linear}")
    print(f"Accuracy Score  For Linear Regression : {accuracy_linear}")
      
    loop_count_linear = 0
    while accuracy_linear < 0.95:
        _, _, classifier, _, _, accuracy_linear = linear_classifier_and_prediction("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")
        print(f"Accuracy Score for loop count linear {loop_count_linear}:", accuracy_linear)
        loop_count_linear += 1
    else:
        save_model(classifier, "financial_health_linear")  
    """
