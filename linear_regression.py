import csv

# Read the study hours and marks from data.csv
hours = []
marks = []

with open("data.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        hours.append(float(row["Hours_Studied"]))
        marks.append(float(row["Marks"]))

# Calculate the linear regression slope and intercept
n = len(hours)
mean_hours = sum(hours) / n
mean_marks = sum(marks) / n

numerator = sum(
    (x - mean_hours) * (y - mean_marks)
    for x, y in zip(hours, marks)
)
denominator = sum((x - mean_hours) ** 2 for x in hours)

slope = numerator / denominator
intercept = mean_marks - slope * mean_hours

# Predict marks for 6.5 study hours
study_hours = 6.5
predicted_marks = slope * study_hours + intercept

print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")
print(f"Predicted marks for {study_hours} study hours: {predicted_marks:.2f}")
