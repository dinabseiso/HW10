def make_lists(number):
	""" This list comprehension (yes!) is implemented to create a list 
	where every item is an integer form of an index within the passed in
	string or number.
	"""
	string_version_of_number = str(number)
	return [int(digit) for digit in string_version_of_number]


def cows_and_bulls(guess, random_number):
	""" This function pulls a list of numbers from the make_lists() above
	in order to evaluate index by index whether there is a match (a bull). 
	It counts all True hits in a list of tuples (the product of zip()), to see
	whether the two values in the tuple match.

	It then enters a for loop that iterates through the set of characters in guess_list.
	set() only maintains unique values. So, for example, if there are duplicate
	integers or characters, only one will be represented in the set. set([1, 2, 2]) will 
	return [1, 2]. So, for every digit in this set, it will take the minimum number 
	of matches found in either the guessed value or the randomly generated value. We take
	the minimum of the two because unless we have a complete match between guessed value and
	the randomly generated one, we will have the most matches between the set that originates
	from the guessed value than with our randomly generated value. The only time when this is
	not true is when our randomly generated number contains many duplicate integers, which 
	is why we have the min() function as well. The total number of matches (this includes bulls)
	is cumulatively summated. If we did not have min(guess_list.count(digit)), and instead had 
	evertthing else exclusively, we would run into a problem where it says we have cows when
	we really do not have any cows at all.

	Because we calculated the total number of cows and bulls, we want to subtract bulls in 
	order to get our count of cows. 

	We return the counts as a tuple. 
	"""
	
	guess_list, random_number_list = make_lists(guess), make_lists(random_number)
	bull_count = [digit1 == digit2 for digit1, digit2 in zip(guess_list, random_number_list)].count(True)
	cows_and_bulls = 0
	for digit in set(guess_list):
		cows_and_bulls += min(guess_list.count(digit), random_number_list.count(digit))
	cow_count = cows_and_bulls - bull_count
	return bull_count, cow_count
