names = ["alex", "mike", "emma", "sophie"]
grades = [1, 7, 5]

if "mike" in names:
    index_mike = names.index("mike")
    grade_mike = grades[index_mike]
    print("Mike participated in the exam, and his grade is:", grade_mike)
else:
    print("Mike did not participate in the exam.")
