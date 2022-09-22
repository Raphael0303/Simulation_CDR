from tkinter import *
from tkinter import ttk
import math


WIDTH = 300
HEIGHT = 400
CANVAS_MID_X = WIDTH/2
CANVAS_MID_Y = HEIGHT/2
SIDE = WIDTH/4


WIDTH2 = 200
HEIGHT2 = 100
CANVAS_MID_X2 = WIDTH2/2
CANVAS_MID_Y2 = HEIGHT2/2
SIDE2 = WIDTH2/4
limiter=300

previous_x = previous_y = 0

def create_circle(x, y, r, color="black"): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill=color)

def myfunction(event):
    x, y = event.x, event.y
    x1 = (x+1)
    y1 = (y+1)
    canvas.create_point(x, y, x1, y1)
    sleep(0.5)
 
def Couleur():
    if (colors['bg']=="yellow"):
        colors.configure(bg="purple", fg="white")
    else:
        colors.configure(bg="yellow", fg="black")
    points_recorded.append(colors['bg'])
        

def tell_me_where_you_are(event):
    if (event.widget==canvas):
        previous_x = event.x
        pevious_y = event.y
        print(event.x, event.y)
    
def record_point(event):
    if (event.widget==canvas):
        points_recorded.append(event.x)
        points_recorded.append(event.y)
        create_circle(event.x, event.y, 5, color=colors['bg'])
        top.state(newstate='normal') 

    
def Bras():
    points_recorded.append('bras')
    
def Racque():
    points_recorded.append('racque')
    
def Statuette():
    points_recorded.append('statuette')
    
def Replique():
    points_recorded.append('replique')
    if (colors['bg']=="yellow"):
        create_circle(40,370 , 5, color="red")
    else:
        create_circle(570,370 , 5, color="red")
        
    
def Carre():
    points_recorded.append('carre')
    create_circle(133.5,380 , 5, color="blue")
    create_circle(170.5,380 , 5,color="blue")
    create_circle(170.5+37,380 , 5,color="blue")
    create_circle(170.5+2*37,380 , 5,color="blue")
    create_circle(170.5+3*37,380 , 5,color="blue")
    create_circle(170.5+4*37,380 , 5,color="blue")
    create_circle(170.5+5*37,380 , 5,color="blue")
    create_circle(170.5+6*37,380 , 5,color="blue")
    create_circle(170.5+7*37,380 , 5,color="blue")
    create_circle(170.5+8*37,380 , 5,color="blue")      
    
def Generer():
    points_recorded.append('statuette')
 
    


def rotate(points, angle, center):
    angle = math.radians(angle)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    cx, cy = center
    new_points = []
    for x_old, y_old in points:
        x_old -= cx
        y_old -= cy
        x_new = x_old * cos_val - y_old * sin_val
        y_new = x_old * sin_val + y_old * cos_val
        new_points.append([x_new + cx, y_new + cy])
    return new_points

def draw_square1(points, color="red"):
    fenetre.square1=canvas.create_polygon(points, fill=color)

def test():
    old_vertices = [[150, 150], [250, 150], [250, 250], [150, 250]]
    print ("vertices: ", vertices, "should be: ", old_vertices)
    print (vertices == old_vertices)

def rotation1(self):
    canvas.delete(fenetre.square1)
    fenetre.new_square1 = rotate(fenetre.new_square1, fenetre.angle, fenetre.center1)
    draw_square1(fenetre.new_square1)
    
def move_x(points, dist):
    py=points[2][0]-points[3][0]
    px=points[2][1]-points[3][1]
    new_points=[[points[0][0]+dist*py/math.sqrt(px**2+py**2),points[0][1]+dist*px/math.sqrt(px**2+py**2)],
                [points[1][0]+dist*py/math.sqrt(px**2+py**2),points[1][1]+dist*px/math.sqrt(px**2+py**2)],
                [points[2][0]+dist*py/math.sqrt(px**2+py**2),points[2][1]+dist*px/math.sqrt(px**2+py**2)],
                [points[3][0]+dist*py/math.sqrt(px**2+py**2),points[3][1]+dist*px/math.sqrt(px**2+py**2)]]
    print(new_points)
    return new_points


def move_y(points, dist):
    py=points[1][0]-points[2][0]
    px=points[1][1]-points[2][1]
    new_points=[[points[0][0]+dist*py/math.sqrt(px**2+py**2),points[0][1]+dist*px/math.sqrt(px**2+py**2)],
                [points[1][0]+dist*py/math.sqrt(px**2+py**2),points[1][1]+dist*px/math.sqrt(px**2+py**2)],
                [points[2][0]+dist*py/math.sqrt(px**2+py**2),points[2][1]+dist*px/math.sqrt(px**2+py**2)],
                [points[3][0]+dist*py/math.sqrt(px**2+py**2),points[3][1]+dist*px/math.sqrt(px**2+py**2)]]
    print(new_points)
    return new_points


def moving1_x(self):
    canvas.delete(fenetre.square1)
    fenetre.new_square1 = move_x(fenetre.new_square1, 1)
    fenetre.center1=[(fenetre.new_square1[1][0]+fenetre.new_square1[3][0])/2,(fenetre.new_square1[0][1]+fenetre.new_square1[2][1])/2]
    #print(fenetre.new_square)
    draw_square1(fenetre.new_square1)


    
def moving1_y(self):
    canvas.delete(fenetre.square1)
    fenetre.new_square1 = move_y(fenetre.new_square1, 1)
    fenetre.center1=[(fenetre.new_square1[1][0]+fenetre.new_square1[3][0])/2,(fenetre.new_square1[0][1]+fenetre.new_square1[2][1])/2]
    #print(fenetre.new_square)
    draw_square1(fenetre.new_square1)



def draw_square2(points, color="blue"):
    fenetre.square2=canvas.create_polygon(points, fill=color)


def rotation2(self):
    canvas.delete(fenetre.square2)
    fenetre.new_square2 = rotate(fenetre.new_square2, fenetre.angle, fenetre.center2)
    draw_square2(fenetre.new_square2)
    
    
    
def moving2_x(self):
    canvas.delete(fenetre.square2)
    fenetre.new_square2 = move_x(fenetre.new_square2, 1)
    fenetre.center2=[(fenetre.new_square2[1][0]+fenetre.new_square2[3][0])/2,(fenetre.new_square2[0][1]+fenetre.new_square2[2][1])/2]
    #print(fenetre.new_square)
    draw_square2(fenetre.new_square2)


    
def moving2_y(self):
    canvas.delete(fenetre.square2)
    fenetre.new_square2 = move_y(fenetre.new_square2, 1)
    fenetre.center2=[(fenetre.new_square2[1][0]+fenetre.new_square2[3][0])/2,(fenetre.new_square2[0][1]+fenetre.new_square2[2][1])/2]
    #print(fenetre.new_square)
    draw_square2(fenetre.new_square2)


   
  
    
def get_value():
   #e_text=entry.get()
   #Label(top, text=e_text, font= ('Century 15 bold')).pack(pady=20) 
   points_recorded.append(entry.get())
   top.state(newstate='iconic') 
# def processErreursPolaires(frome, too):
#     xerr=too[0]-frome[0]
#     yerr=too[1]-frome[1]
#     terr=too[2]-frome[2]
#     if( math.fabs(xerr) > limiter or math.fabs(yerr) > limiter/2.5 ):
#         if(math.fabs(xerr) > math.fabs(2*yerr)):
#             yerr = yerr * (limiter/math.fabs(xerr))
#             terr = terr * (limiter/math.fabs(xerr))
#             xerr = ((xerr > 0) - (xerr < 0))*limiter
#         else:
#             xerr = xerr * (limiter/2.5/abs(yerr))
#             terr = terr * (limiter/2.5/abs(yerr))
#             yerr = ((yerr > 0) - (yerr < 0))*limiter/2.5
#     if(micros() > TimerAcc + 4000000 )
#         AccPhaseDone = true;
#     else if( AccPhaseDone == false)
#         multiplier = (micros()-TimerAcc)/4000000.0;
    
#         xerr = xerr*multiplier;
#         yerr = yerr*multiplier;
#         terr = terr*multiplier;
    
#     resultat=[xerr, yerr, terr]
#     return (resultat)

# def processPIDRotation (frome, too):
    
    
fenetre = Tk()

fenetre.x = fenetre.y = 0
points_recorded = []
Mouvement_flag=0
fenetre.center=[0,0]
fenetre.new_square=[]


fenetre.geometry("1000x600")

photo = PhotoImage(master=fenetre, file="Table.png")
canvas = Canvas(fenetre,width=600, height=400)
canvas.create_image(0, 0,anchor=NW, image=photo)
canvas.pack(side=TOP, anchor=NW)


Button(fenetre, text ='Bras', command=Bras).place(x=650, y=40)
Button(fenetre, text ='Racque', command=Racque).place(x=650, y=80)
Button(fenetre, text ='Statuette', command=Statuette).place(x=650, y=120)
Button(fenetre, text ='Replique', command=Replique).place(x=650, y=160)
Button(fenetre, text ='Carre de fouille', command=Carre).place(x=650, y=200)
colors=Button(fenetre, text ='Couleur', command=Couleur, bg="yellow")
colors.place(x=300, y=500)


Button(fenetre, text ='Generer code', command=Generer).place(x=650, y=350)



top= Toplevel(fenetre)
top.geometry("750x250")
top.title("Child Window")
entry= ttk.Entry(top,font=('Century 12'),width=40)
entry.pack(pady= 30)
#Create a button to display the text of entry widget
button= ttk.Button(top, text="Enter", command= get_value)
button.pack()
   #Label(top, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)
top.state(newstate='iconic')  
# vertices1 = [
#                     [CANVAS_MID_X - SIDE/2, CANVAS_MID_Y - SIDE/2],
#                     [CANVAS_MID_X + SIDE/2, CANVAS_MID_Y - SIDE/2],
#                     [CANVAS_MID_X + SIDE/2, CANVAS_MID_Y + SIDE/2],
#                     [CANVAS_MID_X - SIDE/2, CANVAS_MID_Y + SIDE/2]]

# fenetre.angle=1
# fenetre.new_square1=vertices1
# fenetre.center1=[(fenetre.new_square1[1][0]+fenetre.new_square1[3][0])/2,(fenetre.new_square1[0][1]+fenetre.new_square1[2][1])/2]
# fenetre.new_square1 = rotate(fenetre.new_square1, fenetre.angle, fenetre.center1)
# draw_square1(fenetre.new_square1)



# vertices2 = [
#                     [CANVAS_MID_X2 - SIDE2/2, CANVAS_MID_Y2 - SIDE2/2],
#                     [CANVAS_MID_X2 + SIDE2/2, CANVAS_MID_Y2 - SIDE2/2],
#                     [CANVAS_MID_X2 + SIDE2/2, CANVAS_MID_Y2 + SIDE2/2],
#                     [CANVAS_MID_X2 - SIDE2/2, CANVAS_MID_Y2 + SIDE2/2]]


# fenetre.new_square2=vertices2
# fenetre.center2=[(fenetre.new_square2[1][0]+fenetre.new_square2[3][0])/2,(fenetre.new_square2[0][1]+fenetre.new_square2[2][1])/2]
# fenetre.new_square2 = rotate(fenetre.new_square2, fenetre.angle, fenetre.center2)
# draw_square2(fenetre.new_square2)


points_recorded.append(colors['bg'])  
fenetre.bind('<Motion>', tell_me_where_you_are)
fenetre.bind('<ButtonRelease-1>	', record_point)






# fenetre.bind('r', rotation1)
# fenetre.bind('<KeyPress-Right>', moving1_x)
# fenetre.bind('<KeyPress-Up>', moving1_y)

# fenetre.bind('a', rotation2)
# fenetre.bind('d', moving2_x)
# fenetre.bind('z', moving2_y)
  





fenetre.mainloop()
