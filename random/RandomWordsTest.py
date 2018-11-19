
#from random_word import RandomWords
import string
import random

class RandomWordsTest:

	def __init__(self):
		print("Construtor")



	#def generate(self):
	#	print("generate")
		#r = RandomWords()

		# Return a single random word
		#r.get_random_word()
		# Return list of Random words
		#r.get_random_words()
		# Return Word of the day
		#r.word_of_the_day()


	def random_generator(self, size):
		chars=string.ascii_uppercase + string.digits
		return ''.join(random.choice(chars) for x in range(size))



m = RandomWordsTest()
m.generate()
text = m.random_generator(6)
#text = m.random_generator(3, "6793YUIO")

print(text)

