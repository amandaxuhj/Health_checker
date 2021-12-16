""" BMI calculator is part of the function of the health program. """
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


BMI_calculator() 

