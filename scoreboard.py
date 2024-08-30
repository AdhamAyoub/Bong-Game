from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 50, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()  # hide the arrow
        self.color("white")
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(x=-100, y=220)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(x=100, y=220)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
