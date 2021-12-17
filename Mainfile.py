# Health Project Main Page
# Only things that we are definite on right now

Patient_info = []

def menu()-> str:
    ### This is the list of options available to the user
    print("Here is the list of things we can do for you and how to ask for them")
    print("* Calculate water intake - W")
    print("* Calculate calorie intake - F")
    print("* Show your target goals - T ")
    print("* Health check ins - C") 
    print("* Give you affirmations - A")

def screener()->str:
    ### Theses are questions to add to the bank function for the rest of the personalised computations
    age = int(input("What is your age: "))
    Patient_info.append(age)
    print("What is your sex? Male or Female")
    sex = input("M or F: ")
    Patient_info.append(sex)
    hei = int(input("What is your height(in inches): "))
    Patient_info.append(hei)
    wei = int(input("What is your weight(in pounds): "))
    Patient_info.append(wei)
    # if we need more we can add it from the other files

def run_aid()->:
    ### This is like a port that will take the user to the service they want to use
    Start = input("What would you like to do today? ")
    if Start == "W" or Start == "w":
        water()
    elif Start == "F" or Start == "f":
        calorie()
    elif Start == "C" or Start == "c":
        check_in()
    elif Start == "A" or Start == "a":
        affirmations()
    elif Start == "T" or Start == "t":
        targets()
    # When ready make sure to add the error message


def get_help()-> None:
    print("Welcome to ___. We can help you with your health.")
    question = input("Have you ever used our services before? Y or N")
    if question == "Y"
        print("Welcome back! :)")
        run_aid()
    elif question == "N"
        screener()
        # should we just display the menu and then other times we can ask
        question_two = input("Would you like to see our Menu? Y or N")
            if question_two == "Y":
                menu()
                runaid()
            elif question_two == "N":
                runaid()
    final_question = input("Is that all for today? Y or N: ")
    if final_question == "Y":
        print("Have a good day! Come Again! :)")
    elif final_question == "N":
        # need to enter something here