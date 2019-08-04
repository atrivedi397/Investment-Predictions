from functions.data_cleaning_functions import *
from functions.variables import *

new_csv_file_with_removed_columns = csv_file_clean(original_csv_file, col_to_remove, "/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_munged1.csv")

munged_df, the_ultimate_response_list = class_representations(new_csv_file_with_removed_columns)

count_of_answers_by_person = count_all_responses(the_ultimate_response_list)

predicted_outcome = adding_target_to_munged_csv_file(munged_df, "/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv", count_of_answers_by_person)

classifier_and_prediction("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")
