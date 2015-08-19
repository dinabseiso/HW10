#! usr/bin/env python
# numered_lines.py
#

### Import here

### Body here
def numbered_lines(s):
	i = 1
	with open(s) as fin:
		quote = fin.readlines()
			
	with open("small_new.txt", "w") as new_file:
		for line in quote:
			new_file.write("{} {}".format(i, line))
			i += 1 	

### Define main() here
def main():
	numbered_lines("small.txt")


## Boostrap

if __name__ == "__main__":
	main()