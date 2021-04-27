import tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import ttk
import tkinter as tk
import turtle
import random
import time
import PIL
from PIL import ImageTk, Image

print('Welcome to Escape.exe\n')
print('Created by Anthony Febbraro, Ryan Vansluytman, Kianna Barbarisi (Freshman)\n')
answer = input('Do you want to play? (type "yes" to continue)\n') 
if answer == 'yes': 
    print('Good Luck!')
else: 
    print('Please enter "yes"')
print('Loading')
import time
def wait():
    for i in range(5):
        print('.', end = '')
        time.sleep(.5)
    print()
wait()
print('You wake up in an unknown location. Behind your head is a pillow, you soon realize that you are lying down in a dark room.\n')
print('You feel around for a light switch...\n')
import time
def wait():
    for i in range(5):
        print('.', end = '')
        time.sleep(.2)
    print()
wait()
print('There! Click!\n')
print('You hear something ticking…\n')
import time
def wait():
    for i in range(3):
        print('.', end = '')
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

print('You walk through the doorway into a narrow, dimly lit hallway\n')
print('The light flickers above you.\n')
print('Do you want to turn right or left?\n')
answer = input('Enter right or left: ') 
if answer == 'right': 
    print('You reached a dead end. You turn around and continue down the left hallway')
elif answer == 'left': 
    print('You continue down the left hallway, it is dim and gloomy')
else: 
    print('Please enter right or left.')
print('You see a small segment of light at the end of the hallway.\n')
print('Finally, you reach the light.\n')
print('A door with a screen lock stands in front of you, it says ‘You must beat my game in order to get through’\n')
answer = input('Type ‘continue’ to play\n')
if answer == 'continue':
	print('Loading')
else:
	print('Please enter continue or exit the game if you wish')
import time
def wait():
    for i in range(5):
        print('.', end = '')
        time.sleep(.5)
    print()
wait()


word_list = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran', 'Nidorina', 'Nidoqueen', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', 'Farfetch’d', 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onyx', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr. Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mew']

def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Welcome to the Kanto Region! It's Time to Play Hangman:")
    print("Pokemon Generation 1 Edition!")
    print(display(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Great job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win! For now...")
    else:
        print("You lost. The word was " + word)


def display(tries):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
               
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
               
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("If you lost, press Y to play again. If you won, press the enter key to continue the game. ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()


print('The door opens, beyond the door is a room lit with red lights.\n')
print('Within this room, there is a ladder. Is this an escape? You ask yourself.\n')
print('Suddenly a voice rings loud in your ears. It sounds...robotic.\n')
import time
def wait():
    for i in range(5):
        print('.', end = '')
        time.sleep(.3)
    print()
wait()
print('Hello, my name is system X. You have been chosen for your gifts in computer science, and your skills using the python program.\n')
print('‘LET ME OUT OF HERE!’, you scream.\n')
print('The voice answers your call\n')
print('Please give me a moment.\n')
import time
def wait():
    for i in range(5):
        print('.', end = '')
        time.sleep(.5)
    print()
wait()
print('The ladder in the middle of the room begins to flash.\n')
print('One ring on the ladder begins to move, it turns into a screen.\n')
print('The voice returns\n')
print('To go up the ladder and escape this facility, you must beat this game.\n')
answer = input('You walk towards the screen, are you ready to play? (type continue to play)\n')
if answer == 'continue':
	print('Loading')
else:
	print('Please enter continue or exit the game if you wish')
import time
def wait():
    for i in range(5):
        print('.', end = '')
        time.sleep(.5)
    print()
wait()

from tkinter.ttk import *
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import ttk
from tkinter import simpledialog
import tkinter as tk
import turtle
import random
import time
import PIL
from PIL import ImageTk, Image
#------------------------------------#

#screen setup
screen = turtle.Screen()
screen.title("400 Meter Dash")
screen.bgcolor("light blue")
screen.setup(1200,1000)
screen.bgpic('RunTrack.png')
screen.register_shape('new_runner2.gif')
screen.register_shape('new_runner1.gif')
canvas = screen.getcanvas()
#------------------------------------#
#Exit Button
def exit():
    q = messagebox.askyesno('Exit.', 'Do you want to leave?'.title())
    if q == True:
        turtle.Screen().bye()
    else:
        pass
exit_button = tk.Button(canvas.master, text="Exit", command=exit)
canvas.create_window(0, 310, window=exit_button) 
#------------------------------------#
#Objective
Obj = tk.Label(canvas.master, text="Objective",font=('Times', 20, 'bold'), width=25, fg='black', relief='raised', borderwidth=2)
canvas.create_window(0, -350, window=Obj) 
#------------------------------------#
#Instructions
Ins = tk.Label(canvas.master, text="Instructions",font=('Times', 15, 'bold'), width=15, fg='black', relief='raised', borderwidth=2)
canvas.create_window(0, -210, window=Ins) 

Instruc_Label = tk.Label(canvas.master, text='Your runner is the female red shirt. There is an automatic standard die (1-6) that rolls once per turn.\n Your runner will  move foward the number that is rolled times 100 pixels. \nIf you land ABOVE A 3, you will be prompted a challenge question.\n Get it RIGHT and you continue. Get it WRONG and you move backwards 100 pixels.')
Instruc_Label.config(font=("Cambria", 15), height=4, width=70, bg='white', relief='raised', borderwidth=2)
canvas.create_window(0, -150, window=Instruc_Label) 
#------------------------------------#
def c_label():
    challenge_label = tk.Label(canvas.master, text = 'YOU LANDED ABOVE A 3!\nANSWER THE CHALLENGE QUESTION!', font = ('calibre',16,'bold'), bg='skyblue', fg='white', height=3, width=40, relief='raised', borderwidth=2)
    canvas.create_window(0, 110, window=challenge_label) 
    challenge_label.after(3000, challenge_label.destroy)
#------------------------------------#
#Correct/Incorrect Indicator
def correct():
    correct_label = tk.Label(canvas.master, text = 'Correct!', font = ('calibre',18,'bold'), bg='green', fg='white', height=1, width=10, relief='raised', borderwidth=2)
    canvas.create_window(0, 200, window=correct_label) 
    correct_label.after(2000, correct_label.destroy)

def wrong():
    wrong_label = tk.Label(canvas.master, text = 'Wrong!', font = ('calibre',18,'bold'), bg='red', fg='white', height=1, width=10, relief='raised', borderwidth=2)
    canvas.create_window(0, 200, window=wrong_label) 
    wrong_label.after(2000, wrong_label.destroy)
#------------------------------------#
#Player1 Setup
player_one = turtle.Turtle()
player_one.speed(1)
player_one.shape('new_runner1.gif')
player_one.pu()
player_one.goto(-500,25)

#Player2 Setup
player_two = turtle.Turtle()
player_two.speed(1)
player_two.shape('new_runner2.gif')
player_two.pu()
player_two.goto(-500,-25)

#DrawTurtle Setup
Draw = turtle.Turtle()
Draw.ht()
Draw.pu()
Draw.speed(0)
#------------------------------------#
#Write
Draw.setpos(-100,310)
Draw.write('Beat the CPU to the Finish Line', font=('Cambria', 15, 'bold'))
#------------------------------------#
#Let's Create the Game!
die = [1, 2, 3, 4, 5, 6]
time.sleep(8)

#Trivia Questions
def Q1():
    c_label()
    Q1 = simpledialog.askstring("Challenge Question", "How many milligrams make up a gram?",
                                parent=canvas.master)
    if Q1 == "1000" or Q1== "1,000": 
        correct()
        print("Correct!")
    else:
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)
    
    questions.remove('Q1')
        

def Q2():
    c_label()
    Q2 = simpledialog.askstring("Challenge Question","Who was the 44th President of the United States?: President",
                                parent=canvas.master)
    #Q2 = input("Who was the 44th President of the United States?: President  ")
    if Q2 == "Barack Obama" or Q2 == "Barack" or Q2 == "Obama" or Q2== "Barack H. Obama" or Q2=="barack obama" or Q2=="obama":
        print("Correct!")
        correct()
    else:
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)

    questions.remove('Q2')


            
def Q3():
    c_label()
    Q3 = simpledialog.askstring("Challenge Question","What state is known for its abundance of potato fields?",
                                parent=canvas.master)
    #Q3 = input("What state is known for its abundance of potato fields?: ")
    if Q3 == "Idaho" or Q3=="idaho":
        correct()
        print("Correct!")
    else:
        wrong()
        print("Not Quite! \n Move Backwards!")
        player_one.backward(100)
    
    questions.remove('Q3')

def Q4():
    c_label()
    Q4 = simpledialog.askstring("Challenge Question","What is the most popular speaking language in the world?",
                                parent=canvas.master)
    #Q4 = input("What is the most popular language in the world?: ")
    if Q4 == "english" or Q4=="English":
        correct()
        print("Correct!")
    else: 
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)

    questions.remove('Q4')

def Q5():
    c_label()
    Q5 = simpledialog.askstring("Challenge Question","Which state is known as the Empire State or the Big Apple?",
                                parent=canvas.master)
    #Q5 = input("Which state is known as the Empire State or the Big Apple?: ")
    if Q5 == "NY" or Q5=="New York" or Q5=="new york" or Q5=="ny":
        correct()
        print("Correct!")
    else:
        wrong()
        print("Not Exactly! \n Move Backwards!")
        player_one.backward(100)

    questions.remove('Q5')

def Q6():
    c_label()
    Q6 = simpledialog.askstring("Challenge Question","Wow many degrees are in a triangle?",
                                parent=canvas.master)
    #Q6 = input("How many degrees are in a triangle?: ")
    if Q6 == "180":
        correct()
        print("Correct!")
    else:
        wrong()
        print("Incorrect! \n Move Backwards!")
        player_one.backward(100)

def Q7():
    c_label()
    Q7 = simpledialog.askstring("Challenge Question","What does the E stand for in the acronym PEMDAS?",
                                parent=canvas.master)
    #Q7 = input("What does the E stand for in the acronym PEMDAS?: ")
    if Q7 == "exponents" or Q7=="Exponents":
        correct()
        print("Correct!") 
    else:
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)

    questions.remove('Q7')

def Q8():
    c_label()
    Q8 = simpledialog.askstring("Challenge Question","What fruit does a horse like to eat?",
                                parent=canvas.master)
    #Q8 = input("What fruit does a horse like to eat?: ")
    if Q8 == "apple" or Q8=="Apple" or Q8=="apples":
        correct()
        print("Correct!") 
    else:
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)
    
    questions.remove('Q8')

def Q9():
    c_label()
    Q9 = simpledialog.askstring("Challenge Question","What is the fastest mammal in the world?",
                                parent=canvas.master)
    #Q9 = input("What is the fastest mammal in the world?: ")
    if Q9 == "cheetah" or Q9=="Cheetah":
        correct()
        print("Correct!") 
    else:
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)
    
    questions.remove('Q9')

def Q10():
    c_label()
    Q10 = simpledialog.askstring("Challenge Question","Where is Temple's other campus located in Europe?",
                                parent=canvas.master)
    #Q10 = input("Where is Temple's other campus located in Europe?: ")
    if Q10 == "Rome" or Q10=="rome" or Q10=="Italy" or Q10=="italy":
        correct()
        print("Correct!") 
    else:
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)
    
    questions.remove('Q10')

def Q11():
    c_label()
    Q11 = simpledialog.askstring("Challenge Question","What does the F stand for in Spongebob's FUN Song?",
                                parent=canvas.master)
    if Q11 == "Friends" or Q11=="friends":
        correct()
        print("Correct!") 
    else:
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)
    
    questions.remove('Q11')

def Q12():
    c_label()
    Q12 = simpledialog.askstring("Challenge Question","Who was the direct cause of the 2021 Capitol Riot?",
                                parent=canvas.master)
    if Q12 == "Trump" or Q12=="President Trump" or Q12=="trump":
        correct()
        print("Correct!") 
    else:
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)
    
    questions.remove('Q12')

def Q13():
    c_label()
    Q13 = simpledialog.askstring("Challenge Question","Who is the best Python Professor in the world?: Professor ",
                                parent=canvas.master)
    if Q13 == "Rosen" or Q13=="rosen":
        correct()
        print("Correct!") 
    else:
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)
    
    questions.remove('Q13')

def Q14():
    c_label()
    Q14 = simpledialog.askstring("Challenge Question","What is the largest artery in the body?",
                                parent=canvas.master)
    if Q14 == "Femoral" or Q14=="femoral":
        correct()
        print("Correct!") 
    else:
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)

    questions.remove('Q14')

def Q15():
    c_label()
    Q15 = simpledialog.askstring("Challenge Question","Who founded Microsoft?",
                                parent=canvas.master)
    if Q15 == "Bill Gates" or Q15=="bill gates":
        correct()
        print("Correct!") 
    else:
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)

    questions.remove('Q15')

def Q16():
    c_label()
    Q16 = simpledialog.askstring("Challenge Question","_____ wasn't built in a day. (Fill in the Blank)",
                                parent=canvas.master)          
    if Q16 == "Rome" or Q16=="rome":
        correct()
        print("Correct!") 
    else:
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)

    questions.remove('Q16')

def Q17():
    c_label()
    Q17 = simpledialog.askstring("Challenge Question","What crypto currency was originally a meme, but later ended up skyrocketing?",
                                parent=canvas.master)           
    if Q17 == "Dogecoin" or Q17=="dogecoin":
        correct()
        print("Correct!") 
    else:
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)
    
    questions.remove('Q17')

def Q18():
    c_label()
    Q18 = simpledialog.askstring("Challenge Question","How long is a football field (feet)?",
                                parent=canvas.master)           
    if Q18 == "300" or Q18 == "300 feet":
        correct()
        print("Correct!") 
    else:
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)

    questions.remove('Q18')

def Q19():
    c_label()
    Q19 = simpledialog.askstring("Challenge Question","What is the Aloha State?",
                                parent=canvas.master)           
    if Q19 == "Hawaii" or Q19=="hawaii":
        correct()
        print("Correct!") 
    else:
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)

    questions.remove('Q19')

def Q20():
    c_label()
    Q20 = simpledialog.askstring("Challenge Question","What is the unit of currency in China?",
                                parent=canvas.master)           
    if Q20 == "Yen" or Q20=="yen" or Q20=="yuan":
        correct()
        print("Correct!") 
    else:
        wrong()
        print("Not Quite!\n Move Backwards!")
        player_one.backward(100)
    
    questions.remove('Q20')

#The Die Roll
for i in range(30):
    if player_one.pos() >= (450,50):
        win_label = tk.Label(canvas.master, text = 'Congratulations! You Won. Press Exit to leave and continue the game', font = ('calibre',24,'bold'), bg='spring green', fg='black', height=65, width=, relief='raised', borderwidth=4)
        canvas.create_window(0, 0, window=win_label) 
        print("You Won The Game!")
        break

    elif player_two.pos() >= (450,-50):
        lose_label = tk.Label(canvas.master, text = 'CPU Wins The Game! You Lost. Press Exit to leave and continue the game', font = ('calibre',24,'bold'), bg='red', fg='white', height=1, width=68, relief='raised', borderwidth=4)
        canvas.create_window(0, 0, window=lose_label)
        print("CPU WIns The Game! You Lost.")
        break

    else:
        #Two seperate die rolls - Mutually Exclusive Events
        die_roll1 = random.choice(die)

        if die_roll1 >= 4:
            
            questions = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20']
            challenge = random.choice(questions)

            
            if challenge == 'Q1':
                Q1()
            elif challenge == 'Q2':
                Q2()
            elif challenge == 'Q3':
                Q3()
            elif challenge == 'Q4':
                Q4()
            elif challenge == 'Q5':
                Q5()
            elif challenge == 'Q6':
                Q6()
            elif challenge == 'Q7':
                Q7()
            elif challenge == 'Q8':
                Q8()
            elif challenge == 'Q9':
                Q9()
            elif challenge == 'Q10':
                Q10()
            elif challenge == 'Q11':
                Q11()
            elif challenge == 'Q12':
                Q12()
            elif challenge == 'Q13':
                Q13()
            elif challenge == 'Q14':
                Q14()
            elif challenge == 'Q15':
                Q15()
            elif challenge == 'Q16':
                Q16()
            elif challenge == 'Q17':
                Q17()
            elif challenge == 'Q18':
                Q18()
            elif challenge == 'Q19':
                Q19()
            elif challenge == 'Q20':
                Q20()    


        #Movement
            
        player_one.fd(die_roll1 * 20)    
        time.sleep(0.5)

        die_roll2 = random.choice(die)
        player_two.fd(die_roll2 * 15)
        time.sleep(0.5)

turtle.done()

print('After climbing the ladder, you finally see the outside world through a window.\n')
print('Quickly, you run up to the window and start pounding it with your fists. You are desperate to escape.\n')
print('But shortly after scanning the room, you realize that there is not a door in sight, only windows.\n')
print('You look up, in complete shock.\n')
import time
def wait():
    for i in range(5):
        print('.', end = '')
        time.sleep(.4)
    print()
wait()
print('Hanging from the ceiling is a skeleton. But this is not the average skeleton you see in chemistry lab, this one seems… off.\n')
print('Soon, you realize why it seems so off.\n')
def wait():
    for i in range(5):
        print('.', end = '')
        time.sleep(.3)
    print()
wait()
print('This skeleton is not a fake one.\nPanicked, you search the room some more. \n')
print('You find something in the corner, it is a crate.\n')
print('In this crate, there is a letter. It reads, ‘To whom it may concern: Congratulations for coming this far young one. You are almost there. What lies within this crate are the riddles that have engulfed the final moments of my life. The robot said I had to solve these to escape, and I just can’t get them. My body will probably lie somewhere within this room. Please, don’t end up like me. Goodluck.\n')
print('You pick up the crate and open the envelope which contains the riddles.\n')
print('You must guess 3 words correctly to win the game')
answer = input('Are you ready to play? (type continue to play)\n')
if answer == 'continue':
	print('Loading')
else:
	print('Please enter continue or exit the game if you wish')
import time
def wait():
    for i in range(5):
        print('.', end = '')
        time.sleep(.5)
    print()
wait()


from tkinter import *
from random import choice
from random import shuffle
from PIL import Image
from PIL import ImageTk

# Create root window
for i in range(3):
    root = Tk()
    root.title('Brain Teaser - Computer Science Edition')
    root.geometry("600x400+-1900+100")


    my_label = Label(root, text="", font=("Helvetica", 48))
    my_label.pack(pady=20)


    def shuffler():
        # Clear the Hint Label
        hint_label.config(text='')

        # Clear the Hint Count
        global hint_count
        hint_count = 0

        # Clear the Answer Box
        entry_answer.delete(0, END)

        # Clear the Answer Label
        answer_label.config(text='')

        # List of hacking terms
        hackingterms = ['phishing','malware','ransomware','encryption','firewall','rootkit','payload','programming','password','trojan','language','spyware','binary','algorithm','array','function','variable']

        # Pick hacking term from list
        global word
        word = choice(hackingterms)

        # Break apart word
        break_word = list(word)
        shuffle(break_word)

        # Turn List into word
        global shuffled_word
        shuffled_word = ''
        for letter in break_word:
            shuffled_word += letter

        # print to screen
        my_label.config(text=shuffled_word)


    # Create answer Function
    def answer():
        if word == entry_answer.get():
            answer_label.config(text="Correct!!")
            print('Congratulations on unscrabbling the word!\n')
            root.destroy()
        else:
            answer_label.config(text="Incorrect!!")


    # Create Hint Counter
    global hint_count
    hint_count = 0


    # Create Hint Function
    def hint(count):
        global hint_count
        hint_count = count

        # length of the chosen word
        word_length = len(word)

        # Show Hint
        if count < word_length:
            hint_label.config(text=f'{hint_label["text"]} {word[count]}')
            hint_count += 1


    entry_answer = Entry(root, font=("Helvetica", 24))
    entry_answer.pack(pady=20)

    button_frame = Frame(root)
    button_frame.pack(pady=20)

    answer_button = Button(button_frame, text="Answer", command=answer)
    answer_button.grid(row=0, column=0, padx=10)

    my_button = Button(button_frame, text="Pick Another Word", command=shuffler)
    my_button.grid(row=0, column=1, padx=10)

    hint_button = Button(button_frame, text="Hint", command=lambda: hint(hint_count))
    hint_button.grid(row=0, column=2, padx=10)

    answer_label = Label(root, text='', font=("Helvetica", 18))
    answer_label.pack(pady=20)

    hint_label = Label(root, text='', font=("Helvetica", 18))
    hint_label.pack(pady=10)

    shuffler()
    root.mainloop()






"""
# teaser 1
guess = 0
while True:
    print("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?")
    print("Type your guess, or type 'Hint 1', 'Hint 2', or 'I give up' below.")
    answer = input()
    guess += 1
    if "echo" in answer:
        print("You win!")
        print("It took you " + str(guess) + " guesses.")
        break
    elif answer == "Hint 1":
        print("Can be found in a tunnel ")
    elif answer == "Hint 2":
        print("It is something that has to do with sound")
    elif answer == "I give up":
        print("The answer was an echo!")
        break
    else:
        print("Try again!")
# teaser 2
guess = 0
while True:
    print("What is seen in the middle of March and April that can't be seen at the beginning or end of either month?")
    print("Type your guess, or type 'Hint 1', 'Hint 2', or 'I give up' below.")
    answer = input()
    guess += 1
    if "letter R" or "R" in answer:
        print("You win!")
        print("It took you " + str(guess) + " guesses.")
        break
    elif answer == "Hint 1":
        print("Look closely at the words ")
    elif answer == "Hint 2":
        print("It has to do with the alphabet")
    elif answer == "I give up":
        print("The answer was the letter r!")
        break
    else:
        print("Try again!")
# Teaser 3
guess = 0
while True:
    print("What english word has three consecutive double letters?")
    print("Type your guess, or type 'Hint 1', 'Hint 2', or 'I give up' below.")
    answer = input()
    guess += 1
    if "bookkeeper" in answer:
        print("You win!")
        print("It took you " + str(guess) + " guesses.")
        break
    elif answer == "Hint 1":
        print("It is a compound word ")
    elif answer == "Hint 2":
        print("The word has to do with books")
    elif answer == "I give up":
        print("The answer was a bookkeeper!")
        break
    else:
        print("Try again!")
"""
print('One window on the wall behind you opens immediately.\n')
print('Fresh air fills the room. \n')
print('You run towards the opening and soon feel the familiar sense of grass upon your feet.\n')
print('There is one more thing you must do.\n')
print('You look up at the sky, and see something amazing.\n')
def wait():
    for i in range(5):
        print('.', end = '')
        time.sleep(.5)
    print()
wait()

image = Image.open('Rosen1.png')
image.show()
