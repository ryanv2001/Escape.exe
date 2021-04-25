import random

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
