height= []
student_height= input("enter heights sepearted by a comma ").split(",")
# height=int(student_height)
# print(height)
sum_h=0
average_height=0
num_of_students=0
for h in range(0, len(student_height)):
    student_height[h]=int(student_height[h])

for h in student_height:
    sum_h= sum_h +h

for student in student_height:
    num_of_students += 1

average_height= sum_h/num_of_students
print(average_height)
    # print(sum(height))
