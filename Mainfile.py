# Health Project Main Page
# Only things that we are definite on right now

Patient_info = []

def menu()-> str:
    print("Here is the list of things we can do for you and how to ask for them")
    print("* Calculate water intake - W")
    print("* Calculate calorie intake - F")
    print("* Show your target goals - T ")
    print("* Health check ins - C") 
    print("* Give you affirmations - A")

def screener()->str:
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

def run_aid()
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