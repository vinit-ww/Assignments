def keywords( x , y ):
    print x == y
    #Error invalid syntax
    #   x as y
    print x
    #Error invalid syntax
    #print "%r" %(assert( x > y))
    del x
    print y
    globvar = 10
    print globvar    
    a = [ 1 , 2 , 3 , 4 , 5]
    print 5 in a
    print True is True
    a = lambda x : x*2
    for i in range( 1 , 6 ):
        print (a(i))
        
def generator():
    for i in range(6):
        yield i * i
        
keywords( 10 , 20 )
#g here is an object
g = generator()
print g
for i in g:
    print i 
