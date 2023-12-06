from tkinter import *
import random

# Initialize the GUI
rps = Tk()
rps.geometry("400x300")
rps.title("Rock Paper Scissors")

# Define global variables
user_score = 0
comp_score = 0
user_choice = ""
comp_choice = ""

# Functions to convert choices between strings and integers
def choice_to_number(choice):
    rps_dict = {'rock': 0, 'paper': 1, 'scissor': 2}
    return rps_dict[choice]

def number_to_choice(number):
    rps_dict = {0: 'rock', 1: 'paper', 2: 'scissor'}
    return rps_dict[number]

# Function to generate the computer's random choice
def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

# Function to determine the outcome of the game
def result(human_choice, comp_choice):
    global user_score
    global comp_score

    # Convert choices to integers
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)

    # Check for a draw
    if user == comp:
        print("Draw!")

    # Check for a win or loss based on the difference between the choices
    elif (user - comp) % 3 == 1:
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        comp_score += 1

    # Update the text area with the latest information
    text_area = Text(master=rps, font=("arial", 15, "italic bold"), relief=RIDGE, bg="#033642", fg="white", width=26)
    text_area.grid(column=0, row=4)

    answer = "Your choice: {uc} \nComputer's choice: {cc} \nYour score: {u} \nComputer score: {c}".format(
        uc=human_choice,
        cc=comp_choice,
        u=user_score,
        c=comp_score,
    )
    text_area.insert(END, answer)

# Functions for each button choice
def rock():
    global user_choice
    global user_score

    user_choice = "rock"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

def paper():
    global user_choice
    global user_score

    user_choice = "paper"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

def scissor():
    global user_choice
    global user_score

    user_choice = "scissor"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

# Create buttons
button_rock = Button(text="Rock", bg="#808187", font=("arial", 15, "italic bold"), relief=RIDGE,
                     activebackground="#059458", activeforeground="white", width=24, command=rock)
button_rock.grid(column=0, row=1)

button_paper = Button(text="Paper", bg="#808187", font=("arial", 15, "italic bold"), relief=RIDGE,
                     activebackground="#059458", activeforeground="white", width=24, command=paper)
button_paper.grid(column=0, row=2)

button_scissor = Button(text="Scissor", bg="#808187", font=("arial", 15, "italic bold"), relief=RIDGE,
                     activebackground="#059458", activeforeground="white", width=24, command=scissor)
button_scissor.grid(column=0, row=3)

# Start the GUI loop
rps.mainloop()
