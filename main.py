import turtle
# what is turtle? Official infos on the python turtle package https://docs.python.org/3/library/turtle.html

wn = turtle.Screen()  # wn == window
wn.title("PONG GAME") 
wn.bgcolor("black")  # wn background color
wn.setup(width=800, height=600)
wn.tracer(0)  # this one stops the wn to updating » we have to manually update it
# in our case makes the game run faster

# ___TO PLAY PONG WE NEED 4 ITEMS:
# ___PADDLE A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # speed of animation. NOT the speed of the actual paddle. (0) = max speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # change the size of the paddle
paddle_a.penup()
paddle_a.goto(-350, 0)  # xy coordinates where paddle A is located at the start of the game

# ___PADDLE B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ___BALL
ball = turtle.Turtle()
ball.speed(0)  # speed of animation. NOT the speed of the actual paddle. (0) = max speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# ___SCORE COUNTER
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player A: 0   ☃︎ ☃︎ ☃︎   Player B: 0", align="center", font=("Courier", 24, "normal"))

play_a = 0
play_b = 0


# ONCE CREATED THOSE OBJECTS, WE HAVE TO MAKE SURE THEY INTERACT BETWEEN THEM WITH FUNCTIONS
# to make things simpler and easier to understand for a first time developer we defined a fx per object

# ___PADDLE A
def paddle_a_up():
    y = paddle_a.ycor()  # to move the paddle I need to know the current coordinate.
    # y = paddle_a.ycor(). the y var stores the current y axis coordinates data
    y += 20  # to add 20px to the y var (unit of increment per single tap, when going up)
    paddle_a.sety(y)  # paddle_a , set y , to the new (y)


def paddle_a_down():
    y = paddle_a.ycor()  # to move the paddle I need to know the current coordinate.
    y -= 20  # to add 20px to the y var (unit of increment per single tap, when going down)
    paddle_a.sety(y)  # paddle_a , set y , to the new (y)


# ___PADDLE B
def paddle_b_up():
    y = paddle_b.ycor()

    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# ___PADDLE MOVEMENTS
wn.listen()  # this line tells the program to "listen" to keyboard input

wn.onkeypress(paddle_a_up, "w")  # when "w" call the function "paddle_a_up"
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_b_up, "Up")

# BALL MOVEMENTS
# we separate the ball movement between the x-axis movement and the y-axis movement
ball.dx = 0.2  # dx means "delta x" and defines the unit increment (2px) and thus the speed of the ball moving in the x axis
ball.dy = 0.2  # same as dx but for the y-axis

# every game needs a MAIN GAME LOOP
while True:
    wn.update()  # every time the loop run, it updates the screen

    ball.setx(ball.xcor() + ball.dx)  # move the ball
    ball.sety(ball.ycor() + ball.dy)

    # ___BORDERS TO MAKE THE BALL BOUNCE

    if ball.ycor() > 290:  # the background s 600px. 300 + 300
        # ball's size is 20 10+10.
        # THUS » the ball in centred at the 290th px
        ball.sety(290)  # i) set y coordinates at 290th px
        ball.dy *= -1  # ii) invert ball's direction » ball.dy = ball.dy * -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: # if ball goes beyond the playing field on the right side:
        ball.goto(0, 0)  # it goes back to starting point
        ball.dx *= -1
        play_a += 1. # == play_a = play_a + 1 -> player A scores one point
        score.clear()
        score.write("Player A: {}   ☃︎ ☃︎ ☃︎   Player B: {}".format(play_a, play_b), align="center",
                    font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        play_b += 1
        score.clear()
        score.write("Player A: {}   ☃︎ ☃︎ ☃︎   Player B: {}".format(play_a, play_b), align="center",
                    font=("Courier", 24, "normal"))

    # ___To make sure the ball bounces off the paddles,
    # we use the paddle's Y coordinates
    # chained comparison are written explicitly to simplify understanding of the logic
    if (ball.xcor() > 340 and ball.xcor() < 350) \
            and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        # if ball gets in front of the paddle ( 340 < x < 350 )
        # and the centre of the ball in in a ± 50px from the paddle centre

        ball.setx(340)  # makes sure the ball does not bounces on the inside
        ball.dx *= -1  # Inverts ball's direction on the X axis

    if ball.xcor() < -340 and ball.xcor() > -350 \
            and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
