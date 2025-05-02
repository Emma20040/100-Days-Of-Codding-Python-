student_scores={
    "Hary":81,
    "Ron": 78,
    "Hermione":99,
    "draco":74,
    "Nevielle":62,
}

for scores in student_scores:
    if student_scores[scores]>80 and student_scores[scores]<91:
        student_scores[scores]= "good expectation"
    elif student_scores[scores]>90:
        student_scores[scores]= "outstanding"
    elif student_scores[scores]<80 and student_scores[scores]>70:
        student_scores[scores]= "Acceptable"
    else:
        student_scores[scores]= "fail"

print(student_scores)