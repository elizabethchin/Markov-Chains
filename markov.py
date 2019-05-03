"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
	"""Take file path as string; return text as string.

	Takes a string that is a file path, opens the file, and turns
	the file's contents as one string of text.
	"""

	# your code goes here

	open_file = open(file_path)
	file_as_string = open_file.read()


	return file_as_string


def make_chains(text_string):
	"""Take input text as string; return dictionary of Markov chains.

	A chain will be a key that consists of a tuple of (word1, word2)
	and the value would be a list of the word(s) that follow those two
	words in the input text.

	For example:

		>>> chains = make_chains("hi there mary hi there juanita")

	Each bigram (except the last) will be a key in chains:

		>>> sorted(chains.keys())
		[('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

	Each item in chains is a list of all possible following words:

		>>> chains[('hi', 'there')]
		['mary', 'juanita']
		
		>>> chains[('there','juanita')]
		[None]
	"""

	chains = {}
	the_list = []


	split_list = text_string.split()

#make list of 3rd value
	for i in range(len(split_list) - 2):
		key = (split_list[i], split_list[i + 1])
		value = split_list[i + 2]
		if key not in chains:
			chains[key] = []

		the_list.append(value)
#make the keys
	# for i in range(len(split_list) - 1):
	# 		dic_key = (split_list[i], split_list[i + 1])
	# 		chains[dic_key] = [] 
	# print(chains)

		#chains[dic_key] = []
		#print(chains)

#makes keys and values
	for i in range(len(split_list) - 2):
		key = (split_list[i], split_list[i + 1])
		va =  split_list[i + 2]
		chains[key] = []



	    	



	


	return chains


def make_text(chains):
	"""Return text from chains."""

	words = []

	# your code goes here

	return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
