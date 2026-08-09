import turtle
import random
import winsound
import time

class Window():
    def __init__(self,title,bgimg,bgcolor,x_size,y_size):
        self.screen=turtle.Screen()
        self.screen.title(title)
        self.screen.bgpic(bgimg)
        self.screen.bgcolor(bgcolor)
        self.screen.setup(x_size,y_size)
        
        self.screen.tracer(0)
        self.screen.addshape("strawberry.gif")

turtles_list=[]

class Turtle():
   
    def __init__(self,shape,color):
        self.turtle= turtle.Turtle()
        self.turtle.shape(shape)
        self.turtle.color(color)
        self.turtle.penup()
        turtles_list.append(self.turtle)
    
    #movement
    def go_right(self):
        self.turtle.setheading(0)
    def go_left(self):
        self.turtle.setheading(180)
    def go_up(self):
        self.turtle.setheading(90)
    def go_down(self):
        self.turtle.setheading(270)
        
    def direction(self, head, screen: turtle.Screen):
        screen.listen()
        if(head==0):
         
            screen.onkey(self.go_down,"Down")
            screen.onkey(self.go_up,"Up")
            screen.onkey(self.go_right,"Left")
            
        elif(head==90):
         
            screen.onkey(self.go_left,"Left")
            screen.onkey(self.go_right,"Right")
            screen.onkey(self.go_up,"Down")
        elif(head==180):
           
            screen.onkey(self.go_down,"Down")
            screen.onkey(self.go_up,"Up")
            screen.onkey(self.go_left,"Right")
        elif(head==270):
            
            screen.onkey(self.go_right,"Right")
            screen.onkey(self.go_left,"Left")
            screen.onkey(self.go_down,"Up")
    def gen_seg(self):
        new_seg=turtle.Turtle()
        new_seg.hideturtle()
        new_seg.shape("circle")
         
        new_seg.color("yellow")
        new_seg.penup()
        turtles_list.append(new_seg)

    def touch_boundary(self, x, y, score, number, screen):
        global game_running
        if x >= 293 or x <= -293 or y >= 293 or y <= -293:
            game_running = False  # stop loop

          
            score.goto(0, 0)
            score.color("yellow")
            score.write(f"Game Over\n   Score {number}", align="center", font=("Arial", 25, "bold"))
            winsound.Beep(600, 1000)
            
class Food():
    def __init__(self,shape):
        self.turtle=turtle.Turtle()
        
        self.turtle.shape(shape)
        self.turtle.penup()
        
    
    def gen_food(self):
  
   
        x=random.randrange(-289,289)
        y=random.randrange(-289,289)
    
        self.turtle.hideturtle()
        self.turtle.goto(x,y)
        self.turtle.showturtle()
        
number=0
eat_food=True
seg_gen=False
 
k=0
speed=3
screen=Window("Snake Game","bg.png","black",650,700)
tur=Turtle("square","yellow")
food=Food("strawberry.gif")
score=turtle.Turtle()
score.color("Light green")
score.hideturtle()
score.penup()
score.goto(0,310)
food_eat=0
distance=8

score.write(f"Score: {number}",move=False,align="center",font=("Arial",25,"bold"))


def show_score(number):
 
  
    score.clear()
    score.write(f"Score: {number}",move=False,align="center",font=("Arial",25,"bold"))


game_running=True
def game_loop():
    global eat_food, number, speed, k,game_running,food_eat,distance
    

    tur.turtle.forward(speed)
    tur.direction(tur.turtle.heading(), screen.screen)
    x, y = tur.turtle.position()
    tur.touch_boundary(x, y, score,number,screen)
 
    

    if eat_food:
        food.gen_food()
        tur.gen_seg()
        winsound.MessageBeep(winsound.MB_ICONASTERISK)
        speed += 0.5
        food_eat=food_eat+1
     
        eat_food = False

    if tur.turtle.distance(food.turtle) < 8:
        number+=10
        show_score(number)
        eat_food = True

    if k == 3:
        for idx in range(len(turtles_list) - 1, 0, -1):
            x = turtles_list[idx - 1].xcor()
            y = turtles_list[idx - 1].ycor()
            turtles_list[idx].goto(x, y)
            turtles_list[idx].showturtle()
        k = 0
    k += 1

    screen.screen.update()  
    screen.screen.ontimer(game_loop, 50) 
#   Detect collision with body
    for segment in turtles_list[2:]:
        if (tur.turtle.distance(segment)<distance):
          
            score.clear()
            score.goto(0, 0)
            score.color("yellow")
            score.write(f"Game Over\nScore {number}", align="center", font=("Arial", 25, "bold"))
            screen.screen.update()
            winsound.Beep(600,1000)
            time.sleep(1)
            turtle.bye()
    if food_eat ==5:
        distance+=1
        food_eat=0
    screen.screen.update()
    if game_running==False:
      
        time.sleep(1)
        turtle.bye()


game_loop()
 
turtle.done()
 
 

