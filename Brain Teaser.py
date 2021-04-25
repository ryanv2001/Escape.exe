
from tkinter import *
from random import choice
from random import shuffle
from PIL import Image
from PIL import ImageTk

# Create root window
root = Tk()
root.title('Brain Teaser - Hacking Word Edition')
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
    hackingterms = ['phishing','malware','ransomware','encryption','denial of service','rootkit','social engineering']

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
