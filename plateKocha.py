from turtle import Turtle, exitonclick

t = Turtle()
t.shape('turtle')

def platek(tura):
    # if tura == 4:
    #     return 0
    # else:
    #     platek(tura)
    for i in range(4):
        t.fd(60)
        t.lt(60)
        t.fd(60)
        t.rt(120)
        t.fd(60)
        t.lt(60)
        t.fd(60)
        t.rt(90)

maksymalna = int(input())
platek(maksymalna)

exitonclick()
