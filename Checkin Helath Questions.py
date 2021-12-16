"""The Health Check-in Question"""

def health_checkin()->str:
    print("Welcome to daily health check-in section! Please answer the following questions:")

    CIQ = 0
    Questions = ["Have you drank 8 cups of water? ","Have you gotten at least 7 hours of sleep ","Have you eaten breakfast "]
    Responses = []
    q_number = 0
    # whatever the wording is here. Double check this
    while CIQ < 3: 
        question = input(Questions[q_number])
        if question == "Y": # Enter true
            Responses.append(question)
            q_number = q_number+1
            CIQ = CIQ+1
        elif question == "N": # Enter false
            q_number = q_number+1
            CIQ = CIQ + 1

    total = len(Responses)
    print("Your score is: ",total,"/3")
    print("You are beautiful!")
    
        



#Have you worked out for at least one hour today?
#
