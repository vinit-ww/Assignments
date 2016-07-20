the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges' , 'pears' , 'apricots']
change =[1,'pennies',2,'dimes',3,'quarter']

#This is the first kind of for loop
for number in the_count:
    print "the_count is %d"% number
    
#same as above
for fruit in fruits:
    print "A fruit of type:%s"% fruit

#also we can go throug mixed list too
#notice we have to use %r because we dont know whats in it
for i in change:
    print "The list change is %r"% change
    
#we can also built list first start with empty one
elements=[]

#then use the range function to do 0 to 5 counts
for i in range(0,6):
    print "Adding %d to list"% i
    #append is a function that list undrstand
    elements.append(i)
#now we can print them too
for i in elements:
    print i 
