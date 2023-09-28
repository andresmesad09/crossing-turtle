from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.color("black")
        self.move_distance = MOVE_DISTANCE
        self.penup()
        self.reset_position()

    def move(self):
        new_y = self.ycor() + self.move_distance
        self.goto(x=self.xcor(), y=new_y)

    def reset_position(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
