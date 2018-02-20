from random import randint
counter = 0
counter1 = 0
#***************************************  Addition Function **************************************
def addition(difficulty,nos_question):
    solved = 0
    total_num_q = nos_question
    global counter
    if counter is 1:
        res = recall_fun()
        solved = 0
        difficulty = str(res[0])
        nos_question = int(res[1])
        total_num_q = nos_question
        counter = 0
    if difficulty == 'E':
        while nos_question:
            try:
                a = randint(0, 50)
                b = randint(0, 10)
                answer = int(input("What's {} + {}\nAnswer: ".format(a,b)))
                if answer == (a + b):
                    print "That's right -- well done!!!\n"
                    solved += 1
                else:
                    print "No, I'm afraid the answer is: {}\n".format(a+b)
                nos_question -= 1
            except (NameError, SyntaxError):
                print '!!!Enter a valid integer!!!'
                continue
            except KeyboardInterrupt:
                print 'Oops!! Keyboard Interrupt''\n''Good bye'
                exit()
    if difficulty == 'I':
        while nos_question:
            try:
                a = randint(50, 100)
                b = randint(50, 100)
                answer = int(input("What's {} + {}\nAnswer: ".format(a, b)))
                if answer == (a + b):
                    print "That's right -- well done!!!\n"
                    solved +=1
                else:
                    print "No, I'm afraid the answer is: {}\n".format(a+b)
                nos_question -= 1
            except (NameError, SyntaxError):
                print '!!!Enter a valid integer!!!'
                continue
            except KeyboardInterrupt:
                print 'Oops!! Keyboard Interrupt''\n''Good bye'
                exit()
    if difficulty == 'H':
        while nos_question:
            try:
                a = randint(100, 900)
                b = randint(100, 900)
                answer = int(input("What's {} + {}\nAnswer: ".format(a, b)))
                if answer == (a + b):
                    print "That's right -- well done!!!\n"
                    solved +=1
                else:
                    print "No, I'm afraid the answer is: {}\n".format(a+b)
                nos_question -= 1
            except (NameError, SyntaxError):
                print '!!!Enter a valid integer!!!'
                continue
            except KeyboardInterrupt:
                print 'Oops!! Keyboard Interrupt''\n''Good bye'
                exit()
    print '\033[FOut of {} question(s) asked, you got {} answer(s) right.\n'.format(total_num_q, solved)
    return 0

# *************************************** Subtraction Function **************************************

def subtraction(difficulty, nos_question):
    solved = 0
    total_num_q = nos_question
    global counter
    if counter is 1:
        res = recall_fun()
        solved = 0
        difficulty = str(res[0])
        nos_question = int(res[1])
        total_num_q = nos_question
        counter = 0
    if difficulty == 'E':
        while nos_question:
            try:
                a = randint(0, 50)
                b = randint(0, 10)
                answer = int(input("What's {} - {}\nAnswer: ".format(a, b)))
                if answer == (a - b):
                    print "That's right -- well done!!!\n"
                    solved +=1
                else:
                    print "No, I'm afraid the answer is: {}\n".format(a-b)
                nos_question -= 1
            except (NameError, SyntaxError):
                print '!!!Enter a valid integer!!!'
                continue
            except KeyboardInterrupt:
                print 'Oops!! Keyboard Interrupt''\n''Good bye'
                exit()
    if difficulty == 'I':
        while nos_question:
            try:
                a = randint(50, 100)
                b = randint(50, 100)
                answer = int(input("What's {} - {}\nAnswer: ".format(a, b)))
                if answer == (a - b):
                    print "That's right -- well done!!!\n"
                    solved+=1
                else:
                    print "No, I'm afraid the answer is: {}\n".format(a-b)
                nos_question -= 1
            except (NameError, SyntaxError):
                print '!!!Enter a valid integer!!!'
                continue
            except KeyboardInterrupt:
                print 'Oops!! Keyboard Interrupt''\n''Good bye'
                exit()
    if difficulty == 'H':
        while nos_question:
            try:
                a = randint(100, 900)
                b = randint(100, 900)
                answer = int(input("What's {} - {}\nAnswer: ".format(a, b)))
                if answer == (a - b):
                    print "That's right -- well done!!!\n"
                    solved +=1
                else:
                    print "No, I'm afraid the answer is: {}\n".format(a-b)
                nos_question -= 1
            except (NameError, SyntaxError):
                print '!!!Enter a valid integer!!!'
                continue
            except KeyboardInterrupt:
                print 'Oops!! Keyboard Interrupt''\n''Good bye'
                exit()
    print '\033[FOut of {} question(s) asked, you got {} answer(s) right.\n'.format(total_num_q, solved)
    return 0

#*************************************** Multiplication Function **************************************

def multiplication(difficulty, nos_question):
    solved = 0
    total_num_q = nos_question
    global counter
    if counter is 1:
        res = recall_fun()
        solved = 0
        difficulty = str(res[0])
        nos_question = int(res[1])
        total_num_q = nos_question
        counter = 0
    if difficulty == 'E':
        while nos_question:
            try:
                a = randint(0, 50)
                b = randint(0, 10)
                answer = int(input("What's {} X {}\nAnswer: ".format(a, b)))
                if answer == (a * b):
                    print "That's right -- well done!!!\n"
                    solved +=1
                else:
                    print "No, I'm afraid the answer is: {}\n".format(a*b)
                nos_question -= 1
            except (NameError, SyntaxError):
                print '!!!Enter a valid integer!!!'
                continue
            except KeyboardInterrupt:
                print 'Oops!! Keyboard Interrupt''\n''Good bye'
                exit()
    if difficulty == 'I':
        while nos_question:
            try:
                a = randint(50, 100)
                b = randint(50, 100)
                answer = int(input("What's {} X {}\nAnswer: ".format(a, b)))
                if answer == (a * b):
                    print "That's right -- well done!!!\n"
                    solved +=1
                else:
                    print "No, I'm afraid the answer is: {}\n".format(a*b)
                nos_question -= 1
            except (NameError, SyntaxError):
                print '!!!Enter a valid integer!!!'
                continue
            except KeyboardInterrupt:
                print 'Oops!! Keyboard Interrupt''\n''Good bye'
                exit()
    if difficulty == 'H':
        while nos_question:
            try:
                a = randint(100, 900)
                b = randint(100, 900)
                answer = int(input("What's {} X {}\nAnswer: ".format(a, b)))
                if answer == (a * b):
                    print "That's right -- well done!!!\n"
                    solved +=1
                else:
                    print "No, I'm afraid the answer is: {}\n".format(a*b)
                nos_question -= 1
            except (NameError, SyntaxError):
                print '!!!Enter a valid integer!!!'
                continue
            except KeyboardInterrupt:
                print 'Oops!! Keyboard Interrupt''\n''Good bye'
                exit()
    print '\033[FOut of {} question(s) asked, you got {} answer(s) right.\n'.format(total_num_q, solved)
    return 0

#***************************************   Division Function **************************************

def divison(difficulty, nos_question):
    solved = 0
    total_num_q = nos_question
    global counter
    if counter is 1:
        res = recall_fun()
        solved = 0
        difficulty = str(res[0])
        nos_question = int(res[1])
        total_num_q = nos_question
        counter = 0
    if difficulty == 'E':
        while nos_question:
            try:
                a = randint(0, 50)
                b = randint(1, 10)
                answer = int(input("What's {} / {}\nAnswer: ".format(a, b)))
                if answer == (a / b):
                    print "That's right -- well done!!!\n"
                    solved +=1
                else:
                    print "No, I'm afraid the answer is: {}\n".format(a/b)
                nos_question -= 1
            except (NameError, SyntaxError):
                print '!!!Enter a valid integer!!!'
                continue
            except KeyboardInterrupt:
                print 'Oops!! Keyboard Interrupt''\n''Good bye'
                exit()

    if difficulty == 'I':
        while nos_question:
            try:
                a = randint(50, 100)
                b = randint(50, 100)
                answer = int(input("What's {} / {}\nAnswer: ".format(a, b)))
                if answer == (a / b):
                    print "That's right -- well done!!!\n"
                    solved +=1
                else:
                    print "No, I'm afraid the answer is: {}\n".format(a/b)
                nos_question -= 1
            except (NameError, SyntaxError):
                print '!!!Enter a valid integer!!!'
                continue
            except KeyboardInterrupt:
                print 'Oops!! Keyboard Interrupt''\n''Good bye'
                exit()
    if difficulty == 'H':
        while nos_question:
            try:
                a = randint(100, 900)
                b = randint(100, 900)
                answer = int(input("What's {} / {}\nAnswer: ".format(a, b)))
                if answer == (a / b):
                    print "That's right -- well done!!!\n"
                    solved +=1
                else:
                    print "No, I'm afraid the answer is: {}\n".format(a/b)
                nos_question -= 1
            except (NameError, SyntaxError):
                print '!!!Enter a valid integer!!!'
                continue
            except KeyboardInterrupt:
                print 'Oops!! Keyboard Interrupt''\n''Good bye'
                exit()
    print '\033[FOut of {} question(s) asked, you got {} answer(s) right.\n'.format(total_num_q, solved)
    return 0



#***************************************   Recall Function **************************************

def recall_fun():
    total_num_q = 0
    solved = 0
    difficulty = None
    level_type = ['E', 'I', 'H']
    while True:
        try:
            difficulty = raw_input('Choose level (Easy:E, Intermediate:I, and Hard:H): ').upper()
        except KeyboardInterrupt:
            print 'Good bye'
            exit()
        if difficulty not in level_type:
            print '!!!Please enter correct level name!!!'
            continue
        else:
            break
    while True:
        try:
            nos_question = int(input('Please give us the number of question you want to attempt: '))
            total_num_q = nos_question
        except:
            print '!!!Enter a valid integer!!!'
            continue
        else:
            if nos_question <= 0:
                print 'Enter a non-zero integer'
                continue
        break
    return difficulty,nos_question

#***************************************  Main Input Function **************************************

def main_input_quiz():
    print '\n************* WELCOME TO THE QUIZ **************\n'
    print '"Press CTRL + C at any time during the quiz to quit"\n'
    res = recall_fun()
    difficulty = str(res[0])
    nos_question = int(res[1])
    question_type = ['A', 'S', 'D', 'M']
    while True:
        print 'Specify the question type:'
        qtype = raw_input('Addition-A:\nSubtraction-S:\nDivision-D:\nMultiplication-M: ').upper()
        if qtype not in question_type:
            print("!!! Please enter a valid choice !!!")
            continue
        else: break

    global counter
    global counter1
    while True:
        if counter1 == 0:
            if qtype =='A':
                addition(difficulty,nos_question)
                counter1 = 1
        if counter1 ==1:
            if qtype == 'A':
                check = raw_input('Would you like to try Addition again?(Y/N):').upper()
                if check == 'Y':
                    counter = 1
                    addition(difficulty, nos_question)
                    continue
                while check == 'N':
                    recheck = raw_input('Would you like to go back to the main menu?(Y/N):').upper()
                    if recheck == 'Y':
                        counter1 = 0
                        main_input_quiz()
                    elif recheck == 'N':
                        print '====================Good bye====================\n'
                        exit()
                    else:
                        print 'Invalid choice'
                        continue
                else:
                    print'Invalid choice!!'
                    continue
        if counter1 == 0:
            if qtype =='S':
                subtraction(difficulty,nos_question)
                counter1 = 1
        if counter1 ==1:
            if qtype == 'S':
                check = raw_input('Would you like to try subtraction again?(Y/N):').upper()
                if check == 'Y':
                    counter = 1
                    subtraction(difficulty, nos_question)
                    continue
                while check == 'N':
                    recheck = raw_input('Would you like to go back to the main menu?(Y/N):').upper()
                    if recheck == 'Y':
                        counter1 = 0
                        main_input_quiz()
                    elif recheck == 'N':
                        print '====================Good bye====================\n'
                        exit()
                    else:
                        print 'Invalid choice'
                        continue
                else:
                    print'Invalid choice!!'
                    continue


        if counter1 == 0:
            if qtype =='M':
                multiplication(difficulty,nos_question)
                counter1 = 1
        if counter1 ==1:
            if qtype == 'M':
                check = raw_input('Would you like to try multiplication again?(Y/N):').upper()
                if check == 'Y':
                    counter = 1
                    multiplication(difficulty, nos_question)
                    continue
                while check == 'N':
                    recheck = raw_input('Would you like to go back to the main menu?(Y/N):').upper()
                    if recheck == 'Y':
                        counter1 = 0
                        main_input_quiz()
                    elif recheck == 'N':
                        print '====================Good bye====================\n'
                        exit()
                    else:
                        print'Invalid choice!!'
                        continue
                else:
                    print'Invalid choice!!'
                    continue


        if counter1 == 0:
            if qtype =='D':
                divison(difficulty,nos_question)
                counter1 = 1
        if counter1 ==1:
            if qtype == 'D':
                check = raw_input('Would you like to try division again?(Y/N):').upper()
                if check == 'Y':
                    counter = 1
                    divison(difficulty, nos_question)
                    continue
                while check == 'N':
                    recheck = raw_input('Would you like to go back to the main menu?(Y/N):').upper()
                    if recheck == 'Y':
                        counter1 = 0
                        main_input_quiz()
                    elif recheck == 'N':
                        print '====================Good bye====================\n'
                        exit()
                    else:
                        print 'Invalid choice'
                        continue
                else:
                    print'Invalid choice!!'
                    continue


main_input_quiz()