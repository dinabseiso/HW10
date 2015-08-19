#! usr/bin/env python
# seventeen1.py

### Imports go here
from random import randint


### Body goes here
def play_game():
	"""This function initiates the game. For this particular game, there will be 
	17 marbles in a jar. Turns between the user and the CPU are taken in grabbing
	marbles from the jar, and this will continue for as long as there are marbles
	in the jar. 

	Because the user always goes first, a value is returned for the number of 
	marbles left after the user grabs 1-3 marble/s. 

	There is a check for whether there are no marbles remaining, and if so the game
	ends and the computer wins. If not, the CPU takes its turn. If the CPU grabs the
	last marble, then the user wins. If not, then...

	Repeat until there are no marbles left.
	"""
	marbles_in_jar = 17
	marbles_in_jar_after_user = 17
	while marbles_in_jar > 0 and marbles_in_jar_after_user > 0: 
		marbles_in_jar_after_user = your_turn(marbles_in_jar)
		if marbles_in_jar_after_user == 0:
			print("There are no marbles left. Computer wins!")
			return
		marbles_in_jar = cpu_turn(marbles_in_jar_after_user)
		if marbles_in_jar == 0:
			print("There are no marbles left. You win!")
			return

def your_turn(marbles_in_jar):		
	""" The user begins their turn and will continue their turn until they send in
	a valid input, validated by the function check_valid_input() defined below. 

	It is printed to the console how many marbles were removed, the number of 
	marbles in the jar is updated, and also printed to the console. 

	The number of marbles now in the jar is returned in order to be utilized by 
	the cpu_turn().
	"""
	your_turn = True
	while your_turn == True:
		attempted_grab = raw_input("Your turn: How many marbles will you remove (1-3)? ")		
		your_turn, grabbed = check_valid_input(attempted_grab, marbles_in_jar)
	print("You removed {} marbles".format(attempted_grab))
	marbles_in_jar -= grabbed
	print("Number of marbles left in jar: {}".format(marbles_in_jar))
	return marbles_in_jar

def cpu_turn(marbles_in_jar):
	""" The computer grabs a random integer between 1 and 3, unless taking that quantity
	is impossible (for example, attempting to grab 3 marbles when only 2 exist). In that 
	case, the CPU will take only two. 

	It is printed to the console the number of marbles the CPU took. The number of marbles
	remaining is then computed, printed, and returned for evaluating into the next turn of 
	the user. 
	""" 
	print ("Computer's turn...")
	computer_grab = randint(1, min(3, marbles_in_jar)) 
	print ("Computer removed {} marbles. ".format(computer_grab))
	marbles_in_jar -= computer_grab
	print("Number of marbles left in jar: {}".format(marbles_in_jar))
	return marbles_in_jar 

def check_valid_input(attempted_grab, marbles_in_jar):
	""" This function checks a few possible inputs that would not allow the script to run 
	as it should. For example, if the input is not an integer value, if the user tries to 
	grab more than three marbles, if the user tries to grab no marbles, and if the user 
	tries to grab more marbles than there are in the jar, they will be asked to try again.

	Until proper input is received, the loop will continue (see your_turn() and cpu_turn()
		for the while loop that contains this function.) 
	"""
	try: 
		grabbed = int(attempted_grab)
		if grabbed > 3:
			raise ValueError("Don't be greedy! Try again!")
		elif grabbed == 0:
			raise ValueError("Nice try. Try again!")
		elif marbles_in_jar - grabbed < 0:
			raise ValueError("Sorry, there aren't enough marbles for that...")
	except Exception:
		print("Sorry, that is not a valid option. Try again! ")
		return True, grabbed
	your_turn = False
	return your_turn, grabbed


### Define main() here
def main():
	print("Let's play the game of Seventeen!")
	print("Number of marbles left in jar: 17")
	play_game()
	


### Boilerplate goes here


if __name__ == "__main__":
	main()