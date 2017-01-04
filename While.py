def loop(a,b):
    #intiliasing i to 0 
    i = 0
    #creating a list
    numbers = []
    #using while loop with condition
    for i in range(0,6,b):
    #while i < a:
        print "at the i is %d "% i
        #using append function
        numbers.append(i)
        #incrementing the loop
    #    i=i+b
        print "Numbers now",numbers
        print "at the bottom i is %d"%i
    
    #printing numbers
    print "The numbers:"

    for num in numbers:
        print num 
    

loop(9,5)    
