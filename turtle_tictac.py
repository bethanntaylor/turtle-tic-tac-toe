
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
player1 = [draw_x, 'beth']
player2 = [draw_o, 'markis']

boxes = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False}

win_ans = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]

def draw_symbol(x,y):
	print "x:",x, "y:",y
	global num_moves_made
	num_moves_made += 1
	if (num_moves_made % 2 == 0):
		player = player1
	else:
		player = player2

	if(-150 <= x <= -50 and 50 <= y <= 150): # Square 1
		player[0](-145,145) 
		boxes[1] = player[1]
	elif(-50 <= x <= 50 and 50 <= y <= 150):	# Square 2
		player[0](-40,145)
		boxes[2] = player[1]
	elif(50 <= x <= 150 and 50 <= y <= 150):	# Square 3
		player[0](60,145)
		boxes[3] = player[1]
	elif(-150 <= x <= -50 and -50 <= y <= 50):	# Square 4
		player[0](-145,45)
		boxes[4] = player[1]
	elif(-50 <= x <= 50 and -50 <= y <= 50):	# Square 5
		player[0](-40,45)
		boxes[5] = player[1]
	elif(50 <= x <= 150 and -50 <= y <= 50):	# Square 6
		player[0](55,45)
		boxes[6] = player[1]
	elif(-150 <= x <= -50 and -150 <= y <= -50):	# Square 7
		player[0](-145,-55)
		boxes[7] = player[1]
	elif(-50 <= x <= 50 and -150 <= y <= -50):	# Square 8
		player[0](-45,-55)
		boxes[8] = player[1]
	elif(50 <= x <= 150 and -150 <= y <= -50):	# Square 9
		player[0](55,-55)
		boxes[9] = player[1]
	
	for i in range (8):
		if (boxes[win_ans[i][0]] == player[1] and boxes[win_ans[i][1]] == player[1] and boxes[win_ans[i][2]] == player[1]):
			rachel.penup()
			rachel.goto(-145, 145)
			rachel.pendown()
			rachel.write(player[1] + ' is the winner!!!', font=('Arial', 30, 'normal'))
		elif (False not in boxes.values()):
			turtle.penup()
			turtle.goto(-145, 145)
			rachel.pendown()
			turtle.write('Draw!', font=('Arial', 30, 'normal'))


turtle.onscreenclick(draw_symbol)

# wn.onclick(draw_symbol) # Register function draw to the event mouse_click


# wn.listen() # Begin listening to events like key_press & mouse_clicks
#wn.mainloop()

turtle.mainloop()	# Wait for user to close window
# exitonclick()	# Wait for user to click before closing window

