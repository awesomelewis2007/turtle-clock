from turtle import Turtle, Screen
import datetime

# get the current time and convert to the hand's angles
wn = Screen()
print("[+] created frame")
wn.title("Clock")
print('[+] win.colour("black") completed')
wn.bgcolor("black")
wn.setup(width=200, height=180)
print("[+] win move")
currentDT = datetime.datetime.now()
pen = Turtle()
pen.pencolor("white")
pen.penup()
pen.goto(0 , -00)
pen.write("LOADING", align="center", font=("Courier", 20, "normal"))
pen.goto(-5 , -30)
pen.write("TIME", align="center", font=("Courier", 20, "normal"))
pen.goto(-5 , -50)
pen.write("FROM SERVER", align="center", font=("Courier", 15, "normal"))
pen.hideturtle()
# output current time
currentHour = currentDT.hour
if currentHour > 12:
    currentHour = currentHour - 12
currentMinute = currentDT.minute
if currentMinute < 10:
    print("Time logged in at - " + str(currentHour) + ":0" + str(currentMinute))
else:
    print("Time logged in at - " + str(currentHour) + ":" + str(currentMinute))
import time
time.sleep(1)
pen.clear()
# outside circle
circle = Turtle()
circle.penup()
circle.pencolor("green")
circle.speed(0)
circle.hideturtle()
circle.goto(0, 0)
circle.circle(10)
print("[+] frame circle")
# outside outside circle
circle = Turtle()
circle.penup()
circle.pencolor("green")
circle.speed(0)
circle.pensize(5)
circle.hideturtle()
circle.goto(0, -70)
circle.pendown()
circle.fillcolor("black")
circle.begin_fill()
circle.circle(70)
circle.end_fill()
print("[+] circle")
# hour hand
hourHand = Turtle()
hourHand.shape("arrow")
hourHand.color("green")
hourHand.speed(10)
hourHand.shapesize(stretch_wid=0.4, stretch_len=4)
print("[+] drawaing the hour hand")

# minute hand
minuteHand = Turtle()
minuteHand.shape("arrow")
minuteHand.color("green")
minuteHand.speed(10)
minuteHand.shapesize(stretch_wid=0.4, stretch_len=5)
print("[+] drawaing the minute hand")
# second hand
secondHand = Turtle()
secondHand.shape("arrow")
secondHand.color("white")
secondHand.speed(10)
secondHand.shapesize(stretch_wid=0.1, stretch_len=6)
print("[+] drawaing the second hand")
# inside circle
insideCircle = Turtle()
insideCircle.shape("circle")
insideCircle.color("black")
insideCircle.shapesize(stretch_wid=1.5, stretch_len=1.5)
print("[+] drawaing the inside frame")
pen = Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 30)
pen.write("12", align="center", font=("Courier", 20, "normal"))
pen.penup()
pen.hideturtle()
pen.goto(50, -15)
pen.write("3", align="center", font=("Courier", 20, "normal"))
pen.penup()
pen.hideturtle()
pen.goto(0, -60)
pen.write("6", align="center", font=("Courier", 20, "normal"))
pen.penup()
pen.hideturtle()
pen.goto(-50, -15)
pen.write("9", align="center", font=("Courier", 20, "normal"))
pen.penup()

# moving hour hand
def moveHourHand():
   currentHourInternal = datetime.datetime.now().hour
   degree = (currentHourInternal - 15) * -30
   currentMinuteInternal = datetime.datetime.now().minute
   degree = degree + -0.5 * currentMinuteInternal
   hourHand.setheading(degree)
   wn.ontimer(moveHourHand, 60000)



# moving minute hand
def moveMinuteHand():
    currentMinuteInternal = datetime.datetime.now().minute
    degree = (currentMinuteInternal - 15) * -6
    currentSecondInternal = datetime.datetime.now().second
    degree = degree + (-currentSecondInternal * 0.1)
    minuteHand.setheading(degree)
    wn.ontimer(moveMinuteHand, 1000)
    

# moving second hand
def moveSecondHand():
    currentSecondInternal = datetime.datetime.now().second
    degree = (currentSecondInternal - 15) * -5
    secondHand.setheading(degree)
    wn.ontimer(moveSecondHand, 1000)
    

# on timer infinite loop
wn.ontimer(moveHourHand, 1)
wn.ontimer(moveMinuteHand, 1)
wn.ontimer(moveSecondHand, 1)
print("""
        WELCOME TO THE CLOCK
=================================
        press enter to quit

""")
input()
print("[X] Closing turtle graphics")
if currentMinute < 10:
    print("Time logged out at - " + str(currentHour) + ":0" + str(currentMinute))
else:
    print("Time logged out at - " + str(currentHour) + ":" + str(currentMinute))