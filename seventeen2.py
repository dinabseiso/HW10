#! usr/bin/env python
# seventeen2.py

### Import here
from random import randint


### Body
def draws(file):
	with open(file) as fin1:
		future_draws = fin1.readlines()
		return future_draws

def play_game(file):
	"""This function initiates the game. For this particular game, there will be 
	17 marbles in a jar. Turns between the user and the CPU are taken in grabbing
	marbles from the jar, and this will continue for as long as there are marbles
	in the jar. 

	Because the user always goes first, a value is returned for the number of 
	marbles left after the user grabs 1-3 marble/s. The values have already been 
	read from a file in a variable future_draws, which recognizes line breaks. 

	An empty list winner is instantiated for future appending/record-keeping of 
	who has won.

	Each line (aka game) in future_draws is read as a string, including commas. Instead, a list 
	of draws would be prefered, so that we could step through the user choices for 
	as long as there are marbles in the jar. 

	There is a check for whether there are no marbles remaining, and if so the game
	ends and the computer wins. If not, the CPU takes its turn. If the CPU grabs the
	last marble, then the user wins. If not, then...

	Repeat until there are no marbles left.
	"""
	winner = []
	future_draws = draws(file)
	for line in future_draws:
		marbles_in_jar = 17
		marbles_in_jar_after_user = 17
		line_string = line.split(",")
		while marbles_in_jar > 0 and marbles_in_jar_after_user > 0: 
			for draw in line_string: 
				marbles_in_jar_after_user = your_turn(marbles_in_jar, draw)
				if marbles_in_jar_after_user == 0:
					winner.append("P2")
					break
				marbles_in_jar = cpu_turn(marbles_in_jar_after_user)
				if marbles_in_jar == 0:
					winner.append("P1")
					break
	results(future_draws, winner)


def your_turn(marbles_in_jar, future_draws):		
	""" This was not entirely necessary, but because I already implemented it previously
	I figured it would be good to have here as well. It takes in the input from the 
	user explicitly and verifies that the input is valid. If it is not, it iterates again.
	Returns the number of marbles left in the jar for the CPU to evaluate. 
	"""
	your_turn = True
	while your_turn == True:
		for draws in future_draws:
			draws = draws.split(",")
			for grab in draws:
				your_turn, grabbed = check_valid_input(grab, marbles_in_jar)
				marbles_in_jar -= grabbed
				return marbles_in_jar

def cpu_turn(marbles_in_jar):
	""" The computer grabs a random integer between 1 and 3, unless taking that quantity
	is impossible (for example, attempting to grab 3 marbles when only 2 exist). In that 
	case, the CPU will take only two. 

	It is printed to the console the number of marbles the CPU took. The number of marbles
	remaining is then computed, printed, and returned for evaluating into the next turn of 
	the user. 
	""" 
	computer_grab = randint(1, min(3, marbles_in_jar)) 
	marbles_in_jar -= computer_grab
	return marbles_in_jar 

def check_valid_input(grabbed, marbles_in_jar):
	""" This function checks a few possible inputs that would not allow the script to run 
	as it should. For example, if the input is not an integer value, if the user tries to 
	grab more than three marbles, if the user tries to grab no marbles, and if the user 
	tries to grab more marbles than there are in the jar, they will be asked to try again.

	Something additionally covered here is for the number of marbles grabbed to equal the
	number of marbles remaining if the predetermined grab-value is more than the number 
	of marbles left in the jar. 

	Until proper input is received, the loop will continue (see your_turn() and cpu_turn()
		for the while loop that contains this function.) 
	"""
	try: 
		grabbed = int(grabbed)
		if grabbed > 3:
			raise ValueError("Don't be greedy! Try again!")
		elif grabbed == 0:
			raise ValueError("Nice try. Try again!")
		elif marbles_in_jar - grabbed < 0:
			grabbed = marbles_in_jar
			print grabbed
	except Exception:
		print("Sorry, that is not a valid option. Try again! ")
		return True, grabbed
	your_turn = False
	return your_turn, grabbed


def results(future_draws, winner):
	with open("seventeen2_output.txt", "w") as fin2:
		game_number = 1
		winner_index = 0
		for options in future_draws:
			options = options.strip()
			options = options.replace(",","-")
			the_winner = winner[winner_index]
			fin2.write("Game #{}. Play sequence: {}. Winner: {} \n".format(game_number, options, the_winner))
			game_number += 1
			winner_index += 1
		player_one_wins = winner.count("P1")
		player_two_wins = winner.count("P2")
		fin2.write("Player 1 won {} times; Player 2 won {} times.".format(player_one_wins, player_two_wins))




### Define main() 
def main():
	play_game("seventeen2_input.txt")


## Boilerplate

if __name__ == "__main__":
	main()