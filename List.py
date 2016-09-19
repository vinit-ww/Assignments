from sys import exit

def gold_room():
    print "The room is full of gold . how much do you take"
    
    choice=raw_input(">")
    if "0" in choice or "1" in choice:
        how_much=int(choice)
    else:
        dead("man learn to type a number")
        
    if how_much < 50:
        print "Nice , youre not greedy, you win!"
        exit(0)
    else:
        dead("You are greddy")
        
def bear_room():
    print "there is bear there"
    print "the bear has a bunch of honey"
    print "the fat bear is in another door"
    print "how are you going to move the bear"
    bear_moved = False
    
    
    while True:
        choice = raw_input(">")
        
        if choice == "take honey":
            dead("You are not stronger then bear you're smarter")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door and you can go"
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("you are dead")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "No Idea get some Idea"
def some_room():
    print "There is a ghost look directly in his eyes and you die"
    print "do you flee for your life or die head on"
    
    choice = raw_input(">")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Game over")
    else:
        some_room()
        
def dead(why):
    print why
    exit(0)
    
def start():
    print "You are in a dark room\n there is a door at your right and left\nwhich one do you take?"
    choice = raw_input(">")
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        some_room()
    else:
        dead("you stumbled around the room until you are dead")
    
    
start()
        
    
                            
