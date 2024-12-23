# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('red')
# timmy.forward(-200)
# print(timmy)

# myscreen = Screen()
# print(myscreen.canvheight)
# myscreen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("programming L", ['python', 'js', 'java' ])
table.add_column("frameworks", ['django', 'express', 'springBoot'])
print(table)