#! /usr/bin/env python
# 

### Imports go here



### Body goes here:
"""The len_list() function works for counting
the length of a list, a string, a tuple, a dictionary!
"""
def len_list(l):
	count = 0
	for i in l:
		count += 1
	return count

## Define main() here:
def main():
	print len_list(["s", "o", "n"])
	print len_list("blah")


## Bootstrap here:

if __name__ == "__main__":
	main()