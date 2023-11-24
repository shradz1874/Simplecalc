def calc():
    def add():
        c = a + b
        print("the addition of the two numbers is:", c)

    def sub():
        d = a - b
        print("the substraction of the two numbers is: ", d)

    def mult():
        e = a * b
        print("The multiplication of the two numbers is: ", e)

    def div():
        f = a / b
        print("The division of the two numbers is: ", f)

    def mod():
        g = a % b
        print("the modulo of the two numbers is: ", g)

    print("WELCOME TO OUR SIMPLE CALCULATOR \n")
    a = float(input("Enter the first value : \n"))
    b = float(input("enter the second value : \n"))
    h = float(input("\nenter the operation to be performed :\n"
                    "PRESS 1 FOR ADDITION \n"
                    "PRESS 2 FOR SUBSTRACTION \n"
                    "PRESS 3 for multiplication \n"
                    "press 4 for division \n"
                    "press 5 for modulus operation \n\n"))

    if h == 1:
        add()

    elif h == 2:
        sub()

    elif h == 3:
        mult()

    elif h == 4:
        div()

    else:
        mod()

    m = int(input("\nDo you wish to do another calculation?\n Press 1 if yes\n Press 2 if no\n"))
    if m==1:
        calc()


    elif m==2:
        print("Thank you for using this simple calculator")

    else:
        print("enter a valid choice")
        calc()

calc()






























