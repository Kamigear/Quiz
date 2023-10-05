print("Do like to play this quiz ? : ")
answer = input("Y/N : ")

Total_question = 10
score = 100
if answer.lower() == "y"  or answer.lower() == "yes":

    #question
    q1 = input("What has to be broken before you can use it?")
    if q1.lower() == "egg":
        print("You were correct")
    else:
        score -= 10
        print("You were wrong")

    q2 = input("What is full of holes but still holds water?")
    if q2.lower() == "sponge":
        print("You were correct")
    else:
        score -= 10
        print("You were wrong")

    q3 = input("What is always in front of you but can’t be seen?")
    if q3.lower() == "future":
        print("You were correct")
    else:
        score -= 10
        print("You were wrong")

    q4 = input("What can you break, even if you never pick it up or touch it?")
    if q4.lower() == "promise":
        print("You were correct")
    else:
        score -= 10
        print("You were wrong")

    q5 = input("What goes up but never comes down?")
    if q5.lower() == "sponge":
        print("You were correct")
    else:
        score -= 10
        print("You were wrong")

    q6 = input("I shave every day, but my beard stays the same. What am I?")
    if q6.lower() == "barber":
        print("You were correct")
    else:
        score -= 10
        print("You were wrong")

    q7 = input("The more of this there is, the less you see. What is it?")
    if q7.lower() == "darkness":
        print("You were correct")
    else:
        score -= 10
        print("You were wrong")

    q8 = input("David’s parents have three sons: Snap, Crackle, and what’s the name of the third son?")
    if q8.lower() == "david":
        print("You were correct")
    else:
        score -= 10
        print("You were wrong")

    q9 = input("What is black when it’s clean and white when it’s dirty?")
    if q9.lower() == "whiteboard":
        print("You were correct")
    else:
        score -= 10
        print("You were wrong")

    q10 = input("Where does today come before yesterday?")
    if q10.lower() == "dictionary":
        print("You were correct")
    else:
        score -= 10
        print("You were wrong")

print("your score is ", score)
if score >= 80:
    print("you got exelent score")
elif score >= 50:
    print("you got bad score")

