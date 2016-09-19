#using raw_input get input convert it to string and show at output
print "Enter your name :"
name = raw_input()
#using raw_input to get input and explicitly converting it to int both cases are same
print "Enter your phone number :"
number = raw_input()
number = int(number);
print "Enter your pin code :"
pin = int(raw_input())
print "Your name is %s and your phone number is %d and pincode of city is %d "%( name , number , pin)
