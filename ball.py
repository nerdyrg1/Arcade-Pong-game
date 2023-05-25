from turtle import Turtle


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1, outline=None)
        self.penup()
        self.x_step = 10
        self.y_step = 10
        self.move_speed = 0.1
        self.goto(position)

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x,new_y)

    def deflection_wall(self):
        self.y_step *= -1

    def deflection_paddle(self):
        self.x_step *= -1
        self.move_speed *= 0.9

    # def miss_paddle(self):
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.deflection_paddle()



