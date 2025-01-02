import pandas
student_dict = {
    'students': ['Emma', 'Xi', 'Mike'],
    'score': [60, 30, 40]
}

for (key, value) in student_dict.items():
    print(value)

student_dataframe= pandas.DataFrame(student_dict)
# print(student_dataframe)

# looping through the dataframe
for (key, value) in student_dataframe.items():
    print(value)

# looping through the rows of the data frame
for (index, row) in student_dataframe.iterrows():
    print(row.students)
