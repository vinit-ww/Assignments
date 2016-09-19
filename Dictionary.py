#mapping states to abbreviation
states={
        'Maharastra'  : 'MH',
        'Uttrakhand'  : 'Uk',
        'Delhi'       : 'DL',
        'Rajasthan'   : 'RJ'
}
#creating a basic set of states and some cities in them
cities={
        'Uk'   : 'Dehradun',
        'DL'   : 'Delhi6',

}
#add more cities
cities['MH'] = 'Mumbai'
cities['RJ'] = 'Jodhpur'

print cities
#print out some cities
print '-'*10
print "UK state has: city",cities['Uk']
print "DL state has: city",cities['DL']

#print some states
print '-'*10
print "Maharastra abbreviation is",states['Maharastra']
print "Delhi abbreviation is",states['Delhi']

#doing by using states than cities
print '-'*10
print "MH state has city",cities[states['Maharastra']]
print "Uk state has: city",cities[states['Uttrakhand']]

#print every state annreviation
print '-'*10
for state,abbvr in states.items():
    print "%s is abbreviated as %s"%(state,abbvr)
    
#print every cities in state

print '-'*10
for abbrv,city in cities.items():
    print "%s has city %s"%(abbrv,city)

#now do both at the same time
print '-'*10
for abbvr,state in states.items():
    print "%s is %s and has city "%((abbvr,state))
    
#safetly get a abbreviation if state is not there
state = states.get('Texas')

if not state:
    print "Sorry no Texas"

#get a city with default value

city = cities.get('TX','Does Not Exsist')
print "The city for the state 'TX' is:%s"%city    
    
