import os

def welcome_page():
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

    user_input = input("Would you like to enter the home page (1-yes, 0-no): ")
    
    return user_input

def home_page():
    print('-' * terminal_width)
    print(program_name, "\n")
    print("You will be able to choose your variables to create custom visualizations of our snowstorm dataset.\n")
    print("Page Options:")
    print("1. Example Visuals: view example visuals we've made!")
    print("2. Data Analysis: select your variables and plots to create your own visualizations!")
    print("3. Notes: save or delete your analysis notes here!")
    print("4. Help & Resources: have questions? Look here!")
    print("5. Welcome Page\n")    
    user_input = input("Which page would you like to go to? (1, 2, 3, 4, 5): ")
    return user_input

def data_analysis():
    print('-' * terminal_width)
    print("Data Analysis".center(terminal_width), "\n")
    print("Now it's your turn! Build your own visualization by picking your variables & plotting style.\n")
    print("Variable options:")
    print("(1) Snowstorm (2) Location (3) Latitude/Longitude (4) Forecast Zone (5) Elevation Zone (6) Snowfall Totals\n")
    x_variable = input("Please select your x variable: ")
    y_variable = input("Please select your y variable: ")
    print()
    print("Visualization options: ")
    print("(1) Bar chart (2) Line graph (3) Scatter plot\n")
    visualization_style = input("Please select your visualization style: ")
    user_input = input("Would you like to run the analysis (1), get help (2), or return to the home page (3): ")
    if int(user_input) == 1:
        user_input = input(f"Running data analysis will create your custom visual with variable {x_variable} and variable {y_variable}. Are you sure you would like to continue: ")
    elif int(user_input) == 2:
        user_input = help_resources()
    return x_variable, y_variable, visualization_style, user_input

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

terminal_width = os.get_terminal_size().columns
program_name = "❆ SnowStorm ❆".center(terminal_width)

# Print Welcome Page
user_input = int(welcome_page())

if user_input == 1:
    home_page_input = int(home_page())
    # if home_page_input == 1:
    #     # Example visuals
    if home_page_input == 2:
        x_variable, y_variable, visualization_style, user_input = data_analysis()
    elif home_page_input == 4:
        help_page_input = int(help_resources())
        if help_page_input == 1:
            home_page_input == int(home_page())
            
    
        
