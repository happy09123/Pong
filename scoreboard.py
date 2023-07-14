from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.goto(0, 225)
        self.scores = [0, 0]
        self.update_scoreboard("none")

    def update_scoreboard(self, index):
        if type(index) == int:
            self.clear()
            self.scores[index] += 1

        self.write(f"{self.scores[0]}     {self.scores[1]}", False, "center", ("Courier", 45, "normal"))
