#assigning cars number
cars = 100
#assigning space in a car which will be used to find capacity
space_in_a_car = 4
#The total number of drivers
drivers = 30
#The total number of passengers
passengers = 90
#The total number of cars that are not driven at that time
cars_not_driven = cars - drivers
#The total number of car driven
cars_driven = drivers
#The total car pool capacity
carpool_capacity = cars_driven * space_in_a_car
#The total average person per car
average_passengers_per_car = passengers / cars_driven 


print "There are",cars,"cars available"
print "There are only", drivers ,"drivers available"
print "There will be", cars_not_driven , "empty cars today"
print "we can transport", carpool_capacity,"people today"
print "we have", passengers , "to carpool today"
print "we need to put about",average_passengers_per_car,"in each car"
