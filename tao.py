import turtle
tao=turtle.Pen()
tao.color('black','black')
tao.begin_fill()
tao.circle(100)
tao.end_fill()
tao.left(42)
tao.color('black','red')
tao.penup()
tao.begin_fill()
for i in range(2):
    
    tao.circle(137,90)
    tao.circle(137//38,90)

tao.end_fill()
tao.goto(85,50)
tao.left(65)
tao.color('black','red')

tao.begin_fill()
for i in range(2):
    
    tao.circle(137,90)
    tao.circle(137//38,90)

tao.end_fill()

tao.goto(88,140)
tao.left(58)

tao.begin_fill()
for i in range(2):
    
    tao.circle(137,90)
    tao.circle(137//38,90)

tao.end_fill()

tao.color('black')

tao.pendown()
for i in range(2):
    
    tao.circle(137,90)
    tao.circle(137//38,90)
tao.penup()
tao.goto(85,50)
tao.right(58)
tao.pendown()
for i in range(2):
    
    tao.circle(137,90)
    tao.circle(137//38,90)

tao.penup()
tao.goto(0,0)
tao.right(65)
tao.pendown()
for i in range(2):
    
    tao.circle(137,90)
    tao.circle(137//38,90)
    
tao.penup()
tao.goto(23,70)

tao.color('black','black')
tao.begin_fill()
tao.pendown()
tao.circle(30)
tao.end_fill()

tao.penup()
tao.goto(30,20)
