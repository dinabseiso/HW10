def get_randomdigit_lastname1lastname2(length):
    # Comment on process
	digits = int(length)
	random_number = randint(1, (10**digits - 1))
	random_number_string = str(random_number)
	random_number_string = random_number_string.zfill(digits)
	# Compute the maximum number of tries allowed.
	max_tries = 2**digits + digits 												
