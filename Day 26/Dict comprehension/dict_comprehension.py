import random
names = ["Beth", 'John', "monica", "alexcia", "eleanor"]
students_scores ={student:random.randint(1,100) for student in names}
print(students_scores)
passed_students = {student:score for (student, score) in students_scores.items() if score >=50}
print(passed_students)