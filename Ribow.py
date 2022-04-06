
import turtle
from turtle import *
from random import randint
import math

#number of sides
n = 6
#lenght of the sizes
l = 9
s = math.sqrt(2)

turtle.screensize(canvwidth=10000, canvheight=10000,bg="white")
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Armadillo")
skk = turtle.Turtle()
skk.speed(0)
colormode(255)
skk.width(0)
skk.goto(-150, -150)

memo = {}
def fibonacci(n):
    if n in memo : 
        return memo[n]
    if n <= 2: 
        f = 1
    else: f =  fibonacci(n-3) + fibonacci(n-5)+ fibonacci(n-9) + fibonacci(n-7)
    memo[n] = f 
    return f

def star1(fibonacci):
    for i in range(n):
        skk.color(randint(0, 255),randint(0, 255),randint(0, 255))
        skk.forward(fibonacci(n*s))
        skk.left(fibonacci(n))		

def star2(fibonacci):          
    for i in range(l):
        skk.color(randint(0, 255),randint(0, 255),randint(0, 255))
        skk.forward(fibonacci(n*s))
        skk.right(fibonacci(l))	

while True: 
    star1(fibonacci)  , star2(fibonacci) 