import zmq
import os
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
            print("Invalid input. Please enter a number between 0 and 5: ")

def exit_page_validation(question):
    valid_choices = {'0', '1'}
    user_input = input(question)
    while True:
        if user_input in valid_choices:
            return int(user_input)
        else:
            print("Invalid input. Please enter either 1-yes or 0-no: ")

def visualization_validation(question):
    valid_choices = {'bar chart', 'line graph', 'scatter plot'}
    user_input = input(question)
    user_input = user_input.lower()
    while True:
        if user_input in valid_choices:
            return user_input
        else:
            print("Invalid input. Please enter bar chart, line graph, or scatter plot: ")

def search_term():
    while True:
        print("Visualization options: Bar chart, Line graph, Scatter plot")
        term = input("Please enter the visualization style you would like to learn about: ")
        socket1.send_string(term)
        definition = socket1.recv_string()
        print(definition)
        page_input = exit_page_validation("Would you like to search for another term (1-yes, 0-no): ")
        if page_input == 0:
            break

def generate_visual():
    while True:
        print("Visualization options: bar chart, line graph, scatter plot\n")
        visualization_style = visualization_validation("Please enter your visualization style: ")
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

#####################################################################################################################
# PAGE FUNCTIONS
    
def home_page():
    print('-' * terminal_width)
    print(program_name, "\n")
    print("You will be able to choose your variables to create custom visualizations of our snowstorm dataset.\n")
    print("Page Options:")
    print("0. Home Page: view your page options")
    print("1. Example Visuals: view example visuals we've made!")
    print("2. Data Analysis: select your variables and plots to create your own visualizations!")
    print("3. Notes: save or delete your analysis notes here!")
    print("4. Help & Resources: have questions? Look here!") 
    print("5. Exit the Program: closes the program") 
    page_input = page_input_validation()
    return page_input

def example_visuals():
    print('-' * terminal_width)
    print("Example visuals".center(terminal_width), "\n")
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
    print("Now it's your turn! Build your own visualization by picking your plotting style.\n")
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

def notes():
    print("Notes page")

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
    user_input = input("Would you like to enter the home page (1-yes, 0-no): ")
    return user_input

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
print("Welcome to SnowStorm, a CLI program to create customizable visualizations of snowstorms in NW Oregon and SW Washington by choosing your variables & plotting style.\n")

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

            
    
        
