import datetime
import turtle
from turtle import Screen, Turtle
import time
wn = Screen()
print("[+] created frame")
wn.title("Clock")
print('[+] win.colour("black") completed')
wn.bgcolor("black")
wn.setup(width=190, height=195)
print("[+] win move")
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
time.sleep(1)
pen.clear()
while True:
    currentDT = datetime.datetime.now()

    # output current time
    dayx = currentDT.day
    monthx = currentDT.month
    yearx = currentDT.year
    dayx = str(dayx)
    monthx = str(monthx)
    yearx = str(yearx)
    fulldate = dayx+"/"+monthx+"/"+yearx
    minutes = currentDT.minute
    hours = currentDT.hour
    seconds = currentDT.second
    minutes = str(minutes)
    hours = str(hours)
    seconds = str(seconds)
    fulltime = hours+":"+minutes+":"+seconds    

    pen = Turtle()
    pen.hideturtle()
    pen.pencolor("green")
    pen.penup()
    pen.speed(9)
    pen.goto(0 , -00)
    pen.write(fulltime, align="center", font=("Ink Free", 20, "normal"))
    time.sleep(0.001)
    pen.goto(-5 , -30)
    pen.write(fulldate , align="center", font=("Ink Free", 20, "normal"))
    time.sleep(1)
    pen.clear()
turtle.mainloop()   
