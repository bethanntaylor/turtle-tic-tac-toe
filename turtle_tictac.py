import turtle

HORIZ_LINE_TOP = (-150,50)
HORIZ_LINE_BOTTOM = (-150,-50)
VERT_LINE_LEFT = (-50,-150)
VERT_LINE_RIGHT = (50,-150)

turtle.setup(500,500)	# set the window size to 500 by 500 pixels
wn = turtle.Screen()
rachel = turtle.Turtle()

rachel.pensize(3)
rachel.pencolor("#00bfff")

rachel.penup()
rachel.setposition(VERT_LINE_LEFT)


rachel.pendown()
rachel.left(90)
rachel.forward(300)
rachel.penup()

rachel.setposition(VERT_LINE_RIGHT)
rachel.pendown()
rachel.forward(300)
rachel.penup()

rachel.setposition(HORIZ_LINE_BOTTOM)
rachel.pendown()
rachel.right(90)
rachel.forward(300)
rachel.penup()

rachel.setposition(HORIZ_LINE_TOP)
rachel.pendown()
rachel.forward(300)
rachel.penup()

def draw_x(x,y):
	# TODO: Make sure turtle is facing right
	rachel.pencolor("pink")
	rachel.penup()
	rachel.setpos(x+5,y-5)
	rachel.right(45)
	rachel.pendown()
	rachel.forward(100)
	rachel.penup()
	rachel.setposition(x+90,y-5)
	rachel.right(90)
	rachel.pendown()
	rachel.forward(100)	
	rachel.right(225)


def draw_o(x,y):
	rachel.pencolor("blue")
	rachel.penup()
	rachel.setpos(x+30,y-80)
	rachel.pendown()
	rachel.circle(40)
 
player = ()
num_moves_made = 0
# full = False
# won = False

boxes = {'box1': False, 'box2': False, 'box3': False, 'box4': False, 'box5': False, 'box6': False, 'box7': False, 'box8': False, 'box9': False}
num_moves_made = 0 



def draw_symbol(x,y):
	print "x:",x, "y:",y
	if(-150 <= x <= -50 and 50 <= y <= 150): # Square 1
		player(-145,145) 
		boxes['box1'] = True
	elif(-50 <= x <= 50 and 50 <= y <= 150):	# Square 2
		player(-40,145)
		boxes['box2'] = True
	elif(50 <= x <= 150 and 50 <= y <= 150):	# Square 3
		player(55,145)
		boxes['box3'] = True
	elif(-150 <= x <= -50 and -50 <= y <= 50):	# Square 4
		player(-145,45)
		boxes['box4'] = True
	elif(-50 <= x <= 50 and -50 <= y <= 50):	# Square 5
		player(-40,45)
		boxes['box5'] = True
	elif(50 <= x <= 150 and -50 <= y <= 50):	# Square 6
		player(55,45)
		boxes['box6'] = True
	elif(-150 <= x <= -50 and -150 <= y <= -50):	# Square 7
		player(-145,-45)
		boxes['box7'] = True
	elif(-50 <= x <= 50 and -150 <= y <= -50):	# Square 8
		player(-45,-45)
		boxes['box8'] = True
	elif(50 <= x <= 150 and -150 <= y <= -50):	# Square 9
		player(55,-45)
		boxes['box9'] = True
	else:
		exit()

guess =()

while (boxes['box1'] == False or boxes['box2'] == False):
	if (num_moves_made%2 == 0):
		player = draw_x
	else:
		player = draw_o
	turtle.onscreenclick(draw_symbol)
	num_moves_made += 1
	# turtle.onscreenclick(draw_symbol)

# or boxes['box3'] or boxes['box4'] or boxes['box5'] or boxes['box6'] or boxes['box7'] or boxes['box8'] or boxes['box9']

# turtle.onscreenclick(draw_symbol)

turtle.mainloop()	# Wait for user to close window
# exitonclick()	# Wait for user to click before closing window

