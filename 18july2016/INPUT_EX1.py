from sys import argv

script , user_name , last_name = argv
prompt = '>'

print "Hi %s, I'm the %s script."%( user_name , script )
print "I'd like you to ask a few question."
print "Do you like me %s ?"% (user_name,last_name)
likes = raw_input(prompt)

print "where do you live %s?"% (user_name,last_name)
lives = raw_input(prompt)

print "What computer do you have %s?"% (user_name,last_name)
computer = raw_input(prompt)

print """
Alright , you said %r about liking me.
you live in %r.Not sure where that is.
and you have a %r computer . Nice""" %( likes , lives , computer )
