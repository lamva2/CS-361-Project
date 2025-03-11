import zmq
import os
import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#####################################################################################################################
# SUBFUNCTIONS AND HELPER FUNCTIONS

def page_input_validation():
    valid_choices = {'0', '1', '2','3', '4', '5'}
    while True:
        user_input = input("Which page would you like to go to? (0, 1, 2, 3, 4, 5): ")
        if user_input in valid_choices:
            return int(user_input)
        else:
            print("Invalid input. Please enter a number between 0 and 5.")

def exit_page_validation(question):
    valid_choices = {'0', '1'}
    while True:
        user_input = input(question)
        if user_input in valid_choices:
            return int(user_input)
        else:
            print("Invalid input. Please enter either 1-yes or 0-no.")

def visualization_validation(question):
    valid_choices = {'bar chart', 'line graph', 'scatter plot'}
    while True:
        user_input = input(question)
        user_input = user_input.lower()
        if user_input in valid_choices:
            return user_input
        else:
            print("Invalid input. Please enter bar chart, line graph, or scatter plot.")
            
def note_validation(question):
    valid_choices = {'0', '1', '2'}
    while True:
        user_input = input(question)
        if user_input in valid_choices:
            return int(user_input)
        else:
            print("Invalid input. Please enter 0, 1, or 2.")

def search_term():
    while True:
        print("Visualization options: Bar chart, Line graph, Scatter plot")
        term = input("Please enter the visualization style you would like to learn about: ")
        socket1.send_string(term)
        definition = socket1.recv_string()
        print(f"Definition: {definition}\n")
        page_input = exit_page_validation("Would you like to search for another term (1-yes, 0-no): ")
        if page_input == 0:
            break

def generate_visual():
    while True:
        print("Visualization options: bar chart, line graph, scatter plot")
        visualization_style = visualization_validation("Please enter your visualization style: \n")
        ask_again = exit_page_validation(f"Running data analysis will create a {visualization_style}. Are you sure you would like to continue (1-yes, 0-no): ")
        if ask_again == 1:
            socket2.send_string(visualization_style)
            graph_path = socket2.recv_string()
            # Load the graph
            graph = mpimg.imread(graph_path)
            plt.imshow(graph)
            plt.show()
        page_input = exit_page_validation("Would you like to generate another visualization (1-yes, 0-no): ")
        if page_input == 0:
            break

def add_notes():
    while True:
        file = "notes.json"
        note = input("Write your notes: \n")
        data = {
            "file": file,
            "note": note
        }
        ask_again = exit_page_validation("Your note will be added to the notes.json file. Are you sure you would like to do this? (1-yes, 0-no): ")
        if ask_again == 1:
            message = json.dumps(data)
            socket4.send_string(message)
            is_added = socket4.recv_string()
            if is_added == "True":
                print("Note added successfully")
            else:
                print("Error while adding notes to file.")
        page_input = exit_page_validation("Would you like to add another note (1-yes, 0-no): ")
        if page_input == 0:
            break

def delete_notes():
    while True:
        date = input("Enter the date of the note entry you would like to delete (in the form YYYY-MM-DD): ")
        ask_again = exit_page_validation("Your note will be deleted from notes.json file. Are you sure you would like to do this? (1-yes, 0-no): ")
        if ask_again == 1:
            socket3.send_string(date)
            is_deleted = socket3.recv_string()
            if is_deleted == "True":
                print("Note deleted successfully.")
            else:
                print("Error while deleting file.")
        page_input = exit_page_validation("Would you like to delete another note (1-yes, 0-no): ")
        if page_input == 0:
            break

def view_notes():
    print("Printing notes in the form 'date: note'...")
    with open('notes.json', 'r') as file:
        data = json.load(file)
    for item in data:
        print(f"{item['date']}: {item['note']}")
   
def add_questions():
    while True:
        file = "questions.json"
        note = input("Write your question: ")
        data = {
            "file": file,
            "note": note
        }
        ask_again = exit_page_validation("Your question will be posted to the questions.json file to be answered by the admin. Are you sure you would like to do this? (1-yes, 0-no): ")
        if ask_again == 1:
            message = json.dumps(data)
            socket4.send_string(message)
            is_added = socket4.recv_string()
            if is_added == "True":
                print("Question added successfully and will be answered within 2 weeks.")
            else:
                print("Error while adding question to file.")
        page_input = exit_page_validation("Would you like to add another question (1-yes, 0-no): ")
        if page_input == 0:
            break    

def clear_file():
    with open('notes.json', 'w') as file:
        json.dump([], file)       

#####################################################################################################################
# PAGE FUNCTIONS
    
def home_page():
    print('-' * terminal_width)
    print(program_name, "\n")
    print("You will be able to choose your plotting style to create custom visualizations of our snowstorm dataset.")
    print("The progam also contains features to learn about different plotting styles, add/view/delete your notes, and ask questions about data analyis.\n")
    print("Page Options:")
    print("0. Home Page: view your page options")
    print("1. Example Visuals: view example visuals we've made!")
    print("2. Data Analysis: select your plotting style to create your own visualizations of snowstorm data!")
    print("3. Notes: view, add, or delete your analysis notes here!")
    print("4. Help & Resources: have questions? Look here!") 
    print("5. Exit the Program: closes the program") 
    page_input = page_input_validation()
    return page_input

def example_visuals():
    print('-' * terminal_width)
    print("Example Visuals".center(terminal_width), "\n")
    print("Here are some of our favorite visualizations! Feel free to take notes on trends you notice.")
    print("Visual 1: Total Snowfall Over Time")
    print("Variables observed: Total Snowfall (inches), Storm Dates")
    print("Visualization generating in new window...")
    # Load the graph
    graph = mpimg.imread("example_visual.png")
    plt.imshow(graph)
    plt.show()
    page_input = exit_page_validation("Would you like to return to the home page (1-yes, 0-no): ")
    if page_input == 1:
        # Home page option
        return 0
    else:
        # Example visual option
        return 1

# Data Analysis Page
# Functionality:
# 1. Choose visualization style
# 2. Plot custom visual
# 3. Learn about the different visualization options
def data_analysis():
    print('-' * terminal_width)
    print("Data Analysis".center(terminal_width), "\n")
    print("Now it's your turn! Build your own visualization of total snowfall data over time by picking your plotting style.\n")
    search_input = exit_page_validation("Would you like to learn more about the plotting style options? (1-yes, 0-no): ")
    if search_input == 1:
        search_term()
    visualization_input = exit_page_validation("Would you like to create your own visualization? (1-yes, 0-no): ")
    if visualization_input == 1:
        generate_visual()
    page_input = exit_page_validation("Would you like to return to the home page (1-yes, 0-no): ")
    if page_input == 1:
        # Home page option
        return 0
    else:
        # Data Analysis option
        return 2

# Notes Page
# Functionality:
# 1. delete notes based on date entry
# 2. add notes
def notes():
    print('-' * terminal_width)
    print("My Notes".center(terminal_width), "\n")
    print("Here is a space for you to write, delete, and view any notes from your analysis!")
    note_input = note_validation("Would you like to add (0), delete (1), or view (2) your notes? ")
    if note_input == 0:
        add_notes()
    elif note_input == 1:
        delete_notes()
    elif note_input == 2:
        view_notes()
    page_input = exit_page_validation("Would you like to return to the home page (1-yes, 0-no): ")
    if page_input == 1:
        # Home page option
        return 0
    else:
        # Notes option
        return 3
    
def help_resources():
    print('-' * terminal_width)
    print("Help & Resources".center(terminal_width), "\n")
    print("Common FAQ")
    print("Q. How do I get started?")
    print("A. Use the home page to navigate through the different pages. First, look at example visuals to get an idea of what to analyze. Then go to the Data Analysis page to start creating your visuals. If you notice any trends or patterns, write those ideas to your notes page. If you need help at any point, navigate to this page!")
    print("Q. The graph seems to be missing a lot of points. Did I do something wrong?")
    print("A. Missing points occur because of incomplete data. This means the variable you selected just doesn't have complete data, which is okay! This opens discussion on why we might be missing data here and you can predict what the data may look like with the value you are given.")
    print("\n")
    print("Resources")
    print("Northeast Big Data Innovation Hub: https://www.youtube.com/channel/UCaHjFSdvLnxWeYski3QjU_g")
    print("NOAA National Weather Service: https://www.weather.gov/")
    print("\n")
    print("Creator Contact: Valerie Lam - lamva@oregonstate.edu", "\n")
    question_input = exit_page_validation("Would you like to add a question (1-yes, 0-no): ")
    if question_input == 1:
        add_questions()
    page_input = exit_page_validation("Would you like to return to the home page (1-yes, 0-no): ")
    if page_input == 1:
        # Home page option
        return 0
    else:
        # Help and Resources option
        return 4

# Set up environment
context = zmq.Context()
# Microservice A
socket1 = context.socket(zmq.REQ)
socket1.connect("tcp://localhost:5555")
# Microservice B
socket2 = context.socket(zmq.REQ)
socket2.connect("tcp://localhost:5556")
# Microservice C
socket3 = context.socket(zmq.REQ)
socket3.connect("tcp://localhost:5557")
# Microservice D
socket4 = context.socket(zmq.REQ)
socket4.connect("tcp://localhost:5558")

# Start Program
terminal_width = os.get_terminal_size().columns
program_name = "❆ SnowStorm ❆".center(terminal_width)

logo1 = "\/".center(terminal_width)
logo2 = "_\_\/\/_/_".center(terminal_width)
logo3 = "_\_\/_/_".center(terminal_width)
logo4 = "__/_/\_\__".center(terminal_width)
logo5 = "/ /\/\ \\".center(terminal_width)
logo6 = "/\\".center(terminal_width)
print(logo1)
print(logo2)
print(logo3)
print(logo4)
print(logo5)
print(logo6)
print(program_name, "\n")
print()
print("Welcome to SnowStorm, a CLI program to create customizable visualizations of snowstorms in NW Oregon and SW Washington by choosing your plotting style.\n")

user_input = int(home_page())
while True:
    if user_input == 0:
        user_input = home_page()
    elif user_input == 1:
        user_input = example_visuals()
    elif user_input == 2:
        user_input = data_analysis()
    elif user_input == 3:
        user_input = notes()
    elif user_input == 4:
        user_input = help_resources()
    elif user_input == 5:
        break

clear_file()        # Clears notes.json file
# Quit servers
socket1.send_string("exit")
socket1.close()
socket2.send_string("exit")
socket2.close()
socket3.send_string("exit")
socket3.close()
socket4.send_string("exit")
socket4.close()
context.destroy()   # Destroys context
            
    
        
