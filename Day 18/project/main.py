# using colorgram to extract 30 colors from the image in the folder
# import colorgram

# rgb_colors =[]
# colors = colorgram.extract('image.jpg', 30)
# print(colors)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as t
from turtle import Screen
import random


t.colormode(255)
tim= t.Turtle()
tim.speed(0)
color_list= [ (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

tim.hideturtle()
tim.penup()
tim.setheading(230)
tim.forward(275)
tim.setheading(0)
tim.penup()
 
number_0f_dots= 100
for i in range(1, number_0f_dots+ 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(35)
    
    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180) 
        tim.forward(350)
        tim.setheading(0)
screen = Screen()
screen.exitonclick()