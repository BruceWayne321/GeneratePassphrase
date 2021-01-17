
import random 

print("Hey, what type of passphrase would you like?\nAlphabetical, Numeric, special char or mixed\n")
print("for Alphabetical, press 1")
print("for Numeric, press 2")
print("for special char, press 3")
print("for mixed, press 4")

'''
here we are gonna decide the type of our passphrase
'''

while True:
	type = int(input("\nPRESS ANY KEY: "))
	if type > 4  or type < 1:
		print("plz enter a right key")
		continue
	else:
		print('\n' , type , "it is")
		break

'''
here we are gonna decide the length of our passphrase
'''
print("\nwhat length would you like your passphrase to be?")
print("8-16 is acceptable")

while True:
	length = int(input("\nPRESS ANY KEY: "))
	if length > 16 or length < 8 :
		print("plz enter a right key")
		continue
	else:
		print('\n' , length , "it is\n")
		break

'''
here we are defining our characters
'''

#if you just want lower-case letters then uncomment this out
#alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

#if you dont want lower-case as well as upper-case letters then comment this out
alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
'''
here I am creating a class thats gonna generate our passphrase
'''
class gen_passphrase():
	'''
	here I am just defining types(i have no idea why i did it but it works fine)
	'''
	def type(self):
		alphabetical = self.alphabetical
		numerical = self.numerical
		special = self.special
		mixed = self.mixed
	'''
	here we are just creating passphrase with just alphabets in it
	'''
	def alphabetical():
		passphrase = ""
		for l in range(length):
			p = random.choice(alphabet)
			passphrase += p
		print(passphrase)
	'''
	here we are just creating passphrase with just numbers in it
	'''
	def numerical():
		passphrase = ""
		for l in range(length):
			p = str(random.choice(number))
			passphrase += p
		print(passphrase)
	'''
	here we are just creating passphrase with just special characters in it
	'''
	def special():
		passphrase = ""
		for l in range(length):
			p = random.choice(special_char)
			passphrase +=p
		print(passphrase)
	'''
	here we are just creating passphrase with all types of characters in it
	'''
	def mixed():
		passphrase = ""
		for l in range(length):
			t = [alphabet, number, special_char]
			t = random.choice(t)
			p = str(random.choice(t))
			passphrase += p
		print(passphrase)

'''
here i am calling funtions as per the request of the user
'''
if type == 1:
	gen_passphrase.alphabetical()
elif type == 2:
	gen_passphrase.numerical()
elif type == 3:
	gen_passphrase.special()
elif type == 4:
	gen_passphrase.mixed()
else:
	print("THis cAn neVEr HaPpeN!!")
'''
I wrote the else statement because i think that can never happen, who knows (;
'''
