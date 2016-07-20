ten_things = " Apples Oranges Crows Telephone Light Sugar"

print " Wait there are not 10 things int the list lets fix this"

stuff = ten_things.split(' ')
more_stuff = [ "Day" , "Night" , "Song" , "Frisbee" , "Corn" , "Banana" , "Girl" , "Boy"]

while len(stuff) != 10:
    #similar to pop more stuff   
    next_one=more_stuff.pop()
    print "adding", next_one
    stuff.append(next_one)
    print "There are %d items to show"% len(stuff)
    
print "There we go",stuff

print "Lets do some other stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:6])
