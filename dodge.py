import turtle
import random
import math
import time
import os


#screen setup
scr=turtle.Screen()
scr.title("Dodge!")
scr.setup(width=800,height=600)
scr.tracer(0)

game_directory = os.path.dirname(os.path.abspath(__file__))
bg_file = os.path.join(game_directory, "background1.gif")
player_file = os.path.join(game_directory, "player1.gif")

#images
scr.bgpic(bg_file)
scr.addshape(player_file)
fruits=[os.path.join(game_directory, "fruit1w.gif"),
    os.path.join(game_directory, "fruit2a.gif"),
    os.path.join(game_directory, "fruit3o.gif")]
for f in fruits:
    scr.addshape(f)


#variables
hearts=3
speed=35
gameover=False
wiggle=0

#player
player=turtle.Turtle()
player.shape(player_file)
player.penup()
playerbase=-220
player.goto(0,-230)

#fruit
fruit=turtle.Turtle()
fruit.speed(0)
fruit.shape(random.choice(fruits))
fruit.penup()
fruit.goto(random.randint(-250,250),300)

#lives display
lives=turtle.Turtle()
lives.color("darkgreen")
lives.penup()
lives.hideturtle()
lives.goto(-270,340)
lives.write(f"Lives: {hearts}", font=("Comic Sans MS",23,"bold"))

#player move
def left():
    if not gameover and player.xcor()>-360:
        player.setx(player.xcor()-35)
def right():
    if not gameover and player.xcor()<360:
        player.setx(player.xcor()+35)
def movefruit():
    fruit.goto(random.randint(-250,250),350)
    fruit.shape(random.choice(fruits))
def updatelives():
    lives.clear()
    lives.write(f"Lives: {hearts}", font=("Comic Sans MS",23,"bold"))
    
#binding
scr.listen()
scr.onkeypress(left,"Left")
scr.onkeypress(right,"Right")

#loop
while not gameover:
    scr.update()
    time.sleep(0.01)
    fruit.sety(fruit.ycor()-speed)
    
#jiggle
    wiggle+=0.4
    wiggleoffset=math.sin(wiggle)*4
    player.sety(playerbase+wiggleoffset)

#fruits keep falling
    if fruit.ycor()<-300:
        movefruit()
    
#did it hit?
    if fruit.distance(player)<70:
        hearts-=1
        updatelives()
        if hearts<=0:
            gameover=True
        else:
            movefruit()
lives.goto(0, 0)
lives.write("GAME OVER:(", align="center", font=("Comic Sans MS", 40, "bold"))
scr.update()

scr.mainloop()


