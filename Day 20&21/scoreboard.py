from turtle import Turtle

ALLIGMENT= "center"
FONT= ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        with open('./Day 20&21/data.txt') as data:
            self.high_score =int(data.read())
        self.goto(0, 270)
        self.penup()
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALLIGMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!!", align=ALLIGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('./Day 20&21/data.txt', mode='w') as data:
                data.write(f"{self.high_score}")
        self.score =0
        self.update_scoreboard()
