import pandas as pd
import matplotlib.pyplot as plt


x_values = ["18-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "Prefer not to say"]
csv_obj = pd.read_csv("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction_classified_data1.csv")
original_csv = pd.read_csv("/home/atrivedi/Investment-Predictions/Datasets/Investment_Prediction(csv).csv")

# y_values = count of people in each age group belonging to class 0 and 1

original_age_group = list(original_csv["Age band you fall into?"])
original_age_group = original_age_group[1:]

age_group = list(csv_obj["Age band you fall into?"])
target_class = list(csv_obj["target"])

print(original_age_group)
print(age_group)
print(target_class)

count_of_each_age_group_target_class_0 = {"18-19": 0, "20-29": 0, "30-39": 0, "40-49": 0, "50-59": 0, "60-69": 0, "70-79": 0, "Prefer not to say": 0}
count_of_each_age_group_target_class_1 = {"18-19": 0, "20-29": 0, "30-39": 0, "40-49": 0, "50-59": 0, "60-69": 0, "70-79": 0, "Prefer not to say": 0}

for age, target in zip(original_age_group, target_class):
    if target == 0:
        count_of_each_age_group_target_class_0[age] += 1
    else:
        count_of_each_age_group_target_class_1[age] += 1


print(count_of_each_age_group_target_class_0, "\n", count_of_each_age_group_target_class_1)

y_values_target_0 = [4, 86, 74, 13, 1, 4, 1, 0]
y_values_target_1 = [0, 10, 18, 0, 1, 0, 0, 0]

"""
plt.title("Bar Graph")
plt.xlabel("Age Group ---> ")
plt.ylabel("persons for poor fin. management")
plt.bar(x_values, height=y_values_target_0, color="blue")
plt.bar(x_values, height=y_values_target_1, color="yellow")
"""

plt.title("Bar Graph")
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
ax[0, 1].bar(x_values, y_values_target_0, color="red")
ax[0, 1].set_title("age vs number of people with poor fin. mgmnt")
ax[0, 1].set_xlabel("Age Group ---> ")
ax[0, 1].set_ylabel("persons for poor fin. management")

ax[1, 0].bar(x_values, y_values_target_1, color="green")
ax[1, 0].set_title("age vs number of people with good fin. mgmnt")
ax[1, 0].set_xlabel("Age Group ---> ")
ax[1, 0].set_ylabel("persons for good fin. management")

plt.show()
