import tkinter
import random
print(“Welcome to Escape.exe, do you want to play?\n”)
print('Loading')
import time
def wait():
    for i in range(5):
        print('.', end = "")
        time.sleep(.5)
    print()
wait()
print(“You wake up in an unknown location. Behind your head is a pillow, you soon realize that you are lying down in a dark room.\n”)
print(“You feel around for a light switch...\n”)
print('Loading')
import time
def wait():
    for i in range(5):
        print('.', end = "")
        time.sleep(.5)
    print()
wait()
print(“There! Click!\n”)
print(“You hear something ticking…\n”)
print('Loading')
import time
def wait():
    for i in range(5):
        print('.', end = "")
        time.sleep(.5)
    print()
wait()

places = ["under the bed", "inside the pillowcase", "behind the alarm clock", 
    "on the windowsill", "inside the dresser", "under the sheets", 
    "inside the closet", "under the rug", "on the nightstand", "behind the painting"]

possible = [True, False]

hidingplace = random.choice(places)  
    
print ("You see a timer on the wall of the room.")
print ("You get up and read the numbers on the timer, it is counting down.")
print ("You must hurry! You have 80 seconds to find the key and escape the room")
print ("")

print (places[:3])
print (places[3:6])
print (places[6:10])
print ("")

def findTheKey():
    global hidingplace
    num = 80
    seconds = input("Guess a hiding spot: ")
    images(seconds)
    
    while num > 0:  
            
        if seconds == hidingplace:
                print ("You found a key!")
                done = input("Type 'continue' to use the key\n")
                
                    
                if done == "continue":
                    print ("You quickly walk towards the door and turn the key, it opens.")
                    break
                
            
        if seconds != hidingplace:
            if num == 50:
                move = random.choice(possible)
                if move == True:
                    print ("You feel a mysterious prescence is in the room with you, it decides to move the key to another location, even if you may have guessed it before!")
                    print("Time feels... weird. The alarm clock is reset to 80 seconds.\n")
                    hidingplace = random.choice(places)
                    num = num + 40
                    
            if seconds not in places:
                print ("Must be within the list.")
                seconds = input("Guess a hiding spot: ")
                images(seconds)
                
            else:    
                num = num - 10
                print ("The key is not here! Keep Looking!")
                print ("The timer on the wall continues to count down. " + str(num) + " seconds left!")
                print ("")
                
                seconds = input("Guess a hiding spot: ")
                images(seconds)
        
        
        
          
def images(seconds):
    if seconds == "under the bed":   
        print ("   ______  ")
        print ("  |    | | ")
        print ("  |____|_| ")
        print ("")

    if seconds == "inside the pillowcase":
        print ("  ____ ")
        print (" |    | ")
        print (" |____| ")
        print ("")
    
    if seconds == "behind the alarm clock":
        print ("")
        print ("  ______")
        print (" | X  X | ")
        print (" |_X__X_| ")
        print ("")
    if seconds == "on the windowsill":
        print ("  _______")
        print (" |___|___| ")
        print (" |___|___| ")
        print ("")    
        
    if seconds == "inside the dresser":
        print ("    _________    ")
        print ("  _  |     |  _  ")
        print ("  |__|  X  |__|  ")
        print ("")
        
    if seconds == "under the sheets":
        print ("   _______  ")
        print ("  |  /  | | ")
        print ("  |_/___|_| ")
        print ("")
        print ("")
    
    if seconds == "inside the closet":
        print ("")
        
    if seconds == "under the rug":
        print ("  _______ ")
        print (" | X X X | ")
        print (" |_X_X_X_| ")
        print ("")
    
    if seconds == "on the nightstand":
        print ("  _  | ")
        print ("  |__| ")
        print ("")
        
    if seconds == "behind the painting":
        print ("  _______ ")
        print (" | X X X | ")
        print (" | X X X | ")
        print (" | X X X | ")
        print (" | X X X | ")
        print (" |_X_X_X_| ")
        print ("")
       
findTheKey()

print(“You walk through the doorway into a narrow, dimly lit hallway.\n
print(“The light flickers above you.\n”)
print(“Do you want to turn right or left?\n”)
answer = input("Enter right or left: ") 
if answer == "right": 
    print("You reached a dead end. You turn around and continue down the left hallway")
elif answer == "left": 
    print("You continue down the left hallway, it is dim and gloomy")
else: 
    print("Please enter right or left.")
print(“You see a small segment of light at the end of the hallway.\n”)
print(“Finally, you reach the light.\n”)
print(“A door with a screen lock stands in front of you, it says ‘You must beat my game in order to get through’\n”)
answer = input(“Type ‘continue’ to play\n”)
If answer == “continue”:
	print('Loading')
import time
def wait():
    for i in range(5):
        print('.', end = "")
        time.sleep(.5)
    print()
wait()
Else:
	print(“Please enter continue or exit the game if you wish”)
*insert game 2*
print(“The door opens, beyond the door is a room lit with red lights.\n”)
print(“Within this room, there is a ladder. Is this an escape? You ask yourself.\n”)
print(“Suddenly a voice rings loud in your ears. It sounds...robotic.\n”)
print('Loading')
import time
def wait():
    for i in range(5):
        print('.', end = "")
        time.sleep(.5)
    print()
wait()
print(“Hello, my name is system X. You have been chosen for your gifts in computer science, and your skills using the python program.\n”)
print(“‘LET ME OUT OF HERE!’, you scream.\n”)
print(“The voice answers your call\n”)
print(“Please give me a moment.\n”)
print('Loading')
import time
def wait():
    for i in range(5):
        print('.', end = "")
        time.sleep(.5)
    print()
wait()
print(“The ladder in the middle of the room begins to flash.\n”)
print(“One ring on the ladder begins to move, it turns into a screen.\n”)
print(“The voice returns\n”)
print(“To go up the ladder and escape this facility, you must beat this game.\n”)
answer = input(“You walk towards the screen, are you ready to play? (type continue to play)\n”)
If answer == “continue”:
	print('Loading')
import time
def wait():
    for i in range(5):
        print('.', end = "")
        time.sleep(.5)
    print()
wait()
Else:
	print(“Please enter continue or exit the game if you wish”)
*insert game 3*
print(“After climbing the ladder, you finally see the outside world through a window.\n”)
print(“Quickly, you run up to the window and start pounding it with your fists. You are desperate to escape.\n”)
print(“But shortly after scanning the room, you realize that there is not a door in sight, only windows.\n”)
print(“You look up, in complete shock.\n”)
print('Loading')
import time
def wait():
    for i in range(5):
        print('.', end = "")
        time.sleep(.5)
    print()
wait()
print(“Hanging from the ceiling is a skeleton. But this is not the average skeleton you see in chemistry lab, this one seems… off.\n”)
print(“Soon, you realize why it seems so off. This skeleton is not a fake one.\n
print(“Panicked, you search the room some more. \n”)
print(“You find something in the corner, it is a crate.\n”)
print(“In this crate, there is a letter. It reads, ‘To whom it may concern: Congratulations for coming this far young one. You are almost there. What lies within this crate are the riddles that have engulfed the final moments of my life. The robot said I had to solve these to escape, and I just can’t get the last one. My body will probably lie somewhere within this room. Please, don’t end up like me. Goodluck.’\n)
print(“You pick up the crate and open the envelope which contains said riddles.\n”)
answer = input(“Are you ready to play? (type continue to play)\n”)
If answer == “continue”:
	print('Loading')
import time
def wait():
    for i in range(5):
        print('.', end = "")
        time.sleep(.5)
    print()
wait()
Else:
	print(“Please enter continue or exit the game if you wish”)
print(“One window on the wall behind you opens immediately.\n”)
print(“Fresh air fills the room. \n”)
print(“You run towards the opening and soon feel the familiar sense of grass upon your feet.\n”)
print(“There is one more thing you must do.\n”)
print(“You look up at the sky, and see something amazing.\n”)
