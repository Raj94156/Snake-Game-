from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
f = open("highscore.txt",mode='r')
content = int(f.read())

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.HighScore = content
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore : {self.HighScore}", align=ALIGNMENT, font=FONT)

    def reset(self):

        if self.score > self.HighScore :
            self.HighScore = self.score
            f = open('highscore.txt',mode='w')
            f.write(f"{self.HighScore}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
