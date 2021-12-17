"""The Health Check-in Question"""

def health_checkin()->str:
    print("Welcome to daily health check-in section! Please answer the following questions by typing Y(yes) or N(no):")
    print(" ")
    CIQ = 0
    # AS of now there are 5 questions here to tally
    Questions = ["Have you drank a cup of water today? ","Have you gotten at least 7 hours of sleep? ","Have you eaten a full meal today? ", "Have you worked out for at least one hour today? ", "Have you eaten some vegetables or fruit today? "]
    Responses = []
    q_number = 0
    while CIQ < 5: 
        question = input(Questions[q_number])
        if question == "Y" or question == "n":
            Responses.append(question)
            q_number = q_number+1
            CIQ = CIQ+1
        elif question == "N" or question == "n":
            q_number = q_number+1
            CIQ = CIQ + 1

    point_total = len(Responses)
    print("Your score is: ",point_total,"/5")
    print(" ")
    # Let's change this to my part of the code # Done/Did
    if point_total = 0:
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
        
