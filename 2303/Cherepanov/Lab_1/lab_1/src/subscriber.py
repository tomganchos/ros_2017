#!/usr/bin/env python

import turtle
import rospy
from std_msgs.msg import String

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

    def go_up(self):
        new_x = self.xcor()
        new_y = self.ycor() + 24
        if (new_x, new_y) not in walls:
            self.goto(new_x, new_y)
            wn.update()
            rospy.loginfo('I heard Up')

    def go_down(self):
        new_x = self.xcor()
        new_y = self.ycor() - 24
        if (new_x, new_y) not in walls:
            self.goto(new_x, new_y)
            wn.update()
            rospy.loginfo('I heard Down')

    def go_left(self):
        new_x = self.xcor() - 24
        new_y = self.ycor()
        if (new_x, new_y) not in walls:
            self.goto(new_x, new_y)
            wn.update()
            rospy.loginfo('I heard Left')

    def go_right(self):
        new_x = self.xcor() + 24
        new_y = self.ycor()
        if (new_x, new_y) not in walls:
            self.goto(new_x, new_y)
            wn.update()
            rospy.loginfo('I heard Right')

level = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXXX         XXXXX",
"X  XXXXXXXX  XXXXX  XXXXX",
"X      XXXX  XXXXX  XXXXX",
"X        XX  XX        XX",
"XXXXXXX  XX  XX        XX",
"XXXXXXX  XX  XXXXX  XXXXX",
"XXXXXXX  XX    XXX  XXXXX",
"X   XXX        XXX  XXXXX",
"X   XXX  XXXXXXXXXXXXXXXX",
"X           XXXXXXXXXXXXX",
"X                  XXXXXX",
"XXXXXXXXXXXXXX     XXX  X",
"XXXXXXXXXXXXXXXX   XXX  X",
"XXX   XXXXXXXXXX        X",
"XXX                     X",
"XXX         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX   XXXXX              X",
"XX   XXXXXXXXXXXXXXX  XXX",
"XX      XXXXXXXXXXXX  XXX",
"XXXX         XXXXX      X",
"XXXXXXX                 X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

def setup_maze(level, pen, player, walls):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            if character == "P":
                player.goto(screen_x, screen_y)

def subscriber():
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("A Maze Game")
    wn.setup(700, 700)

    pen = Pen()
    player = Player()
    walls = []

    setup_maze(level, pen, player, walls)

    wn.tracer(0)

    def callback(data):
        rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
        if data.data == 'Left':
            player.go_left
        if data.data == 'Right':
            player.go_right
        if data.data == 'Up':
            player.go_up
        if data.data == 'Down':
            player.go_down
    #wn.update()

    #turtle.listen()
    #turtle.onkey(player.go_left, "Left")
    #turtle.onkey(player.go_right, "Right")
    #turtle.onkey(player.go_up, "Up")
    #turtle.onkey(player.go_down, "Down")
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('chatter', String, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()
