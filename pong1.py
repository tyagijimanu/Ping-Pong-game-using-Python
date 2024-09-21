#Building PingPong game using Pygame

import turtle 
#it is a library used to create minimal graphics games

wn = turtle.Screen() 
#wn or win is used to create a window/background screen and we're using turtle module thats why writing "turtle.Screen"
# notice that S is capital in Screen

wn.title("Pong by tyaginayan") 
#window ko naam diya h

wn.bgcolor("black")
#background color of the window is set to black

wn.setup(width=700, height=500)
#window ka size set kiya h by using 'setup' keyword, unit is in pixels

wn.tracer(0) 
#you're essentially telling the turtle graphics to stop automatically updating the screen with every movement and drawing action

#Score
score_a = 0
score_b = 0
#yahan hamne initial score 0 define kr diya for both the players

# Paddle A

paddle_a = turtle.Turtle()
# 'turtle' for module name and 'Turtle' for class name and paddle_a is the object/instance of the class Turtle

paddle_a.penup()
#it is use to lift the pen off the drawing surface
#by default turtle ka pen down he hota h leaving trail behind where it is going toh "penup()" us pen ko drawing surface se lift kr deta h so that it won't leave trail of the path

paddle_a.speed(0)
#this is not the speed of the paddle it is the speed of the animation
#it sets the speed to the maximum possible speed

paddle_a.shape("square")
#it sets the shape of the paddle to square

paddle_a.color("white")
#it sets the color of the paddle to white

paddle_a.shapesize(stretch_wid=5, stretch_len=1)
#by default the paddle size is 20x20 pixels
#so we stretched it horizontally 5 times the default value so now it is 100pixels and length of the paddle utni he h

paddle_a.goto(-300, 0)
#it is the position of the paddle

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto(300,0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.speed(0)

# Ball
ball = turtle.Turtle()
ball.penup()
ball.goto(0,0)
ball.color("white")
ball.shape("circle")
ball.speed(0)
ball.dx = 0.25
#it is the change in the position of the ball i.e 1 pixel
ball.dy = -0.25

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write("Player A: 0 Player B: 0", align = "center", font = ("Cascadia Code", 18, "normal"))
#yahan hmne center mein Player A: 0 Player B: 0 likha h
# 0 dono ka initial score h jo baad mein ek se bdta jayega, neeche ek function banaya h ki how the score will increase

#Function (kis se kya krwana hai wo sab function m aata h)

# Function to update the score display
def update_score():#score k update kr dega
    pen.clear()#ye previous score k erase kr dega
    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Cascadia Code", 18, "normal"))
    #ye player A and player B k liye curly braces mein updated score likh dega 
    #{} this is where you want to insert the values of score_a and score_b
    #The .format(score_a, score_b) part is used to substitute these variables into the placeholders.

def paddle_a_up():
    #This line defines a function named "paddle_a_up()"
    #isme paddle ko define kr diya ki wo uper jayega
    y = paddle_a.ycor()
    #This line retrieves the current y-coordinate of the "paddle_a" object. In turtle graphics, the ycor() method returns the y-coordinate of the turtle's current position on the screen.
    y += 20
    #ye line paddle ko current coordinate se 20 pixels uper khiska dega
    paddle_a.sety(y)
    #ye line "paddle_a" object k liye naya y-coordinate set kr dega using set(y) method, this method will move the turtle to the specified y-coordinate while maintaing the current x-coordinate
    wn.update()
    #used to update the screen

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    wn.update()
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    wn.update()
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    wn.update()
    
wn.listen() #isse screen se input jayega
wn.onkeypress(paddle_a_up, "w") # w dabane par paddle_a 20pixels up ho jayega
wn.onkeypress(paddle_a_down, "s")# s dabane par pddle_a 20p down ho jayega
wn.onkeypress(paddle_b_up, "Up")# up arrow dabane par paddle_b 20pixels ho jayega
wn.onkeypress(paddle_b_down, "Down")#down arrow dabane par paddle_b 20pixels down ho jayegal

#Main game loop
while True:
    wn.update()
    #it simply updates the turtle window
    
    #Move the Ball
    
    ball.setx(ball.xcor() + ball.dx)
    #ye ball k naye coordinate mein dx add krke usko default bana dega
    ball.sety(ball.ycor() + ball.dy)
    
    #Border Checking
    
    if ball.ycor() > 240:
    #This line is a conditional statement. It checks whether the y-coordinate of the ball's current position (ball.ycor()) is less than -240.
        ball.sety(240)
        #if the above condition comes true then this line will set the y-coordinate of the ball to -240
        ball.dy *= -1
        #this line will reverse the velocity of the ball
        #If the ball was moving downward (positive dy), this line will change its direction to move upward (negative dy).
        
    if ball.ycor() < -240:
        ball.sety(-240)    
        ball.dy *= -1
        
    
    if ball.xcor() > 340:
        ball.setx(340)
        ball.dx *= -1
        score_a += 1
        #isme jaise he ball 340 k beyond jayegi player B ka score bad jayega
        pen.clear()
        #it will erase previous score and will write new score
        #agar ye nhi likhenge toh overwriting ho jayegi
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font = ("Cascadia Code", 18, "normal"))
        update_score()

        
    
    if ball.xcor() < -340:
        ball.setx(-340)   
        ball.dx *= -1
        score_b += 1
        #isme jaise he ball -340 se peeche jayegi toh player A ka score bad jayega
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font = ("Cascadia Code", 18, "normal"))
        #it will write the score for Player A and Player B such that if ball strikes at the wall behind paddle A then player B will get point and vice versa
        update_score()
    #Paddle and Ball collisions
    
    if (ball.xcor() > 290 and ball.xcor() < 300) and (ball.ycor() > paddle_b.ycor() - 50 and ball.ycor() < paddle_b.ycor() + 50):
         ball.setx(290)
         ball.dx *= -1
    #jab ball ka x-coordinate 290 se jyada hoga aur 300 se kam hoga aur ball ka y-coordinate paddle_b k y-coordinate + 50 se kam hoga aur ball ka y-coordinate paddle_b k y-coordinate - 50 se jayda hoga tab ball +290 se reflect ho jayegi     
    
    if (ball.xcor() < -290 and ball.xcor() > -300) and (ball.ycor() <  paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
         ball.setx(-290)
         ball.dx *= -1
    #jab ball ka x-coordinate -300 se jyada hoga aur -290 se kam hoga aur ball ka y-coordinate paddle_a k y-coordinate + 50 se kam hoga aur ball ka y-coordinate paddle_a k y-coordinate - 50 se jayda hoga tab ball -290 se reflect ho jayegi     