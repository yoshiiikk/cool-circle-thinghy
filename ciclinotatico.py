import turtle
import random as r

turtle.ht()
turtle.speed(100)

i = 1
endciclo = 1
ciclo = 0
colors = ["red","orange","yellow","green","blue","indigo","violet"]
radius = [350,300,250,200,150,100,50]

def fxn(x, y):
    global endciclo
    endciclo = 0

while endciclo:
    turtle.dot(radius[i], colors[i])
    turtle.onscreenclick(fxn)
    i +=1
    if i > len(colors)-1:
        colors.append(colors.pop(0))
        i = 0

turtle.clear()
for i in range(0,50,10):
    turtle.clear()
    turtle.write("67", align="center", font=("impact", i))
    
turtle.done()

#tung tung tung sahur saved my life S2