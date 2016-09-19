import random
guess_made = 0
number = random.randint(1,20)
print "%d"%(number)
while guess_made < 3:
	guess = int(raw_input("Take a guess between 1 and 20 :"))
	guess_made=guess_made+1
	
	if  guess == number:
		print "Congrats! The number Guessed is Right"
		break

	if  guess < number:
		print "The Guess is too low"
	
	if  guess > number:
		print "The Guess is too High"
	
