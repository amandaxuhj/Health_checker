import random
def affirmation()->str:
    Affirmation = ["Investing in your health is one of the best investments you can make.", "Please take time to care for your body and health!","A healthy body is always the result of healthy thoughts and feelings.", "Let's work towards a healthier lifestyle! Yout got this!"]
    print(Affirmation[random.randint(0,3)])
    
affirmation()
