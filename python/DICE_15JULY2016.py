import random
i = 0;
choice = raw_input('Do you Want to Generate random number 1 for yes 0 for No')
while choice != 0:
	if( choice != 0 ):
	   number=random.randint(1,6)
	   print "The Outcome is %d" %(number)
    	   choice = raw_input('Do You Want to Generate random number 1 for yes 0 for No')
	if( choice != 0 ):
	   continue
		
