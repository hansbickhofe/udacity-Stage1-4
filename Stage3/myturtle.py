import turtle

def draw_myturtle(kind,size,color,speed,turn):
    myform = turtle.Turtle()
    myform.color(color)
    myform.speed(speed)
    myform.shape("classic")
    myturn = 90 + turn
    
    if kind == "square":
        myform.right(myturn)
        for i in range (1,5):
            myform.forward(size)
            myform.right(90)
            
    elif kind == "triangle":
        for i in range (1,4):
            myform.forward(size)
            myform.right(120)
            
    elif kind == "circle":
        myform.circle(size)
        
    
window = turtle.Screen()
window.bgcolor("blue")            

for i in range(0,36):
    hans = draw_myturtle("square",200,"yellow",100,i*10)

window.exitonclick()

