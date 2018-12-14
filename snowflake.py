import turtle

twig_size = 100
flakes = 3
twig_amount = 3

def createArm(amount, iteration, twig_amount):
    if (iteration < 1):
        return
    turtle.left(360 / amount)
    turtle.fd(twig_size)
    createTwig(twig_amount)
    turtle.bk(twig_size * (twig_amount + 1))
    createArm(amount, iteration - 1, twig_amount)

def createTwig(amount):
    if (amount < 1):
        return
    turtle.fd(twig_size)
    turtle.bk(twig_size)
    turtle.left(45)
    turtle.fd(twig_size)
    turtle.bk(twig_size)
    turtle.right(90)
    turtle.fd(twig_size)
    turtle.bk(twig_size)
    turtle.left(45)
    turtle.fd(twig_size)
    createTwig(amount - 1)

turtle.pendown()
createArm(flakes, flakes, twig_amount)
turtle.Screen().exitonclick()
