print("Do like to play this quiz ? : ")
answer = input("Y/N : ")

Total_question = 10
score = 100
if answer.lower() == "y"  or answer.lower() == "yes":

    # Question 1
    q1 = input("What has to be broken before you can use it?\n"
               "A) Glass\nB) Egg\nC) Pencil\nYour answer (A/B/C): ")

    if q1.lower() == "b" or q1.lower() == "egg":
        score += 10
        print("You were correct")
    else:
        print("You were wrong")

    # Question 2
    q2 = input("What is full of holes but still holds water?\n"
               "A) Sponge\nB) Bucket\nC) Sieve\nYour answer (A/B/C): ")

    if q2.lower() == "a" or q2.lower() == "sponge":
        score += 10
        print("You were correct")
    else:
        print("You were wrong")

    # Question 3
    q3 = input("What is always in front of you but can't be seen?\n"
               "A) Air\nB) Wind\nC) Future\nYour answer (A/B/C): ")

    if q3.lower() == "c" or q3.lower() == "future":
        score += 10
        print("You were correct")
    else:
        print("You were wrong")

    # Question 4
    q4 = input("What can you break, even if you never pick it up or touch it?\n"
               "A) Glass\nB) Stone\nC) Promise\nYour answer (A/B/C): ")

    if q4.lower() == "c" or q4.lower() == "promise":
        score += 10
        print("You were correct")
    else:
        print("You were wrong")

    # Question 5
    q5 = input("What goes up but never comes down?\n"
               "A) Helicopter\nB) Sponge\nC) Kite\nYour answer (A/B/C): ")

    if q5.lower() == "c" or q5.lower() == "kite":
        score += 10
        print("You were correct")
    else:
        print("You were wrong")

    # Question 6
    q6 = input("I shave every day, but my beard stays the same. What am I?\n"
               "A) Man\nB) Barber\nC) Cat\nYour answer (A/B/C): ")

    if q6.lower() == "b" or q6.lower() == "barber":
        score += 10
        print("You were correct")
    else:
        print("You were wrong")

    # Question 7
    q7 = input("The more of this there is, the less you see. What is it?\n"
               "A) Light\nB) Sound\nC) Darkness\nYour answer (A/B/C): ")

    if q7.lower() == "c" or q7.lower() == "darkness":
        score += 10
        print("You were correct")
    else:
        print("You were wrong")

    # Question 8
    q8 = input("David’s parents have three sons: Snap, Crackle, and what’s the name of the third son?\n"
               "A) John\nB) Robert\nC) David\nYour answer (A/B/C): ")

    if q8.lower() == "c" or q8.lower() == "david":
        score += 10
        print("You were correct")
    else:
        print("You were wrong")

    # Question 9
    q9 = input("What is black when it’s clean and white when it’s dirty?\n"
               "A) T-shirt\nB) Sock\nC) Whiteboard\nYour answer (A/B/C): ")

    if q9.lower() == "c" or q9.lower() == "whiteboard":
        score += 10
        print("You were correct")
    else:
        print("You were wrong")

    # Question 10
    q10 = input("Where does today come before yesterday?\n"
                "A) Calendar\nB) Time Machine\nC) Dictionary\nYour answer (A/B/C): ")

    if q10.lower() == "c" or q10.lower() == "dictionary":
        score += 10
        print("You were correct")
    else:
        print("You were wrong")

print("your score is ", score)
if score >= 80:
    print("you got exelent score")
elif score >= 50:
    print("you got bad score")

