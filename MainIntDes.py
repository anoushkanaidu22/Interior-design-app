from cmu_112_graphics import *
from clientClass import *
from furnitureClass import *
import random
import math

#change background color function
def drawBG(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.bgColor[0])

#calculates distance between two points
def distance(app,x0,y0,x1,y1):
    app.distance=math.sqrt((x0-x1)**2+(y0-y1)**2)

#update the budget as user buys furniture
def changeBudget(app):
    for key in app.allAbove:
        if key.budgState==True:
            app.budget=app.budget-key.price
            key.budgState=False
    if app.budget<0:
        app.budgetCheck=True
        app.mode="scoreMode"

#checks collisions within the same splashscreen
def checkCollision(app,obj1,obj2):
    if obj1.collided(obj2):
        obj1.cx=obj1.ogPos[0]
        obj1.cy=obj1.ogPos[1]

#checks collisions between different splashscreens
def checkCollisionDif(app,obj1,obj2):

    if obj1.collided(obj2):
        app.mode=obj1.mode
        obj1.cx=obj1.ogPos[0]
        obj1.cy=obj1.ogPos[1]
        del app.allAbove[obj1]
        app.mode=obj2.mode

##########################################
# startMode
##########################################
#The first screen of the game
def startMode_redrawAll(app,canvas):
    font="Cochin 20 bold"
    canvas.create_rectangle(0,0,app.width,app.height, fill="deep sky blue",\
        outline="deep sky blue")
    canvas.create_rectangle(10,10,app.width-10,app.height-10, outline="white",\
        width=5)
    canvas.create_rectangle(20,20,app.width-20,app.height-20,outline="white",\
        width=5)
    canvas.create_text(app.width/2,120,text="Interior Design",fill="white",font="Copperplate 80 bold")
    canvas.create_text(app.width/2,200,text="Challenge",fill="white",font="Copperplate 70")
    canvas.create_text(app.width/2,250,text="Anoushka Naidu",fill="white",font="Copperplate 20 bold")
    canvas.create_text(app.width/2, app.height/2-50,\
        text="Welcome to Interior Design Challenge!",font=font,fill="white")
    canvas.create_text(app.width/2, app.height/2-30, \
        text="Press the button below to read the direcions",font=font,fill="white")
    canvas.create_text(app.width/2, app.height/2-10, \
        text="and begin your design process!", font=font,fill="white")
    canvas.create_image(app.width/2, app.height/2+80, \
        image=ImageTk.PhotoImage(app.scaledStartModeImage))
    canvas.create_rectangle(app.width/2-150,app.height/2+200,app.width/2+150,\
        app.height/2+250,fill="white",outline="white")
    canvas.create_rectangle(app.width/2-145,app.height/2+205,app.width/2+145,\
        app.height/2+245,fill="deep sky blue",outline="deep sky blue")
    canvas.create_rectangle(app.width/2-140,app.height/2+210,app.width/2+140,\
        app.height/2+240,fill="white",outline="white",activefill="AntiqueWhite2")
    canvas.create_text(app.width/2,app.height/2+225,text="Directions", \
        fill="deep sky blue",font="Cochin 15 bold")

def startMode_mousePressed(app,event):
    if event.x<=app.width/2+150 and event.x>=app.width/2-150 and \
    event.y>=app.height/2+205 and event.y<=app.height/2+245:
        app.mode='directionsMode'

##########################################
# directionsMode
##########################################
#directions for how to play
def directionsMode_redrawAll(app,canvas):
    font="Optima 20"
    canvas.create_rectangle(0,0,app.width,app.height,fill="navy",outline="navy")
    canvas.create_rectangle(10,10,app.width-10,app.height-10, outline="wheat2",\
        width=5) 
    canvas.create_rectangle(20,20,app.width-20,app.height-20,outline="wheat2",\
        width=5)
    canvas.create_text(app.width/2,100,text="DIRECTIONS",fill="wheat2",font="Optima 90 bold")
    canvas.create_text(app.width/2,200,text="You will be assigned a client who will assign you a theme for their room.",fill="wheat2",font=font)
    canvas.create_text(app.width/2,250,text="Keeping their preferences in mind, select furniture by dragging them from",fill="wheat2",font=font)
    canvas.create_text(app.width/2,300,text="the options bar and dropping it into the room.",fill="wheat2",font=font)
    canvas.create_text(app.width/2,350,text="Make sure you are in the right category to move things.",fill="wheat2",font=font)
    canvas.create_text(app.width/2,400,text="When you purchase furniture, or drop into the room, all sales are final,",fill="wheat2",font=font)
    canvas.create_text(app.width/2,450,text="and pieces cannot be returned even if you place them in the options bar.",fill="wheat2",font=font)
    canvas.create_text(app.width/2,500,text="You will be scored on how well your room captures your client's requests.",fill="wheat2",font=font)
    canvas.create_text(app.width/2,550,text="Click the button below to meet your client!",fill="wheat2",font="Optima 20 bold")
    canvas.create_line(app.width/2-250,575,app.width/2+250,575,fill="wheat2",width=3)
    canvas.create_rectangle(app.width/2-150,app.height/2+200,app.width/2+150,\
        app.height/2+250,fill="wheat2",outline="wheat2")
    canvas.create_rectangle(app.width/2-145,app.height/2+205,app.width/2+145,\
        app.height/2+245,fill="navy",outline="navy")
    canvas.create_rectangle(app.width/2-140,app.height/2+210,app.width/2+140,\
        app.height/2+240,fill="wheat2",outline="wheat2",activefill="wheat3")
    canvas.create_text(app.width/2,app.height/2+225,text="Meet Client", \
        fill="navy",font="Optima 15 bold")

def directionsMode_mousePressed(app,event):
    if event.x>=app.width/2-150 and event.x<=app.width/2+150 and \
    event.y>=app.height/2-270 and event.y<=app.height/2-220:
        app.hintButton=True
    if event.x<=app.width/2+150 and event.x>=app.width/2-150 and \
    event.y>=app.height/2+24 and event.y<=app.height/2+290:
        app.mode='clientMode'

##########################################
# clientMode
##########################################
#presents the chosen client and defines the theme

def clientMode_redrawAll(app,canvas):
    font="Courier 17"
    canvas.create_rectangle(0,0,app.width,app.height, fill=app.client.getScreenColor(),outline=app.client.getScreenColor())
    canvas.create_rectangle(10,10,app.width-10,app.height-10, outline="white", width=5)
    canvas.create_rectangle(20,20,app.width-20,app.height-20,outline="white",width=5)
    canvas.create_text(app.width/2, app.height/2-320,text=app.client.getInfo(),\
        font="Courier 17",fill='white')
    canvas.create_image(app.width/2,app.height/2+80,\
        image=ImageTk.PhotoImage(app.scaledClientImage))
    canvas.create_rectangle(app.width/2-150,app.height/2+250,app.width/2+150,\
        app.height/2+300,fill="white",outline="white")
    canvas.create_rectangle(app.width/2-145,app.height/2+255,app.width/2+145,\
        app.height/2+295,fill=app.client.getScreenColor(),\
            outline=app.client.getScreenColor())
    canvas.create_rectangle(app.width/2-140,app.height/2+260,app.width/2+140,\
        app.height/2+290,fill="white",outline="white",activefill="AntiqueWhite2")
    canvas.create_text(app.width/2,app.height/2+275,text="Begin Designing", \
        fill=app.client.getScreenColor(),font=font)
    canvas.create_rectangle(app.width/2-150,app.height/2-270,app.width/2+150,\
        app.height/2-220,fill="white",outline="white")
    canvas.create_rectangle(app.width/2-145,app.height/2-265,app.width/2+145,\
        app.height/2-225,fill=app.client.getScreenColor(),outline=app.client.getScreenColor())
    canvas.create_rectangle(app.width/2-140,app.height/2-260,app.width/2+140,\
        app.height/2-230,fill="white",outline="white",activefill="AntiqueWhite2")
    canvas.create_text(app.width/2,app.height/2-245, text="Definition+Hint",fill=app.client.getScreenColor(),font=font)
    if app.hintButton==True:
        canvas.create_text(app.width/2,app.height/2-180,text=themes[app.client.getTheme()],fill="white", font=font)

def clientMode_mousePressed(app,event):
    if event.x>=app.width/2-150 and event.x<=app.width/2+150 and \
    event.y>=app.height/2-270 and event.y<=app.height/2-220:
        app.hintButton=True
    if event.x<=app.width/2+150 and event.x>=app.width/2-150 and \
    event.y>=app.height/2+24 and event.y<=app.height/2+290:
        app.mode='optionsMode'

##########################################
# optionsMode
##########################################
#the main viewing screen for the room the user creates

def optionsMode_drawBudget(app,canvas):
    canvas.create_text(app.width-app.width/10,app.height/12,\
        text=f'Budget: ${app.budget}',fill="black",font="Arial 15 bold")

def optionsMode_redrawAll(app,canvas):
    drawBG(app,canvas)
    drawButton(canvas, (15,10,105,50))
    canvas.create_rectangle(0,0,app.width,app.height-120,outline="black")
    optionsMode_drawBudget(app,canvas)
    canvas.create_rectangle(3,app.height-120,279,app.height,outline="black",fill="white",activefill="AntiqueWhite2",width=5)
    canvas.create_text(138,app.height-60,text="Couches",fill="black", font="Arial 15")
    canvas.create_rectangle(279,app.height-120,558,app.height,outline="black",fill="white",activefill="AntiqueWhite2",width=5)
    canvas.create_text(417,app.height-60,text="Storage",fill="black", font="Arial 15")
    canvas.create_rectangle(558,app.height-120,837,app.height,outline="black",fill="white",activefill="AntiqueWhite2",width=5)
    canvas.create_text(697,app.height-60,text="Lamps",fill="black", font="Arial 15")
    canvas.create_rectangle(app.width/2-50,0,app.width/2+50,40,outline="black",fill="white",activefill="AntiqueWhite2",width=5)
    canvas.create_text(app.width/2,20,text="Done",fill="black",font="Arial 15")
    #draw objects chosen on other splash screens
    for key in app.allAbove:
            if key==brownCouch:
                canvas.create_image(app.brownCouch.cx, app.brownCouch.cy, image=ImageTk.PhotoImage(app.brownCouch2))
            if key==pinkCouch:
                canvas.create_image(app.pinkCouch.cx, app.pinkCouch.cy, image=ImageTk.PhotoImage(app.pinkCouch2))
            if key==blueCouch:
                canvas.create_image(app.blueCouch.cx, app.blueCouch.cy, image=ImageTk.PhotoImage(app.blueCouch2))
            if key==oldLamp:
                canvas.create_image(app.oldLamp.cx,app.oldLamp.cy,image=ImageTk.PhotoImage(app.lamp2))
            if key==pinkLamp:
                canvas.create_image(app.pinkLamp.cx,app.pinkLamp.cy,image=ImageTk.PhotoImage(app.plamp2))
            if key==blueLamp:
                canvas.create_image(app.blueLamp.cx,app.blueLamp.cy,image=ImageTk.PhotoImage(app.blamp2))
            if key==bookshelf:
                canvas.create_image(app.bookshelf.cx, app.bookshelf.cy, image=ImageTk.PhotoImage(app.bookshelf2))
            if key==drawer:
                canvas.create_image(app.drawer.cx, app.drawer.cy, image=ImageTk.PhotoImage(app.drawer2))
            if key==blueDrawer:
                canvas.create_image(app.blueDrawer.cx, app.blueDrawer.cy, image=ImageTk.PhotoImage(app.blueDrawer2))


def optionsMode_mousePressed(app,event):
    if event.x >= 15 and event.x <= 105 and event.y >= 10 and event.y <= 50:
        colortoend = app.bgColor.pop(0)
        app.bgColor.append(colortoend)
    if event.x>=3 and event.x<=279 and event.y>=app.height-120 and event.y<=app.height:
        app.lampCheck=True
        app.mode="couchesMode"
    if event.x>=558 and event.x<=837 and event.y>=app.height-120 and event.y<=app.height:
        app.couchCheck=True
        app.mode="lampsMode"
    if event.x>=279 and event.x<=558 and event.y>=app.height-120 and event.y<=app.height:
        app.storageCheck=True
        app.mode="storageMode"
    if event.x>=app.width/2-50 and event.x<=app.width/2+50 and event.y>=0 and event.y<=40:
        app.mode="scoreMode"

def drawButton(canvas,coords):
    x0,y0,x1,y1 = coords
    canvas.create_rectangle(x0,y0,x1,y1, fill='lightgray',activefill='CadetBlue1')
    canvas.create_text((x0+x1)/2,(y0+y1)/3,text='change', font = 'Helvetica 10 bold',fill="black")
    canvas.create_text((x0+x1)/2,(y0+y1)/2,text='carpet', font = 'Helvetica 10 bold',fill="black")
    canvas.create_text((x0+x1)/2,2*(y0+y1)/3,text='color', font = 'Helvetica 10 bold',fill="black")

##########################################
# couchesMode
##########################################
#move couches in this splashscreen
def couchesMode_mousePressed(app,event):
    if event.x>=app.width/2-50 and event.x<=app.width/2+50 and event.y>=app.height-150 and event.y<=app.height-120:
        app.couchLocations[brownCouch]=(app.brownCouch.cx,app.brownCouch.cy)
        app.couchLocations[blueCouch]=(app.blueCouch.cx,app.blueCouch.cy)
        app.couchLocations[pinkCouch]=(app.pinkCouch.cx,app.pinkCouch.cy)
        for key in app.couchLocations:
            if app.couchLocations[key][1]<=app.height-160:
                app.allAbove[key]=app.couchLocations[key]
            else:
                if key in app.allAbove:
                    del app.allAbove[key]
        app.couchCheck=True
        app.mode="optionsMode"

def couchesMode_mouseDragged(app,event):
    changeBudget(app)
    if event.x>=app.brownCouch.cx-.5*app.brownCouch.dimensions[0] and event.x<=app.brownCouch.cx+.5*app.brownCouch.dimensions[0] and event.y>=app.brownCouch.cy-.5*app.brownCouch.dimensions[1] and event.y<=app.brownCouch.cy+.5*app.brownCouch.dimensions[1]:
        app.brownCouch.cx=event.x
        app.brownCouch.cy=event.y
        app.pinkCouch.cx=app.pinkCouch.cx
        app.pinkCouch.cy=app.pinkCouch.cy
        app.blueCouch.cx=app.blueCouch.cx
        app.blueCouch.cy=app.blueCouch.cy
    if event.x>=app.pinkCouch.cx-130 and event.x<=app.pinkCouch.cx+130 and event.y>=app.pinkCouch.cy-50 and event.y<=app.pinkCouch.cy+50:
        app.brownCouch.cx=app.brownCouch.cx
        app.brownCouch.cy=app.brownCouch.cy
        app.pinkCouch.cx=event.x
        app.pinkCouch.cy=event.y
        app.blueCouch.cx=app.blueCouch.cx
        app.blueCouch.cy=app.blueCouch.cy
    if event.x>=app.blueCouch.cx-107 and event.x<=app.blueCouch.cx+107 and event.y>=app.blueCouch.cy-50 and event.y<=app.blueCouch.cy+65:
        app.brownCouch.cx=app.brownCouch.cx
        app.brownCouch.cy=app.brownCouch.cy
        app.pinkCouch.cx=app.pinkCouch.cx
        app.pinkCouch.cy=app.pinkCouch.cy
        app.blueCouch.cx=event.x
        app.blueCouch.cy=event.y
#check for collisions within the couch splashscreen
    for couch1 in app.couchList:
        for couch2 in app.couchList:
            if couch1!=couch2:
                checkCollision(app,couch1,couch2)

#update the dictionary of all objects above the options bar
    app.couchLocations[brownCouch]=(app.brownCouch.cx,app.brownCouch.cy)
    app.couchLocations[blueCouch]=(app.blueCouch.cx,app.blueCouch.cy)
    app.couchLocations[pinkCouch]=(app.pinkCouch.cx,app.pinkCouch.cy)
#loop through the couches and the allAbove dictionary and check for collisions
#this is for checking collisions between different splashscreens
    for key in app.couchLocations:
        if app.couchLocations[key][1]>=app.height-160:
            if key in app.allAbove:
                del app.allAbove[key]
        if app.couchLocations[key][1]<app.height-160:
            app.allAbove[key]=app.couchLocations[key]
    index=0
    keyList=list(app.allAbove.keys())
    while index<len(keyList): 
        for couch in app.couchList:    
            if keyList[index]!=couch and couch in app.allAbove:                    
                checkCollisionDif(app,keyList[index],couch)
        if keyList[index] not in app.allAbove:
            keyList.pop(index)
        else:
            index+=1

def couchesMode_drawBudget(app,canvas):
    canvas.create_text(app.width-app.width/10,app.height/12,\
        text=f'Budget: ${app.budget}',fill="black",font="Arial 15 bold")

def couchesMode_redrawAll(app,canvas):
    drawBG(app, canvas)
    couchesMode_drawBudget(app,canvas)
    canvas.create_rectangle(0,0,app.width,app.height-120,outline="black",width=5)
    canvas.create_rectangle(app.width/2-50,app.height-150,app.width/2+50,app.height-120,outline="black",fill="white",activefill="AntiqueWhite2",width=5)
    canvas.create_text(app.width/2, app.height-135,text="Done",fill="black",font="Arial 15")
    canvas.create_image(app.brownCouch.cx, app.brownCouch.cy, image=ImageTk.PhotoImage(app.brownCouch2))
    canvas.create_rectangle(app.brownCouch.cx-123,app.brownCouch.cy-50,app.brownCouch.cx+123,app.brownCouch.cy+50,outline=app.bgColor[0])
    canvas.create_text(120,700,text=f'${brownCouch.getPrice()}',fill="NavajoWhite3")
    canvas.create_text(120,720,text=f'Year: {brownCouch.getYear()}',fill="NavajoWhite3")
    canvas.create_text(120,740,text=f'Seats: {brownCouch.getSeats()}',fill="NavajoWhite3") 
    canvas.create_image(app.pinkCouch.cx, app.pinkCouch.cy, image=ImageTk.PhotoImage(app.pinkCouch2))
    canvas.create_rectangle(app.pinkCouch.cx-130,app.pinkCouch.cy-50,app.pinkCouch.cx+130,app.pinkCouch.cy+50,outline=app.bgColor[0])
    canvas.create_text(400,700,text=f'${pinkCouch.getPrice()}',fill="NavajoWhite4")
    canvas.create_text(400,720,text=f'Year: {pinkCouch.getYear()}',fill="NavajoWhite4")
    canvas.create_text(400,740,text=f'Seats: {pinkCouch.getSeats()}',fill="NavajoWhite4")
    canvas.create_image(app.blueCouch.cx, app.blueCouch.cy, image=ImageTk.PhotoImage(app.blueCouch2))
    canvas.create_rectangle(app.blueCouch.cx-107,app.blueCouch.cy-50,app.blueCouch.cx+107,app.blueCouch.cy+65,outline=app.bgColor[0])  
    canvas.create_text(650,700,text=f'${blueCouch.getPrice()}',fill="NavajoWhite3")
    canvas.create_text(650,720,text=f'Year: {blueCouch.getYear()}',fill="NavajoWhite3")
    canvas.create_text(650,740,text=f'Seats: {blueCouch.getSeats()}',fill="NavajoWhite3")
    #draws chosen furniture from other splashscreens
    for key in app.allAbove:
            if key==oldLamp:
                canvas.create_image(app.oldLamp.cx,app.oldLamp.cy,image=ImageTk.PhotoImage(app.lamp2))
            if key==pinkLamp:
                canvas.create_image(app.pinkLamp.cx,app.pinkLamp.cy,image=ImageTk.PhotoImage(app.plamp2))
            if key==blueLamp:
                canvas.create_image(app.blueLamp.cx,app.blueLamp.cy,image=ImageTk.PhotoImage(app.blamp2))
            if key==bookshelf:
                canvas.create_image(app.bookshelf.cx, app.bookshelf.cy, image=ImageTk.PhotoImage(app.bookshelf2))
            if key==drawer:
                canvas.create_image(app.drawer.cx, app.drawer.cy, image=ImageTk.PhotoImage(app.drawer2))
            if key==blueDrawer:
                canvas.create_image(app.blueDrawer.cx, app.blueDrawer.cy, image=ImageTk.PhotoImage(app.blueDrawer2))
    if app.distance==True:
        canvas.create_rectangle(app.width/2-20,app.height/2-20,app.width/2+20,app.height/2+20,fill="black")

##########################################
# lampsMode
##########################################
#where user can choose lamps
def lampsMode_mousePressed(app,event):
    if event.x>=app.width/2-50 and event.x<=app.width/2+50 and event.y>=app.height-150 and event.y<=app.height-120:
        app.lampLocations[oldLamp]=(app.oldLamp.cx,app.oldLamp.cy)
        app.lampLocations[blueLamp]=(app.blueLamp.cx,app.blueLamp.cy)
        app.lampLocations[pinkLamp]=(app.pinkLamp.cx,app.pinkLamp.cy)
        for key in app.lampLocations:
            if app.lampLocations[key][1]<=app.height-165:
                app.allAbove[key]=app.lampLocations[key]
            else:
                if key in app.allAbove:
                    del app.allAbove[key]
        app.lampCheck=True
        app.mode="optionsMode"

def lampsMode_mouseDragged(app,event):
    changeBudget(app)
    if event.x>=app.oldLamp.cx-27 and event.x<=app.oldLamp.cx+27 and event.y>=app.oldLamp.cy-45 and event.y<=app.oldLamp.cy+45:
        app.oldLamp.cx=event.x
        app.oldLamp.cy=event.y
        app.pinkLamp.cx=app.pinkLamp.cx
        app.pinkLamp.cy=app.pinkLamp.cy
        app.blueLamp.cx=app.blueLamp.cx
        app.blueLamp.cy=app.blueLamp.cy        
    if event.x>=app.pinkLamp.cx-27 and event.x<=app.pinkLamp.cx+27 and event.y>=app.pinkLamp.cy-40 and event.y<=app.pinkLamp.cy+40:
        app.oldLamp.cx=app.oldLamp.cx
        app.oldLamp.cy=app.oldLamp.cy
        app.pinkLamp.cx=event.x
        app.pinkLamp.cy=event.y
        app.blueLamp.cx=app.blueLamp.cx
        app.blueLamp.cy=app.blueLamp.cy
    if event.x>=app.blueLamp.cx-23 and event.x<=app.blueLamp.cx+27 and event.y>=app.blueLamp.cy-44 and event.y<=app.blueLamp.cy+37:
        app.oldLamp.cx=app.oldLamp.cx
        app.oldLamp.cy=app.oldLamp.cy
        app.pinkLamp.cx=app.pinkLamp.cx
        app.pinkLamp.cy=app.pinkLamp.cy
        app.blueLamp.cx=event.x
        app.blueLamp.cy=event.y
#check for collisions within the lamp splashscreen
    for lamp1 in app.lampList:
        for lamp2 in app.lampList:
            if lamp1!=lamp2:
                checkCollision(app,lamp1,lamp2)
#update the dictionary of all objects above the options bar
    app.lampLocations[oldLamp]=(app.oldLamp.cx,app.oldLamp.cy)
    app.lampLocations[pinkLamp]=(app.pinkLamp.cx,app.pinkLamp.cy)
    app.lampLocations[blueLamp]=(app.blueLamp.cx,app.blueLamp.cy)
#loop through the lamps and the allAbove dictionary and check for collisions
#this is for checking collisions between different splashscreens
    for key in app.lampLocations:
        if app.lampLocations[key][1]>=app.height-160:
            if key in app.allAbove:
                del app.allAbove[key]
        if app.lampLocations[key][1]<app.height-160:
            app.allAbove[key]=app.lampLocations[key]

    index=0
    keyList=list(app.allAbove.keys())
    while index<len(keyList): 
        for lamp in app.lampList:    
            if keyList[index]!=lamp and lamp in app.allAbove:                    
                checkCollisionDif(app,keyList[index],lamp)
        if keyList[index] not in app.allAbove:
            keyList.pop(index)
        else:
            index+=1

def lampsMode_drawBudget(app,canvas):
    canvas.create_text(app.width-app.width/10,app.height/12,\
        text=f'Budget: ${app.budget}',fill="black",font="Arial 15 bold")

def lampsMode_redrawAll(app,canvas):
    drawBG(app, canvas)
    canvas.create_rectangle(0,0,app.width,app.height-120,outline="black",width=5)
    lampsMode_drawBudget(app,canvas)
    canvas.create_rectangle(app.width/2-50,app.height-150,app.width/2+50,app.height-120,outline="black",fill="white",activefill="AntiqueWhite2",width=5)
    canvas.create_text(app.width/2, app.height-135,text="Done",fill="black",font="Arial 15")
    canvas.create_image(app.oldLamp.cx,app.oldLamp.cy,image=ImageTk.PhotoImage(app.lamp2))
    canvas.create_rectangle(app.oldLamp.cx-27,app.oldLamp.cy-45,app.oldLamp.cx+27,app.oldLamp.cy+45,outline=app.bgColor[0])
    canvas.create_text(180,720,text=f'${oldLamp.getPrice()}',fill="black")
    canvas.create_text(180,700,text=f'Year: {oldLamp.getYear()}',fill="black")
    canvas.create_image(app.pinkLamp.cx,app.pinkLamp.cy,image=ImageTk.PhotoImage(app.plamp2))
    canvas.create_rectangle(app.pinkLamp.cx-27,app.pinkLamp.cy-40,app.pinkLamp.cx+27,app.pinkLamp.cy+40,outline=app.bgColor[0])
    canvas.create_text(480,720,text=f'${pinkLamp.getPrice()}',fill="black")
    canvas.create_text(480,700,text=f'Year: {pinkLamp.getYear()}',fill="black")
    canvas.create_image(app.blueLamp.cx,app.blueLamp.cy,image=ImageTk.PhotoImage(app.blamp2))
    canvas.create_rectangle(app.blueLamp.cx-23,app.blueLamp.cy-44,app.blueLamp.cx+27,app.blueLamp.cy+37,outline=app.bgColor[0])
    canvas.create_text(600,720,text=f'${blueLamp.getPrice()}',fill="black")
    canvas.create_text(600,700,text=f'Year: {blueLamp.getYear()}',fill="black")
    #prints furniture from other splashscreens
    for key in app.allAbove:
            if key==brownCouch:
                canvas.create_image(app.brownCouch.cx, app.brownCouch.cy, image=ImageTk.PhotoImage(app.brownCouch2))
            if key==pinkCouch:
                canvas.create_image(app.pinkCouch.cx, app.pinkCouch.cy, image=ImageTk.PhotoImage(app.pinkCouch2))
            if key==blueCouch:
                canvas.create_image(app.blueCouch.cx, app.blueCouch.cy, image=ImageTk.PhotoImage(app.blueCouch2))
            if key==bookshelf:
                canvas.create_image(app.bookshelf.cx, app.bookshelf.cy, image=ImageTk.PhotoImage(app.bookshelf2))
            if key==drawer:
                canvas.create_image(app.drawer.cx, app.drawer.cy, image=ImageTk.PhotoImage(app.drawer2))
            if key==blueDrawer:
                canvas.create_image(app.blueDrawer.cx, app.blueDrawer.cy, image=ImageTk.PhotoImage(app.blueDrawer2))
##########################################
# storageMode
##########################################
#where user can choose storage furniture
def storageMode_mousePressed(app,event):
    if event.x>=app.width/2-50 and event.x<=app.width/2+50 and event.y>=app.height-150 and event.y<=app.height-120:
        app.storageLocations[bookshelf]=(app.bookshelf.cx,app.bookshelf.cy)
        app.storageLocations[drawer]=(app.drawer.cx,app.drawer.cy)
        app.storageLocations[blueDrawer]=(app.blueDrawer.cx,app.blueDrawer.cy)
        for key in app.storageLocations:
            if app.storageLocations[key][1]<=app.height-180:
                app.allAbove[key]=app.storageLocations[key]
            else:
                if key in app.allAbove:
                    del app.allAbove[key]
        app.storageCheck=True
        app.mode="optionsMode"

def storageMode_mouseDragged(app,event):
    changeBudget(app)
    if event.x>=app.bookshelf.cx-35 and event.x<=app.bookshelf.cx+35 and event.y>=app.bookshelf.cy-70 and event.y<=app.bookshelf.cy+65:
        app.bookshelf.cx=event.x
        app.bookshelf.cy=event.y
        app.drawer.cx=app.drawer.cx
        app.drawer.cy=app.drawer.cy
        app.blueDrawer.cx=app.blueDrawer.cx
        app.blueDrawer.cy=app.blueDrawer.cy
    if event.x>=app.drawer.cx-45 and event.x<=app.drawer.cx+45 and event.y>=app.drawer.cy-45 and event.y<=app.drawer.cy+45:
        app.bookshelf.cx=app.bookshelf.cx
        app.bookshelf.cy=app.bookshelf.cy
        app.drawer.cx=event.x
        app.drawer.cy=event.y
        app.blueDrawer.cx=app.blueDrawer.cx
        app.blueDrawer.cy=app.blueDrawer.cy
    if event.x>=app.blueDrawer.cx-30 and event.x<=app.blueDrawer.cx+30 and event.y>=app.blueDrawer.cy-35 and event.y<=app.blueDrawer.cy+35:
        app.bookshelf.cx=app.bookshelf.cx
        app.bookshelf.cy=app.bookshelf.cy
        app.drawer.cx=app.drawer.cx
        app.drawer.cy=app.drawer.cy
        app.blueDrawer.cx=event.x
        app.blueDrawer.cy=event.y
#check for collisions within the storage splashscreen
    for sto1 in app.storageList:
        for sto2 in app.storageList:
            if sto1!=sto2:
                checkCollision(app,sto1,sto2)
#update the dictionary of all objects above the options bar
    app.storageLocations[bookshelf]=(app.bookshelf.cx,app.bookshelf.cy)
    app.storageLocations[drawer]=(app.drawer.cx,app.drawer.cy)
    app.storageLocations[blueDrawer]=(app.blueDrawer.cx,app.blueDrawer.cy)
    #loop through the storage options and the allAbove dictionary and check for collisions
    #this is for checking collisions between different splashscreens
    for key in app.storageLocations:
        if app.storageLocations[key][1]>=app.height-160:
            if key in app.allAbove:
                del app.allAbove[key]
        if app.storageLocations[key][1]<app.height-160:
            app.allAbove[key]=app.storageLocations[key]
    index=0
    keyList=list(app.allAbove.keys())
    while index<len(keyList): 
        for sto in app.storageList:    
            if keyList[index]!=sto and sto in app.allAbove:                    
                checkCollisionDif(app,keyList[index],sto)
        if keyList[index] not in app.allAbove:
            keyList.pop(index)
        else:
            index+=1

def storageMode_drawBudget(app,canvas):
    canvas.create_text(app.width-app.width/10,app.height/12,\
        text=f'Budget: ${app.budget}',fill="black",font="Arial 15 bold")

def storageMode_redrawAll(app,canvas):
    drawBG(app, canvas)
    storageMode_drawBudget(app,canvas)
    canvas.create_rectangle(0,0,app.width,app.height-120,outline="black",width=5)
    canvas.create_rectangle(app.width/2-50,app.height-150,app.width/2+50,app.height-120,outline="black",fill="white",activefill="AntiqueWhite2",width=5)
    canvas.create_text(app.width/2, app.height-135,text="Done",fill="black",font="Arial 15")
    canvas.create_image(app.bookshelf.cx, app.bookshelf.cy, image=ImageTk.PhotoImage(app.bookshelf2))
    canvas.create_rectangle(app.bookshelf.cx-35,app.bookshelf.cy-70,app.bookshelf.cx+35,app.bookshelf.cy+65,outline=app.bgColor[0])
    canvas.create_text(200,700,text=f'${bookshelf.getPrice()}',fill="black")
    canvas.create_text(200,720,text=f'Year: {bookshelf.getYear()}',fill="black")
    canvas.create_text(200,740,text=f'Volume: {bookshelf.getVolume()}',fill="black")
    canvas.create_image(app.drawer.cx, app.drawer.cy, image=ImageTk.PhotoImage(app.drawer2))
    canvas.create_rectangle(app.drawer.cx-45,app.drawer.cy-45,app.drawer.cx+45,app.drawer.cy+45,outline=app.bgColor[0])  
    canvas.create_text(400,700,text=f'${drawer.getPrice()}',fill="black")
    canvas.create_text(400,720,text=f'Year: {drawer.getYear()}',fill="black")
    canvas.create_text(400,740,text=f'Volume: {drawer.getVolume()}',fill="black")
    canvas.create_image(app.blueDrawer.cx, app.blueDrawer.cy, image=ImageTk.PhotoImage(app.blueDrawer2))
    canvas.create_rectangle(app.blueDrawer.cx-30,app.blueDrawer.cy-35,app.blueDrawer.cx+30,app.blueDrawer.cy+35,outline=app.bgColor[0])  
    canvas.create_text(600,700,text=f'${blueDrawer.getPrice()}',fill="black")
    canvas.create_text(600,720,text=f'Year: {blueDrawer.getYear()}',fill="black")
    canvas.create_text(600,740,text=f'Volume: {blueDrawer.getVolume()}',fill="black")
    #printing furniture from other splash screens
    for key in app.allAbove:

            if key==oldLamp:
                canvas.create_image(app.oldLamp.cx,app.oldLamp.cy,image=ImageTk.PhotoImage(app.lamp2))
            if key==pinkLamp:
                canvas.create_image(app.pinkLamp.cx,app.pinkLamp.cy,image=ImageTk.PhotoImage(app.plamp2))
            if key==blueLamp:
                canvas.create_image(app.blueLamp.cx,app.blueLamp.cy,image=ImageTk.PhotoImage(app.blamp2))
            if key==brownCouch:
                canvas.create_image(app.brownCouch.cx, app.brownCouch.cy, image=ImageTk.PhotoImage(app.brownCouch2))
            if key==pinkCouch:
                canvas.create_image(app.pinkCouch.cx, app.pinkCouch.cy, image=ImageTk.PhotoImage(app.pinkCouch2))
            if key==blueCouch:
                canvas.create_image(app.blueCouch.cx, app.blueCouch.cy, image=ImageTk.PhotoImage(app.blueCouch2))
##########################################
# scoreMode
##########################################
#calculates the score of the user's room
#checks the parameters of the used objects and sees if they match theme
def calculateScore(app):
    if app.scoreDone==False:
        if app.client.getTheme()=="vintage":
            for key in app.allAbove:
                if key.getYear()<2000:
                    app.score+=10
        if app.client.getTheme()=="pink":
            for key in app.allAbove:
                if key.getColor()=="pink":
                    app.score+=10
        if app.client.getTheme()=="blue":
            for key in app.allAbove:
                if key.getColor()=="blue":
                    app.score+=10
        if app.client.getTheme()=="good seating and storage":
            for key in app.allAbove:
                if isinstance(key,Couch):
                    app.score+=key.seating*2
                if isinstance(key,Storage):
                    app.score+=key.volume*.2
        #check for parallel lines in placed furniture
        for key1 in app.allAbove:
            for key2 in app.allAbove:
                if key1!=key2:
                    if key1.cy+key1.dimensions[1]/2==key2.cy+key2.dimensions[1]/2:
                        app.score+=5
                    if key1.cy-key1.dimensions[1]/2==key2.cy-key2.dimensions[1]/2:
                        app.score+=5
                    if key1.cx-key1.dimensions[0]/2==key2.cx-key2.dimensions[0]/2:
                        app.score+=5
                    if key1.cx+key1.dimensions[0]/2==key2.cx+key2.dimensions[0]/2:
                        app.score+=5
        if app.budgetCheck==True:
            app.score=app.score-10
        if app.score<0:
            app.score=0
        app.scoreDone=True
    else:
        app.score=app.score

def scoreMode_mousePressed(app,event):
    if event.x>=app.width/2-150 and event.x<=app.width/2+150 and \
    event.y>=app.height/2-270 and event.y<=app.height/2-220:
        calculateScore(app)
        app.scoreCheck=True
    if event.x>=app.width-160 and event.x<=app.width-25 and event.y>=app.height-100 and event.y<=app.height-25:
        app.mode="AIMode"

def scoreMode_redrawAll(app,canvas):
    font="Optima 20" 
    canvas.create_rectangle(0,0,app.width,app.height,fill="SpringGreen4",outline='SpringGreen4')
    canvas.create_rectangle(10,10,app.width-10,app.height-10, outline="SpringGreen2",\
        width=5)
    canvas.create_rectangle(20,20,app.width-20,app.height-20,outline="SpringGreen2",\
        width=5)
    if app.budgetCheck==False:
        canvas.create_text(app.width/2,app.height/2-150,text="Congratulations on finishing the room!", fill="SpringGreen2",font="Optima 40 bold")
    if app.scoreCheck==True:
        canvas.create_text(app.width/2,app.height/2-110,text=f'{app.client.getName()} has given you a score of:', fill="SpringGreen2",font="Optima 25")
        canvas.create_text(app.width/2,app.height/2-50,text=f'{int(app.score)}/60', fill="SpringGreen2",font="Optima 80 bold")
        if app.score==50:
            canvas.create_text(app.width/2,app.height/2,text="It's perfect!",font=font, fill="SpringGreen2")
        if app.score<50 and app.score>=40:
            canvas.create_text(app.width/2,app.height/2,text="Good work!",font=font, fill="SpringGreen2")
        if app.score<40 and app.score>=30:
            canvas.create_text(app.width/2,app.height/2,text="Try harder next time.",font=font, fill="SpringGreen2")
        if app.score<30 and app.score>=20:
            canvas.create_text(app.width/2,app.height/2,text="Maybe you were confused...",font=font, fill="SpringGreen2")
        if app.score<20 and app.score>=10:
            canvas.create_text(app.width/2,app.height/2,text=f'I do not think {app.client.getName()} is pleased...',font=font, fill="SpringGreen2")
        if app.score<10:
            canvas.create_text(app.width/2,app.height/2,text="Maybe you should try a different career.",font=font, fill="SpringGreen2")
    canvas.create_image(app.width/2,app.height-200,\
        image=ImageTk.PhotoImage(app.scaledClientImage))
    canvas.create_rectangle(app.width/2-150,app.height/2-270,app.width/2+150,\
        app.height/2-220,fill="SpringGreen2",outline="SpringGreen2")
    canvas.create_rectangle(app.width/2-145,app.height/2-265,app.width/2+145,\
        app.height/2-225,fill="SpringGreen4",outline="SpringGreen4")
    canvas.create_rectangle(app.width/2-140,app.height/2-260,app.width/2+140,\
        app.height/2-230,fill="SpringGreen2",outline="SpringGreen2",activefill="SpringGreen3")
    canvas.create_text(app.width/2,app.height/2-245, text="See Score",fill="SpringGreen4",font="Optima 15 bold")
    canvas.create_rectangle(app.width-160,app.height-100,app.width-25,app.height-25,fill="SpringGreen2",outline="black")
    canvas.create_text(app.width-93,app.height-80,text="Click here to see",fill="SpringGreen4",font="Optima 15")
    canvas.create_text(app.width-93,app.height-60,text="how an AI completed",fill="SpringGreen4",font="Optima 14")
    canvas.create_text(app.width-93,app.height-40,text="the client's request!",fill="SpringGreen4",font="Optima 15")
    if app.budgetCheck==True:
        canvas.create_text(app.width/2,app.height/2-150,text="You spent all your money.", fill="SpringGreen2",font="Optima 40 bold")

##########################################
# AIMode
##########################################
#AI alg places furniture in the optimal position for max score

#checks that objects aren't being placed on top of each other, are too close (for visual effect), or 
#not in a horizontal line (horizontal lines guarantees more points)
def isLegal(obj1,obj2):
    if obj1.collided(obj2) or obj1.cy+obj1.dimensions[1]/2!=obj2.cy+obj2.dimensions[1]/2 or dist(obj1,obj2)==False:
        return False
    else:
        return True

#calculates the x distance between objects
def dist(obj1,obj2):
    sep=0
    if obj2.cx>obj1.cx:
        sep=(obj2.cx-obj2.dimensions[0]/2)-(obj1.cx+obj1.dimensions[0]/2)
    else:
        sep=(obj1.cx-obj1.dimensions[0]/2)-(obj2.cx+obj2.dimensions[0]/2)
    if sep<100:
        return False
    else:
        return True

#main backtracking alg: places lamp, keeps placing couch until it's legal, if 
#that's impossible is calls the function again, once the couch and lamp are placed,
#places the storage object, or if that's impossible, call the function again, etc.
def placeFurniture(app):
    xc=random.randint(130,700)
    yc=random.randint(300,500)
    for lamp in lampList:
        if lamp.theme==app.client.theme:
            app.chosenLamp=lamp
    app.chosenLamp.cx=xc
    app.chosenLamp.cy=yc
    app.l1=xc
    app.l2=yc
    for couch in couchList:
        if couch.theme==app.client.theme:
            app.chosenCouch=couch
    cxc=random.randint(130,700)
    cyc=app.chosenLamp.cy+app.chosenLamp.dimensions[1]/2-app.chosenCouch.dimensions[1]/2
    app.chosenCouch.cx=cxc
    app.chosenCouch.cy=cyc
    if isLegal(app.chosenCouch,app.chosenLamp):
        app.c1=app.chosenCouch.cx
        app.c2=app.chosenCouch.cy
        app.AIlocation.append(app.chosenCouch)
        for sto in storageList:
                if sto.theme==app.client.theme:
                    app.chosenSto=sto
        sxc=random.randint(130,700)
        syc=app.chosenLamp.cy+app.chosenLamp.dimensions[1]/2-app.chosenSto.dimensions[1]/2
        app.chosenSto.cx=sxc
        app.chosenSto.cy=syc
        if isLegal(app.chosenSto,app.chosenLamp) and isLegal(app.chosenSto,app.chosenCouch):
            app.s1=app.chosenSto.cx
            app.s2=app.chosenSto.cy
            app.AIlocation.append(app.chosenSto)
            return None
        else:
            return placeFurniture(app)
    else:
        return placeFurniture(app)

def drawFurniture(app,canvas):
    if app.chosenLamp==oldLamp:
        canvas.create_image(app.l1,app.l2,image=ImageTk.PhotoImage(app.lamp2))
    if app.chosenLamp==pinkLamp:
        canvas.create_image(app.l1,app.l2,image=ImageTk.PhotoImage(app.plamp2))
    if app.chosenLamp==blueLamp:
        canvas.create_image(app.l1,app.l2,image=ImageTk.PhotoImage(app.blamp2))
    if app.chosenCouch==brownCouch:
        canvas.create_image(app.c1,app.c2,image=ImageTk.PhotoImage(app.brownCouch2))
    if app.chosenCouch==pinkCouch:
        canvas.create_image(app.c1,app.c2,image=ImageTk.PhotoImage(app.pinkCouch2))
    if app.chosenCouch==blueCouch:
        canvas.create_image(app.c1,app.c2,image=ImageTk.PhotoImage(app.blueCouch2))
    if app.chosenSto==bookshelf:
        canvas.create_image(app.s1,app.s2,image=ImageTk.PhotoImage(app.bookshelf2))
    if app.chosenSto==drawer:
        canvas.create_image(app.s1,app.s2,image=ImageTk.PhotoImage(app.drawer2))
    if app.chosenSto==blueDrawer:
        canvas.create_image(app.s1,app.s2,image=ImageTk.PhotoImage(app.blueDrawer2))

def drawCarpet(app,canvas):
    if app.client.getTheme()=="pink":
        canvas.create_rectangle(0,0,app.width,app.height,fill="HotPink1",outline="HotPink1")
    if app.client.getTheme()=="blue":
        canvas.create_rectangle(0,0,app.width,app.height,fill="DodgerBlue3",outline="DodgerBlue3")
    if app.client.getTheme()=="vintage":
        canvas.create_rectangle(0,0,app.width,app.height,fill="burlywood3",outline="burlywood3")
    if app.client.getTheme()=="good seating and storage":
        canvas.create_rectangle(0,0,app.width,app.height,fill="LemonChiffon2",outline="LemonChiffon2")

def AIMode_mousePressed(app,event):
    if event.x<=app.width/2+80 and event.x>=app.width/2-80 and event.y<=app.height-30 and event.y>=app.height-60:
        placeFurniture(app)
        app.AIbutton=True
    if event.x<=app.width/2+60 and event.x>=app.width/2-60 and event.y<=60 and event.y>=10:
        app.score=0
        app.mode="scoreAIMode"

def drawScoreButton(app,canvas):
    canvas.create_rectangle(app.width/2-60,10,app.width/2+60,60,fill="white",outline="white",activefill="AntiqueWhite4")
    canvas.create_rectangle(app.width/2-70,0,app.width/2+70,70,outline="white",width=5)
    canvas.create_text(app.width/2,35,text="See Score",font="Cochin 17",fill="black")

def AIMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill="IndianRed3",outline="IndianRed3")
    canvas.create_rectangle(10,10,app.width-10,app.height-10, outline="IndianRed4",width=5)
    canvas.create_rectangle(20,20,app.width-20,app.height-20,outline="IndianRed4",width=5)
    canvas.create_rectangle(app.width/2-80,app.height-60,app.width/2+80,app.height-30,fill="IndianRed4",outline="IndianRed4",activefill='IndianRed1')
    canvas.create_rectangle(app.width/2-90,app.height-70,app.width/2+90,app.height-20,outline="IndianRed4",width=5)
    canvas.create_text(app.width/2,app.height-45,text="Click to see AI room",font="Cochin 17", fill="white")
    if app.AIbutton==True:
        drawCarpet(app,canvas)
        drawFurniture(app,canvas)
        drawScoreButton(app,canvas)

##########################################
# scoreAIMode
##########################################
#scores the room the AI created

def calculateAIScore(app):
    app.AIlocation=[app.chosenLamp,app.chosenCouch,app.chosenSto]
    if app.scoreAIDone==False:
        if app.client.getTheme()=="vintage":
            for key in app.AIlocation:
                if key.getYear()<2000:
                    app.score+=10
        if app.client.getTheme()=="pink":
            for key in app.AIlocation:
                if key.getColor()=="pink":
                    app.score+=10
        if app.client.getTheme()=="blue":
            for key in app.AIlocation:
                if key.getColor()=="blue":
                    app.score+=10
        if app.client.getTheme()=="good seating and storage":
            for key in app.AIlocation:
                if isinstance(key,Couch):
                    app.score+=key.seating*2
                if isinstance(key,Storage):
                    app.score+=key.volume*.2
        #check for parallel lines in placed furniture
        for key1 in app.AIlocation:
            for key2 in app.AIlocation:
                if key1!=key2:
                    if key1.cy+key1.dimensions[1]/2==key2.cy+key2.dimensions[1]/2:
                        app.score+=5
                    if key1.cy-key1.dimensions[1]/2==key2.cy-key2.dimensions[1]/2:
                        app.score+=5
                    if key1.cx-key1.dimensions[0]/2==key2.cx-key2.dimensions[0]/2:
                        app.score+=5
                    if key1.cx+key1.dimensions[0]/2==key2.cx+key2.dimensions[0]/2:
                        app.score+=5
        app.AIChecker=True
        app.scoreAIDone=True
    else:
        app.score=app.score

def scoreAIMode_mousePressed(app,event):
    if event.x>=app.width/2-150 and event.x<=app.width/2+150 and \
    event.y>=app.height/2-270 and event.y<=app.height/2-220:
        calculateAIScore(app)
        app.scoreCheck=True
    if event.x>=app.width-160 and event.x<=app.width-25 and event.y>=app.height-100 and event.y<=app.height-25:
        app.mode="AIMode"
    # if event.x>=app.width/2-140 and event.x<=app.width/2+140 and event.y>=app.height/2-340 and event.y<=app.height/2-310:
    #     appStarted(app)

def scoreAIMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill="goldenrod4",outline='goldenrod4')
    canvas.create_rectangle(10,10,app.width-10,app.height-10, outline="goldenrod2",\
        width=5)
    canvas.create_rectangle(20,20,app.width-20,app.height-20,outline="goldenrod2",\
        width=5)
    if app.budgetCheck==False:
        canvas.create_text(app.width/2,app.height/2-150,text="The AI finished the room!", fill="goldenrod2",font="Georgia 40 bold")
    if app.AIChecker==True:
        canvas.create_text(app.width/2,app.height/2-110,text=f'{app.client.getName()} has given it a score of:', fill="goldenrod2",font="Georgia 25")
        canvas.create_text(app.width/2,app.height/2-50,text=f'{int(app.score)}/60', fill="goldenrod2",font="Georgia 80 bold")
        # canvas.create_rectangle(app.width/2-150,app.height/2-350,app.width/2+150,app.height/2-300,fill="goldenrod2",outline="goldenrod2")
        # canvas.create_rectangle(app.width/2-145,app.height/2-345,app.width/2+145,app.height/2-305,fill="goldenrod4",outline="goldenrod4")
        # canvas.create_rectangle(app.width/2-140,app.height/2-340,app.width/2+140,app.height/2-310,fill="goldenrod2",outline="goldenrod2",activefill="goldenrod3")
        # canvas.create_text(app.width/2,app.height/2-325,text="Play Again",fill="goldenrod4",font="Arial 15 bold")
    canvas.create_image(app.width/2,app.height-200,\
        image=ImageTk.PhotoImage(app.scaledClientImage))
    canvas.create_rectangle(app.width/2-150,app.height/2-270,app.width/2+150,\
        app.height/2-220,fill="goldenrod2",outline="goldenrod2")
    canvas.create_rectangle(app.width/2-145,app.height/2-265,app.width/2+145,\
        app.height/2-225,fill="goldenrod4",outline="goldenrod4")
    canvas.create_rectangle(app.width/2-140,app.height/2-260,app.width/2+140,\
        app.height/2-230,fill="goldenrod2",outline="goldenrod2",activefill="goldenrod3")
    canvas.create_text(app.width/2,app.height/2-245, text="See Score",fill="goldenrod4",font="Georgia 15 bold")

##########################################
# other
##########################################
#pic on start screen from https://www.mymove.com/wp-content/uploads/2022/07/mm-things-you-should-know-about-becoming-an-interior-designer-hero.jpg
def appStarted(app):
    app.mode='startMode'
    app.hintButton=False
    startModeUrl="https://www.mymove.com/wp-content/uploads/2022/07/mm-things-you-should-know-about-becoming-an-interior-designer-hero.jpg"
    app.startModeImage=app.loadImage(startModeUrl)
    app.scaledStartModeImage=app.scaleImage(app.startModeImage,1/6)
    app.clients=clients
    app.client=app.clients[random.randrange(0,len(app.clients))]
    app.clientImage=app.loadImage(app.client.imageLink)
    app.scaledClientImage=app.scaleImage(app.clientImage,1/3)

    couch1=brownCouch.getLink()
    app.brownCouch1=app.loadImage(couch1)
    app.brownCouch2=app.scaleImage(app.brownCouch1, 1/6)
    app.brownCouch=brownCouch
    app.couchList=couchList
    app.couchLocations={}
    app.couchAbove={}
    app.couchCheck=False
    pink1=pinkCouch.getLink()
    app.pinkCouch1=app.loadImage(pink1)
    app.pinkCouch2=app.scaleImage(app.pinkCouch1, 1/3)
    app.pinkCouch=pinkCouch
    blue1=blueCouch.getLink()
    app.blueCouch1=app.loadImage(blue1)
    app.blueCouch2=app.scaleImage(app.blueCouch1, 1/2)
    app.blueCouch=blueCouch

    lamp1=oldLamp.getLink()
    app.lamp1=app.loadImage(lamp1)
    app.lamp2=app.scaleImage(app.lamp1,1/13)
    app.oldLamp=oldLamp
    app.lampList=lampList
    app.lampLocations={}
    app.lampAbove={}
    app.lampCheck=False
    pinklamp1=pinkLamp.getLink()
    app.plamp1=app.loadImage(pinklamp1)
    app.plamp2=app.scaleImage(app.plamp1,1/6)
    app.pinkLamp=pinkLamp
    bluelamp1=blueLamp.getLink()
    app.blamp1=app.loadImage(bluelamp1)
    app.blamp2=app.scaleImage(app.blamp1,1/7)
    app.blueLamp=blueLamp

    app.storageList=storageList
    app.storageLocations={}
    app.storageAbove={}
    app.storageCheck=False
    book1=bookshelf.getLink()
    app.bookshelf1=app.loadImage(book1)
    app.bookshelf2=app.scaleImage(app.bookshelf1, 1/4)
    app.bookshelf=bookshelf
    draw1=drawer.getLink()
    app.drawer1=app.loadImage(draw1)
    app.drawer2=app.scaleImage(app.drawer1, 1/26)
    app.drawer=drawer
    draw2=blueDrawer.getLink()
    app.blueDrawer1=app.loadImage(draw2)
    app.blueDrawer2=app.scaleImage(app.blueDrawer1, 1/8)
    app.blueDrawer=blueDrawer

    app.budget=app.client.getBudget()
    app.scoreCheck=False
    app.score=0
    app.scorefinal = 0
    app.bgColor = ['white','bisque','LemonChiffon2','NavajoWhite3','burlywood3','HotPink1','DodgerBlue3','red','green','gray','IndianRed','brown']
    app.bgColorLen = len(app.bgColor)
    app.scoreColor=''
    app.distance=0

    app.AIlocation=[]
    app.c1=0
    app.c2=0
    app.l1=app.width/2
    app.l2=app.height/2
    app.s1=0
    app.s2=0
    app.furnitureList=furnitureList
    app.imageList=[app.brownCouch2,app.pinkCouch2,app.blueCouch2,app.lamp2,app.plamp2,app.blamp2,app.bookshelf2,app.drawer2,app.blueDrawer2]
    app.allAbove={}
    app.scoreDone=False
    app.brownCouchcheck=False
    app.AIbutton=False
    app.chosenLamp=oldLamp
    app.chosenCouch=brownCouch
    app.chosenSto=bookshelf
    app.budgetCheck=False
    app.scoreAIDone=False
    app.AIChecker=False

runApp(width=838,height=800)

#features beyond MVP:
#budget
#restart game
#timer?
#screen shot save room?
#budget for AI?