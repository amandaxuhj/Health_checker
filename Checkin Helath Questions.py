"""The Health Check-in Question"""

def health_checkin()->str:
    print("Welcome to daily health check-in section! Please answer the following questions by typing Y(yes) or N(no):")

    CIQ = 0
    Questions = ["Have you drank 8 cups of water? ","Have you gotten at least 7 hours of sleep? ","Have you eaten breakfast? ", "Have you worked out for at least one hour today? ", "Have you eaten some vegetables or fruit today? "]
    Responses = []
    q_number = 0
    # whatever the wording is here. Double check this
    while CIQ < 5: 
        question = input(Questions[q_number])
        if question == "Y": # Enter true
            Responses.append(question)
            q_number = q_number+1
            CIQ = CIQ+1
        elif question == "N": # Enter false
            q_number = q_number+1
            CIQ = CIQ + 1

    total = len(Responses)

    print("Your score is: ",total,"/5")
    print("You're doing a great job!Please take time to care for your body and health!")

    
        
#silly change

health_checkin()
