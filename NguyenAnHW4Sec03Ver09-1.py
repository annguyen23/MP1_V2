# Project:      HW 4 (NguyenAnHW4Sec03Ver09.py)
# Name:         An Nguyen
# Date:         02/28/18
# Description:  Create a graph let user to click
#               to print ramdom dices and total.

from graphics import*

def main():

    # Create a graph window in khaki:
    win = GraphWin("random dices", 1070,400)
    win.setBackground("Khaki")

    # Set first center points of box and label, dice number:
    point1=Point(50-200,20)
    point2=Point(230-200,200)
    number=0
    center1 = Point(120-200,110)
    center2 = Point(170-200,110)

    # Create loop to draw boxes and labels 5 times:
    for i in range (5):

        # Move center points to draw in next position:
        # Draw boxes:
        point1.move(200,0)
        point2.move(200,0)
        drawbox(win,point1,point2)


        # Move center points to draw in next position:
        # Increase dice number each time:
        # Draw label:
        center1.move(200,0)
        center2.move(200,0)
        number += 1
        drawlabel(win,center1,center2,number)

    # Create a label to draw dice total:
    label_diceTotal = Text(Point(500,270),"Dice Total")
    label_diceTotal.setSize(20)
    label_diceTotal.draw(win)

    # Set the first x max and min point
    # to ask user click in the box later:
    xPoint_Max=230-200
    xPoint_Min=50-200

    # Set the first points to draw dice:
    point1 = Point(-140,30)
    point2 = Point(20,190)

    # Create a messge to ask user to tap in the box:
    message = Text(Point(500,230),"Please tap in the box in order")
    message.draw(win)

    # Set dice total = 0:
    intdiceTotal = 0

    # Set n=1 to run the loop below:
    n=1

    # Set center point of dot to draw dot in loop:
    center = Point(140-200,110)

    # import random to use random (1-6):
    import random

    # Create a label to draw total dice value:
    label_dice_num = Text(Point(502,310),"")
    label_dice_num.setSize(20)
    label_dice_num.draw(win)
    
    # Create loop to draw dices and dots inside:
    while n==1:

        # Increase x max and min point 200
        # because each box-point's gap is 200 
        xPoint_Max=xPoint_Max+200
        xPoint_Min=xPoint_Min+200

        # Pause the program until user click
        # Then get x and y points to set
        # program for user to click inside box:
        ClickXY = win.getMouse()
        xPoint = ClickXY.getX()
        yPoint = ClickXY.getY()

        # Move points to draw the next boxes and dots:
        point1.move(200,0)
        point2.move(200,0)
        center.move(200,0)

        # Undraw the message because user does not click yet
        # Also, undraw the message when user tap wrong.
        message.undraw()

        # set bltRun=True to run loop below:
        bltRun=True


        
        # Create loop to draw dices and dots inside:
        while bltRun==True:

            # Create the program for user to tap inside box:
            if xPoint_Max>xPoint>xPoint_Min and 200>yPoint>20:

                # Let the dice runs random 1-6:
                # Calculate the total dice value:
                dice = random.randint(1, 6)
                intdiceTotal += dice

                # Draw the dice:
                drawbox(win,point1,point2)

                # Create a loop to draw dots:
                if dice == 1:
                    dice_number1(win,center)
                elif dice == 2:
                    dice_number2(win,center)
                elif dice == 3:
                    dice_number1(win,center)
                    dice_number2(win,center)
                elif dice == 4:
                    dice_number2(win,center)
                    dice_number4(win,center)
                elif dice == 5:
                    dice_number1(win,center)
                    dice_number2(win,center)
                    dice_number4(win,center)
                else:
                    dice_number2(win,center)
                    dice_number4(win,center)
                    dice_number6(win,center)
                
                # Undraw the "ask user click in box" 
                # message when they click right: 
                message.undraw()

                # Draw the total dice value:
                label_dice_num.setText(intdiceTotal)

                # Set bltRun=False to stop the second while loop:
                bltRun=False

            # For user if click outside box
            # or not in right box:
            else:

                # Draw the messge to warn them:
                message.draw(win)

                # Decrease the x min and max click
                # point for loop to run again
                xPoint_Max=xPoint_Max-200
                xPoint_Min=xPoint_Min-200

                # Move points of dice-box and dot
                # back 200 to run loop again
                point1.move(-200,0)
                point2.move(-200,0)
                center.move(-200,0)

                # Set bltRun=False to stop the second while loop:
                bltRun=False

        # Create a loop to stop the first loop
        # when the last dice is drawn:
        if xPoint_Max == 1030:
            n=0
            
    # Set points to draw exit-button:
    point1 = Point(900,340)
    point2 = Point(1000,380)
    drawbox(win,point1,point2)
    
    # Draw "exit" inside the exit-button:
    label_exit = Text (Point(948,360),"Exit")
    label_exit.setSize(20)
    label_exit.setFill("red")
    label_exit.draw(win)

    # Create a program to close graph win
    # when user click in the exit-button:
    bltRun_exit = True
    while bltRun_exit==True:
        Click_exit = win.getMouse()
        xPt = Click_exit.getX()
        yPt = Click_exit.getY()
        if 1000>xPt>900 and 380>yPt>340:
            win.close()
            bltRun_exit=False   
        else:
            bltRun_exit=True
            
# Create a function to draw boxes, dices and buttons:
def drawbox(win,point1,point2):
    box = Rectangle(point1,point2)
    box.setFill("White")
    box.setOutline("Gray")
    box.setWidth(3)
    box.draw(win)

# Create a function to draw dice labels with numbers:
def drawlabel(win,center1,center2,number):
    label1 = Text (center1,"Dice")
    label1.setSize(20)
    label1.draw(win)
    label2 = Text (center2,number)
    label2.setSize(20)
    label2.draw(win)

# Create a function to draw dots:
def drawdot(win,center_dot):
    dot = Circle(center_dot,20)
    dot.setFill("Black")
    dot.draw(win)
    
# Create a function to draw 1-dot dice:
def dice_number1(win,center):
    drawdot(win,center)
    
# Create a function to draw 2-dot dice: 
def dice_number2(win,center):
    center.move(-45,-45)
    drawdot(win,center)   
    center.move(90,90)
    drawdot(win,center)
    center.move(-45,-45)

# Create a function to draw 4-dot dice:
def dice_number4(win,center):
    center.move(45,-45)
    drawdot(win,center)
    center.move(-90,90)
    drawdot(win,center)
    center.move(45,-45)

# Create a function to draw 6-dot dice:
def dice_number6(win, center):
    center.move(-45,0)
    drawdot(win,center)
    center.move(90,0)
    drawdot(win,center)
    center.move(-45,0)

    
main()






