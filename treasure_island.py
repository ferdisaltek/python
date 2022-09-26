from multiprocessing.connection import wait
from turtle import left, right


x=input("left or right").lower()
if x=="left":
    y=input("swim or wait").lower()
    if y=="wait":
        z=input("chose color")
        if z=="yellow":
            print("win")
        elif z=="red":
            print("game over")
        elif z=="blue":
            print("game over")
        else:
            print("gameover")
    else:
        print("game over")