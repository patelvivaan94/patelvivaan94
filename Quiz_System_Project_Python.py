d = "Y"

while( d == "Y" or d == "Y"):
    a = input("Enter your username:")
    password = "RR3"
    
    b = input("Enter the password:")
    while(b != password):
        b = input(f"This is the incorrect password. Please enter again:")
        
    if b == password:
        print(f" Hello {a} and Welcome to the Math Quiz! Good luck")
        print(f"")
    
    score = 0
    
    def ScorePlus():
        global score
        score += 10
        print(" Your Score: ",score)
        
    def ScoreMinus():
        global score
        score -= 2
        print(" Your Score: ",score)
        
    print(f"!!!!!!!Question Number 1 is below!!!!!!!!!!")
    
    def q1():
        global score
        print(" 27 + 36 = ? ")
        print("1. 65")
        print("2. 63")
        print("3. 14")
        print("4. 2")
        answer = str(input("Enter the option:"))
        while(not answer.isdigit() or int(answer) >= 5):
            answer = input("!!!Error! Please input something inbetween the value of 1 and 4!!!:")
        if answer == "2":
            print("Ding ding ding! Thats correct! Moving on!")
            ScorePlus()
        else:
            print("Sorry, but that is incorrect, moving on!")
            ScoreMinus()
    q1()
    
    print(f"!!!!!!!Question Number 2 is below!!!!!!!!!!")
    def q2():
        global score
        print(" 162 + 284 = ? ")
        print("1. 298")
        print("2. 445")
        print("3. 447")
        print("4. 446")
        answer = str(input("Enter the option:"))
        while(not answer.isdigit() or int(answer) >= 5):
            answer = input("!!!Error! Please input something inbetween the value of 1 and 4!!!:")
        if answer == "4":
            print("Ding ding ding! Thats correct! Moving on!")
            ScorePlus()
        else:
            print("Sorry, but that is incorrect, moving on!")
            ScoreMinus()
    q2()
    
    print(f"!!!!!!!Question Number 3 is below!!!!!!!!!!")
    def q3():
        global score
        print(" 5 x 7 = ? ")
        print("1. 32")
        print("2. 54")
        print("3. 98")
        print("4. 35")
        answer = str(input("Enter the option:"))
        while(not answer.isdigit() or int(answer) >= 5):
            answer = input("!!!Error! Please input something inbetween the value of 1 and 4!!!:")
        if answer == "4":
            print("Ding ding ding! Thats correct! Moving on!")
            ScorePlus()
        else:
            print("Sorry, but that is incorrect, moving on!")
            ScoreMinus()
    q3()
    
    print(f"!!!!!!!Question Number 4 is below!!!!!!!!!!")
    def q4():
        global score
        print(" 28 x 53 = ? ")
        print("1. 1038")
        print("2. 2023")
        print("3. 1484")
        print("4. 2054")
        answer = str(input("Enter the option:"))
        while(not answer.isdigit() or int(answer) >= 5):
            answer = input("!!!Error! Please input something inbetween the value of 1 and 4!!!:")
        if answer == "3":
            print("Ding ding ding! Thats correct! Moving on!")
            ScorePlus()
        else:
            print("Sorry, but that is incorrect, moving on!")
            ScoreMinus()
    q4()
    
    print(f"!!!!!!!Question Number 5 is below!!!!!!!!!!")
    def q5():
        global score
        print(" 36 / 4 = ? ")
        print("1. 2")
        print("2. 9")
        print("3. 7")
        print("4. 12")
        answer = str(input("Enter the option:"))
        while(not answer.isdigit() or int(answer) >= 5):
            answer = input("!!!Error! Please input something inbetween the value of 1 and 4!!!:")
        if answer == "2":
            print("Ding ding ding! Thats correct! Moving on!")
            ScorePlus()
        else:
            print("Sorry, but that is incorrect, moving on!")
            ScoreMinus()
    q5()
    
    print(f"!!!!!!!Question Number 6 is below!!!!!!!!!!")
    def q6():
        global score
        print(" 187 / 3 = ? ")
        print("1. 54.9")
        print("2. 62.3")
        print("3. 57.2")
        print("4. 68.6")
        answer = str(input("Enter the option:"))
        while(not answer.isdigit() or int(answer) >= 5):
            answer = input("!!!Error! Please input something inbetween the value of 1 and 4!!!:")
        if answer == "2":
            print("Ding ding ding! Thats correct! Moving on!")
            ScorePlus()
        else:
            print("Sorry, but that is incorrect, moving on!")
            ScoreMinus()
    q6()
    
    print(f"!!!!!!!Question Number 7 is below!!!!!!!!!!")
    def q7():
        global score
        print(" (5 x 4) + 36 / 7 equal? ")
        print("1. 24")
        print("2. 33")
        print("3. 26")
        print("4. 87")
        answer = str(input("Enter the option:"))
        while(not answer.isdigit() or int(answer) >= 5):
            answer = input("!!!Error! Please input something inbetween the value of 1 and 4!!!:")
        if answer == "3":
            print("Ding ding ding! Thats correct! Moving on!")
            ScorePlus()
        else:
            print("Sorry, but that is incorrect, moving on!")
            ScoreMinus()
    q7()
    
    print(f"!!!!!!!Question Number 8 is below!!!!!!!!!!")
    def q8():
        global score
        print(" 9857 - 9 = ? ")
        print("1. 9857")
        print("2. 9848")
        print("3. 8947")
        print("4. 9080")
        answer = str(input("Enter the option:"))
        while(not answer.isdigit() or int(answer) >= 5):
            answer = input("!!!Error! Please input something inbetween the value of 1 and 4!!!:")
        if answer == "2":
            print("Ding ding ding! Thats correct! Moving on!")
            ScorePlus()
        else:
            print("Sorry, but that is incorrect, moving on!")
            ScoreMinus()
    q8()
    
    print(f"!!!!!!!Question Number 9 is below!!!!!!!!!!")
    def q9():
        global score
        print(" 4 x 9 = ? ")
        print("1. 36")
        print("2. 24")
        print("3. 48")
        print("4. 56")
        answer = str(input("Enter the option:"))
        while(not answer.isdigit() or int(answer) >= 5):
            answer = input("!!!Error! Please input something inbetween the value of 1 and 4!!!:")
        if answer == "1":
            print("Ding ding ding! Thats correct! Moving on!")
            ScorePlus()
        else:
            print("Sorry, but that is incorrect, moving on!")
            ScoreMinus()
    q9()
    
    print(f"!!!!!!!Question Number 10 is below!!!!!!!!!!")
    def q10():
        global score
        print(" 37 x 93 = ? ")
        print("1. 3476")
        print("2. 3329")
        print("3. 3441")
        print("4. 3879")
        answer = str(input("Enter the option:"))
        while(not answer.isdigit() or int(answer) >= 5):
            answer = input("!!!Error! Please input something inbetween the value of 1 and 4!!!:")
        if answer == "3":
            print("Ding ding ding! Thats correct! Moving on!")
            ScorePlus()
        else:
            print("Sorry, but that is incorrect, moving on!")
            ScoreMinus()
    q10()
    print(f"")
    d = input("Do you want to take the quiz again? (Y/N):")
    if d == "N" or d == "n":
        print(f" Good Job, {a}! You got {score} points")
        print(f"")






