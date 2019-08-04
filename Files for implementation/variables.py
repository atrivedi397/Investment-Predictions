"""Variable dataset declared for the counting of zeroes and ones in the answers"""

"""--- structure = {person1 : {count_zeroes : number1, count_ones : number2}, ......}"""
count_of_answers_given_by_person = {}

for i in range(0, 212):
    count_of_answers_given_by_person[i] = {"zeroes_count": 0, "ones_count": 0}


original_csv_file = "/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction(csv).csv"

# these are the columns / questions that are to be removed from the csv file.
# these are hence irrelevant questions
col_to_remove = ["Timestamp", "Please state your gender", "Does your household have a budget?",
                 "Who is responsible for day-to-day monetary decisions in your household?",
                 "Money is there to be spent", "If yes, how did you manage to make ends meet?",
                 "What is your view about saving money?"]