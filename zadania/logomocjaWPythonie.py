import turtle

t = turtle.Turtle()

# t.forward(100)
# # t.fd(100)
# t.left(90)
# t.lt(80)
# t.fd(100)
# t.rt(80)
# t.back(100)
# t.bk(100)
# t.rt(90)
# t.up()
# t.fd(100)
# t.down()
# t.fd(100)
# t.color("red")
# # t.color() #I w systemie szesnastkowym
# # t.begin_fill() #Wypełnienie figury
# # t.end_fill() #Wypełnienie figury, musi być zamknięta
# t.circle(100)

# Zad 1
# for i in range(4):
#     t.fd(150)
#     t.rt(90)
# Zad 2
# parametr = 100 #int(input())
# def funkcja(a):
#     for i in range(4):
#         t.fd(a)
#         t.rt(90)
# funkcja(300)

# Zad 3
# def funkcja(a):
#     for i in range(3):
#         t.fd(a)
#         t.rt(120)
# funkcja(300)

# Zad 4
# def kwadrat(a):
#     for i in range(4):
#         t.fd(a)
#         t.rt(90)
# kwadrat(100)
# t.up()
# t.lt(90)
# t.fd(100)
# t.down()
# kwadrat(100)
# t.up()
# t.lt(90)
# t.fd(100)
# t.down()
# kwadrat(100)
# t.up()
# t.lt(90)
# t.fd(100)
# t.down()
# kwadrat(100)

# Zad 5
x = int(input())
def kwadrat(a):
    for i in range(a):
        if i//4:
            t.lt(90)
            t.up()
            t.fd(300)
            t.down()
            for i in range(4):
                t.fd(100)
                t.rt(90)
        else:
            for i in range(4):
                t.fd(100)
                t.rt(90)
            t.up()
            t.lt(90)
            t.fd(100)
            t.down()
kwadrat(x)



turtle.done()