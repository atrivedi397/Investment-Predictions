"""Variable dataset declared for the counting of zeroes and ones in the answers"""

"""--- structure = {person1 : {count_zeroes : number1, count_ones : number2}, ......}"""
count_of_answers_given_by_person = {}
# 212 = total number of persons that took the survey

for i in range(0, 212):
    count_of_answers_given_by_person[i] = {"zeroes_count": 0, "ones_count": 0}

# change the path of the original csv file according to your OS
original_csv_file = "/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction(csv).csv"

# these are the columns / questions that are to be removed from the csv file.
# these are hence irrelevant questions
col_to_remove = ["Timestamp", "Please state your gender", "Does your household have a budget?",
                 "Who is responsible for day-to-day monetary decisions in your household?",
                 "Money is there to be spent", "If yes, how did you manage to make ends meet?",
                 "What is your view about saving money?"]


columns_removed_for_literacy = ["Your highest education level?",
                                #"Who is responsible for day-to-day monetary decisions in your household?",
                                #"Does your household have a budget?",
                                "Which of the following statements best describe your pattern for choosing a financial product/service",
                                "Which source of financial information influences you the most?",
                                "In the past 12 months, have you been saving money in the following forms?",
                                "Your retirement is covered under which of the following?",
                                "Suppose you put ₹10,000 into a <no fee> savings account with a guaranteed interest of 2% per year. You don't make any further payments into this account and you don't withdraw any money. How much would be in the account at the end of the first year, once the interest payment is made?"]


columns_removed_for_income = ["Which bracket does your household income fall into?",
                              "Which form of \"more than one\" source of income you have?",
                              "Considering all the sources of income, is your household income regular and reliable?"]


columns_removed_for_behaviour = ["Before I buy something, I carefully consider whether I can afford it",
                                 "I tend to live for today and let tomorrow take care of itself",
                                 "I find it more satisfying to spend money than to save it for the long term",
                                 "I pay my bills on time",
                                 "I am prepared to risk some of my own money when saving or making an investment",
                                 "I keep a close personal watch on my financial affairs",
                                 "I set a long term financial goals and strive to achieve them",
                                 "Do you have any such habits?"]

"""
question_to_remove = "Income includes : 25,26,27" \
                     "Behaviour includes question number: 13,14,15,16,17,18,19,30" \
                     "Financial literacy includes : Question number 3,9, 10,11,12,23,28,31" \
"""                     ""
