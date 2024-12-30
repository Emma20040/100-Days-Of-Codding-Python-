from turtle import Turtle

FONT = ("Courier", 15, "normal")
ALLIGMENT= "left"



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score =1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-290, 270)
        self.write(f" Level: {self.score}", align=ALLIGMENT, font=FONT)
        

    def point(self):
        self.score += 1
        self.update_scoreboard()
        
