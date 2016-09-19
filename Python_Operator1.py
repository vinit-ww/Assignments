people = 30
cars = 28
trucks = 30


if cars > people or cars < trucks:
    print "We should take cars"
elif cars < people:
    print "We should not take cars"
else:
    print "We can't decide"
    
if trucks > cars and cars > people:
    print "Thats too many trucks"
elif trucks > cars:
    print "maybe we should take the trucks"
else:
    print "we cant decide"
    
if  people> cars:
    print "Alright let's just take trucks"
else:
    print "Fine let's stay home"
