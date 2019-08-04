from .data_cleaning_functions import *
from .variables import *

new_csv_file_with_removed_columns = csv_file_clean(original_csv_file, col_to_remove, "/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_munged1.csv")

munged_df, the_ultimate_response_list = class_representations(new_csv_file_with_removed_columns)


