import pandas as pd

grades = [3, 7, 5, 8, 10, 6, 4, 9, 7, 2, 8]
students = ["James", "Charles", "Christina", "Joseph", "Rafael", "Agnes", "Martha", "Sophia", "Liam", "Olivia", "Noah"]
surnames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Hernandez", "Lopez"]

# Add one point to the final grade and combine names and surnames
adjusted_grades = []
full_names = []

for grade in grades:
    if grade < 10:
        grade += 1
    adjusted_grades.append(grade)

for name, surname in zip(students, surnames):
    full_name = name + " " + surname
    full_names.append(full_name)

# Create a DataFrame with the initial data
df = pd.DataFrame({
    'Full Name': full_names,
    'Grade': adjusted_grades
})

# Calculate the grade "with text format"
def grade_with_text(grade):
    if grade < 5:
        return 'Failed'
    elif 5 <= grade <= 6:
        return 'Passed'
    elif 6 < grade < 7:
        return 'Good'
    elif 7 <= grade < 9:
        return 'Very Good'
    elif 9 <= grade < 10:
        return 'Excellent'
    elif grade == 10:
        return 'Outstanding'

# Apply the function to obtain the grade "with text format"
df['Grade with Text'] = df['Grade'].apply(grade_with_text)

# Calculate the difference of the grade with respect to the group median
group_median = df['Grade'].median()
df['Difference from Median'] = df['Grade'] - group_median

# Calculate the difference of the grade in percentage with respect to the group median
df['Difference in Percentage from Median'] = ((df['Grade'] - group_median) / group_median) * 100

# Save the DataFrame to a CSV file
df.to_csv('student_grades.csv', index=False)

# Display the DataFrame
print(df)
