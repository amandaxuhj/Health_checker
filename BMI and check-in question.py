import math


def BMI_calculator()->float:
    """The first half of the BMI function takes in user's height and weight, then calculate the user's BMI values. The value will be returned to the user as a visible output."""
    
    print("Welcome to the BMI(Body Mass Index) calculator! BMI values are derived from a person's height and weight and indicates whether you are underweight, orverweight,or in the healthy range.")
    height = float(input("please put in your height in inches: "))
    weight = float(input("please put in your weight in poounds: "))
    BMI_value =(weight/((height)*(height)))*703
    print("Your BMI value is", BMI_value)

    """The second part of the BMI_calculator function compares the user's BMI values with the standard value range and gives feedback to the user."""

    if BMI_value < 18.5:
        print("you are in the underweight range ")
    elif BMI_value >= 18.5 and BMI_value < 24.9:
        print("You are in the normal weight range!")
    elif BMI_value >= 24.9 and BMI_vlue < 29.9:
        print("you are in the overweight range.")
    elif BMI_value > 29.9:
        print("You are in the obeisity range.")


"""The Health Check-in Question"""

def health_checkin()->str:
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


def main():
    print("Welcome to health checker! We help you have a better understanding of your daily living habits and some of your basic health conditions!")
    print("\nAnd let's get started!First of all, what would you like to start with, the daily health check-in questions(1), or BMI-calculator?(2)")
    answer = input("\n Please type in 1 or 2: ")

    if answer == "1":
        health_checkin()
    elif answer == "2":
        BMI_calculator()
        
if __name__ == "__main__":
    main()
    
