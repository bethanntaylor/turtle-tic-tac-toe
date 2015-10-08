import turtle

turtle.setup(500,500)	# set the window size to 500 by 500 pixels
wn = turtle.Screen()
rachel = turtle.Turtle()
rachel.pensize(3)
rachel.pencolor("#00bfff")
grid_xy = [[(-150,50), (150,50)], [(-150,-50), (150,-50)], [(-50,-150), (-50,150)], [(50,-150), (50,150)]]
def draw_lines(start,stop):	
	rachel.penup()
	rachel.setposition(start)
	rachel.pendown()
	rachel.setposition(stop)
for i in range(4):
	draw_lines(grid_xy[i][0],grid_xy[i][1])

def draw_x(x,y):
	rachel.pencolor("pink")
	rachel.penup()
	rachel.setpos(x+10,y-90)
	rachel.write('X', font=('Arial', 90, 'normal'))

# def draw_x(x,y):
# 	rachel.pencolor("pink")
# 	rachel.penup()
# 	rachel.setpos(x+5,y-5)
# 	rachel.pendown()
# 	rachel.setpos(x+75,y-75)
# 	rachel.penup()
# 	rachel.setpos(x+75, y-5)
# 	rachel.pendown()
# 	rachel.setpos(x+5,y-75)	

def draw_o(x,y):
	rachel.pencolor("green")
	rachel.penup()
	rachel.setpos(x+10,y-90)
	rachel.write('O', font=('Arial', 90, 'normal'))

# def draw_o(x,y):
# 	rachel.pencolor("blue")
# 	rachel.penup()
# 	rachel.setpos(x+30,y-80)
# 	rachel.pendown()
# 	rachel.circle(40)

# playername = raw_input('player X, enter your name: ')

player1 = [draw_x, ' ']
player2 = [draw_o, ' ']

import tkSimpleDialog
player1[1] = tkSimpleDialog.askstring('Player 1', 'Enter name: ')
player2[1] = tkSimpleDialog.askstring('Player 2', 'Enter name: ')
 
player = ()
num_moves_made = 0

boxes = {1: 'empty', 2: 'empty', 3: 'empty', 4: 'empty', 5: 'empty', 6: 'empty', 7: 'empty', 8: 'empty', 9: 'empty'}
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
		if (boxes[1] == 'empty'):
			boxes[1] = player[1]
			player[0](-145,145)
		else:
			num_moves_made -= 1	
	elif(-50 <= x <= 50 and 50 <= y <= 150):	# Square 2
		if (boxes[2] == 'empty'):
			player[0](-40,145)
			boxes[2] = player[1]
		else:
			num_moves_made -= 1	
	elif(50 <= x <= 150 and 50 <= y <= 150):	# Square 3
		if (boxes[3] == 'empty'):
			player[0](60,145)
			boxes[3] = player[1]
		else:
			num_moves_made -= 1	
	elif(-150 <= x <= -50 and -50 <= y <= 50):	# Square 4
		if (boxes[4] == 'empty'):
			player[0](-145,45)
			boxes[4] = player[1]
		else:
			num_moves_made -= 1	
	elif(-50 <= x <= 50 and -50 <= y <= 50):	# Square 5
		if (boxes[5] == 'empty'):	
			player[0](-40,45)
			boxes[5] = player[1]
		else:
			num_moves_made -= 1	
	elif(50 <= x <= 150 and -50 <= y <= 50):	# Square 6
		if (boxes[6] == 'empty'):
			player[0](55,45)
			boxes[6] = player[1]
		else:
			num_moves_made -= 1	
	elif(-150 <= x <= -50 and -150 <= y <= -50):	# Square 7
		if (boxes[7] == 'empty'):
			player[0](-145,-55)
			boxes[7] = player[1]
		else:
			num_moves_made -= 1	
	elif(-50 <= x <= 50 and -150 <= y <= -50):	# Square 8
		if (boxes[8] == 'empty'):
			player[0](-45,-55)
			boxes[8] = player[1]
		else:
			num_moves_made -= 1	
	elif(50 <= x <= 150 and -150 <= y <= -50):	# Square 9
		if (boxes[9] == 'empty'):
			player[0](55,-55)
			boxes[9] = player[1]
		else:
			num_moves_made -= 1	
	
	for i in range (8):
		if (boxes[win_ans[i][0]] == player[1] and boxes[win_ans[i][1]] == player[1] and boxes[win_ans[i][2]] == player[1]):
			rachel.penup()
			rachel.goto(-240, 160)
			rachel.pendown()
			rachel.write(player[1] + ' is the winner!!!', font=('Arial', 45, 'normal'))
		elif ('empty' not in boxes.values()):
			rachel.penup()
			rachel.goto(-145, 145)
			rachel.pendown()
			rachel.write('Draw!', font=('Arial', 30, 'normal'))


turtle.onscreenclick(draw_symbol)

turtle.mainloop()	# Wait for user to close window
