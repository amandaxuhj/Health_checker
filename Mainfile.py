# Health Project Main Page
# Only things that we are definite on right now
#

import random
import math

Patient_info = []


def water()->str:
    # Tells the user how much water they have left to drink to reach their recommended water intake
    question = input("Do you want to use ounces or cups? O or C: ")
    question_two = int(input("How much water have you had today: "))
    if question == "O" or question == "o":
        wtotaltrue = water_needed()
        if wtotaltrue <= 0:
            print("You have already drank the recommended ounces of water for today!")
        else:
            print("You have",wtotaltrue - question_two,"ounces left to drink today.")
    elif question == "C" or question == "c":
        wtotal = water_needed()
        wtotaltrue = wtotal/8
        if wtotaltrue < 0:
            print("You have already drank the recommended cups of water for today!")
        else:
            print("You have",wtotaltrue - question_two, "cups left to drink today.")

def water_needed()->float:
    # Calculates the proper water intake needed depending on the users weight
    # This is a helper function so it then returns the correct number back to whichever function called it
    water_wei = Patient_info[3]/2.2
    if Patient_info[0] < 30:
        product = water_wei * 40
        finalnum = product / 28.3
        return finalnum
    elif Patient_info[0] >= 30 and Patient_info[0] <= 55:
        product = water_wei * 35
        finalnum = product / 28.3
        return finalnum
    elif Patient_info[0] > 55:
        product = water_wei * 30
        finalnum = product / 28.3
        return finalnum

def targets()->str:
    # This functions informs the user of milestones we are giving them and basing all our recommendations on
    print("Here are your targets that we are basing all our recommendations on:")
    print(" ")

    water = water_needed()
    print("Recommended water intake: ", water,"ounces of water")
    target_sleep()
    # Do we have any others?? If so add this

def target_sleep()->str:
    # Calculates the proper amount of sleep depending on the users age
    # This is a helper function that runs when called
    if Patient_info[0] >= 6 and Patient_info[0] <= 12:
        print("Recommended hours of sleep: 9-12 hours")
    elif Patient_info[0] >= 13 and Patient_info[0] <= 18:
        print("Recommended hours of sleep: 8-10 hours")
    elif Patient_info[0] > 18 and Patient_info[0] <= 65:
        print("Recommended hours of sleep: 8+ hours")
    elif Patient_info[0] > 65:
        print("Recommended hours of sleep: 7-8 hours")


def BMI_calculator()->float:
    """The first half of the BMI function takes in user's height and weight, then calculate the user's BMI values. The value will be returned to the user as a visible output."""
    
    print("Welcome to the BMI(Body Mass Index) calculator! BMI values are derived from a person's height and weight and indicates whether you are underweight, orverweight,or in the healthy range.")
    
    #height = float(input("please put in your height in inches: "))
    #weight = float(input("please put in your weight in poounds: "))
    #BMI_value =(weight/((height)*(height)))*703
    BMI_value = (Patient_info[3]/((Patient_info[2])*(Patient_info[2])))*703
    print("Your BMI value is", BMI_value)

    """The second part of the BMI_calculator function compares the user's BMI values with the standard value range and gives feedback to the user."""

    if BMI_value < 18.5:
        print("you are in the underweight range ")
    elif BMI_value >= 18.5 and BMI_value < 24.9:
        print("You are in the normal weight range!")
    elif BMI_value >= 24.9 and BMI_value < 29.9:
        print("you are in the overweight range.")
    elif BMI_value > 29.9:
        print("You are in the obeisity range.")


def check_in()->str:
    print("Welcome to daily health check-in section! Please answer the following questions by typing Y(yes) or N(no):")

    CIQ = 0
    # AS of now there are 5 questions here to tally
    Questions = ["Have you drank a cup of water today? ","Have you gotten at least 7 hours of sleep? ","Have you eaten a full meal today? ", "Have you worked out for at least one hour today? ", "Have you eaten some vegetables or fruit today? "]
    Responses = []
    q_number = 0
    while CIQ < 5: 
        question = input(Questions[q_number])
        if question == "Y": # Enter true
            Responses.append(question)
            q_number = q_number+1
            CIQ = CIQ+1
        elif question == "N": # Enter false
            q_number = q_number+1
            CIQ = CIQ + 1

    point_total = len(Responses)
    print("Your score is: ",point_total,"/5")
    print(" ")
    # Let's change this to my part of the code # Done/Did
    
    if point_total == 0:
        print(":( Please do yourself a favor, take some time and get these things done! We believe in you!!")
    elif point_total == 1 or point_total == 2:
        print(":( We know you can do better, your body deserves better. Take some time and get on these things. We believe in you!!")
    elif point_total == 3:
        print("Good job on taking time for your health, but let's try and get those two other tasks in. We believe in you!!")
    elif point_total == 4:
        # I think this message is a bit long, let's try it out in text testing
        print(":) Great Job!! You're doing great thigns for you health. Keep going and try to get in that one last thing. We believe in you!!")
    elif point_total == 5:
        print(":) YOU'RE DOING AMAZING!!! Keep up the great work!!")


def affirmation()->str:
    Affirmation = ["Investing in your health is one of the best investments you can make.", "Please take time to care for your body and health!","A healthy body is always the result of healthy thoughts and feelings.", "Let's work towards a healthier lifestyle! Yout got this!"]
    print(Affirmation[random.randint(0,3)])    # Don't forget to enter content here



def menu()-> str:
    ### This is the list of options available to the user
    print("\nHere is the list of things we can do for you and how to ask for them")
    print("* Calculate water intake - W")
    print("* Calculate BMI - B") # change this to whatever it is related to BMI
    print("* Show your target goals - T ")
    print("* Health check ins - C") 
    print("* Give you affirmations - A")

def screener()->str:
    ### Theses are questions to add to the bank function for the rest of the personalised computations
    print(" ")
    print("We need to ask some screener questions about you so we can help :)")
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

def run_aid()->str:
    ### This is like a port that will take the user to the service they want to use
    print(" ")
    Start = input("What would you like to do today? ")
    if Start == "W" or Start == "w":
        water()
    elif Start == "B" or Start == "b":
        BMI_calculator()
    elif Start == "C" or Start == "c":
        check_in()
    elif Start == "A" or Start == "a":
        affirmation()
    elif Start == "T" or Start == "t":
        targets()
    # When ready make sure to add the error message


def get_help()-> None:
    # This is the main function that you should run to run the entire program
    print("Welcome to Health Tracker. We can help you with your health.")
    question = input("Have you ever used our services before? Y or N: ")
    if question == "Y" or question == "y":
        print("Welcome back! :)")
        run_aid()
    elif question == "N" or question == "n":
        screener()
        # should we just display the menu and then other times we can ask
        question_two = input("\nWould you like to see our Menu? Y or N: ")
        if question_two == "Y" or question_two == "y":
            menu()
            run_aid()
        elif question_two == "N" or question_two == "n":
            run_aid()
    final_question = input("\nIs that all for today? Y or N: ")
    if final_question == "Y" or final_question == "y":
        print("Have a good day! Come Again! :)")
    elif final_question == "N" or final_question == "n":
        print("This is filler for now")
        # need to enter something here


get_help()




