player = ('x','o')
num_moves_made = 0
location = range(9)		#[0,1,2,3,4,5,6,7,8]

def draw_board(moves):
	print " %s | %s | %s " % (moves[0], moves[1], moves[2])
	print "-----------"
	print " %s | %s | %s " % (moves[3], moves[4], moves[5])
	print "-----------"
	print " %s | %s | %s " % (moves[6], moves[7], moves[8])

draw_board(location)
full = False
won = False

while(full == False and won == False):
	
	move = int(raw_input("Player %s, where do you want to move? " % (player[num_moves_made%2])))

	if (location[move] != ('x' or 'o')):
		location[move] = player[num_moves_made%2]
		draw_board(location)
	
		if ((location[0] == player[num_moves_made%2] and location[1] == player[num_moves_made%2] and location[2] == player[num_moves_made%2]) or \
			(location[3] == player[num_moves_made%2] and location[4] == player[num_moves_made%2] and location[5] == player[num_moves_made%2]) or \
			(location[6] == player[num_moves_made%2] and location[7] == player[num_moves_made%2] and location[8] == player[num_moves_made%2]) or \
			(location[0] == player[num_moves_made%2] and location[3] == player[num_moves_made%2] and location[6] == player[num_moves_made%2]) or \
			(location[1] == player[num_moves_made%2] and location[4] == player[num_moves_made%2] and location[7] == player[num_moves_made%2]) or \
			(location[2] == player[num_moves_made%2] and location[5] == player[num_moves_made%2] and location[8] == player[num_moves_made%2]) or \
			(location[0] == player[num_moves_made%2] and location[4] == player[num_moves_made%2] and location[8] == player[num_moves_made%2]) or \
			(location[2] == player[num_moves_made%2] and location[4] == player[num_moves_made%2] and location[6] == player[num_moves_made%2])):
			print player[num_moves_made%2], 'is the winner!' 
			won = True

	if (0 not in location and 1 not in location and 2 not in location and 3 not in location and 4 not in location and 5 not in location and 6 not in location and 7 not in location and 8 not in location and (won == False)):
		full = True
		print 'draw!'
	num_moves_made += 1


# If someone won:
	# Print "[letter] wins!"
# Else:
	# Print "draw!"
# Exit the program