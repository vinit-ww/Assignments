#x is a variable who is storing a String
x = "There are %d types of people"% 10
binary = "binary"
do_not = "don't"
#y will get an extracted value of binary and do_not
y = "Those who know %s and Those who know %s"%(binary,do_not)
#x will be printed 
print x
#y will be printed
print y
#it will output the value of string x  but r here has a diffrent purpose
print "I said %r"%x
#using single quotes over %s will also print the string without any error
print "I also said : '%s'. " %y
hilarious = False
joke_evaluation = "Isn't that Joke Funny?!%r"
#It will print concatenated string
print joke_evaluation %hilarious

w = "This is the left side of"
e = " a string with a right side"
#Here + serve the purpose for concatenation
print w+e
