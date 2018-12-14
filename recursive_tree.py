import turtle
turtle.speed(10);
turtle.tracer(0, 0)
# turtle.Screen().mainloop()
#
twig_size = 35
# flakes = 3
# twig_amount = 3
#
# def createArm(amount, iteration, twig_amount):
#     if (iteration < 1):
#         return
#     turtle.left(360 / amount)
#     turtle.fd(twig_size)
#     createTwig(twig_amount)
#     turtle.bk(twig_size * (twig_amount + 1))
#     createArm(amount, iteration - 1, twig_amount)
#
def createTwig(amount, size):
    if (amount < 1):
        return
    turtle.fd(size)
    turtle.bk(size)
    turtle.left(45)
    turtle.fd(size)
    turtle.bk(size)
    turtle.right(90)
    turtle.fd(size)
    turtle.bk(size)
    turtle.left(45)
    # turtle.fd(twig_size)
    # createTwig(amount - 1, size)

def createLeftRightBranches(size, branches):
    for i in range(1, branches):
        turtle.fd(size)
        turtle.left(20)
        createTwig(1, size)
        size = size / 1.25

    for i in range(1, branches):
        size = size * 1.25
        createTwig(1, size)
        turtle.right(20)
        turtle.bk(size)

    for i in range(1, branches):
        turtle.fd(size)
        turtle.right(20)
        createTwig(1, size)
        size = size / 1.25

    for i in range(1, branches):
        size = size * 1.25
        createTwig(1, size)
        turtle.left(20)
        turtle.bk(size)

def createBranch(size):
    for i in range(1, 5):
        turtle.fd(size * 3)
        createLeftRightBranches(size, 6)

    turtle.bk(size * 3 * 4)




turtle.pendown()
# createArm(flakes, flakes, twig_amount)
# createBranch(20)


for i in range(1,5):
    turtle.left(30)
    createBranch(20)

turtle.update()

turtle.Screen().exitonclick()
