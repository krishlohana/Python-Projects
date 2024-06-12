# Calculator (CLI)
try:
    N1 = int(input("Enter First Number:  "))
    N2 = int(input("Enter Second Number: "))

    Flag = False

    while Flag == False:

        Operation = input("Enter The Operation Of Your Choice: +, -, *, /: \n")

        if Operation == "+":
            print("Addition = " , N1 + N2)
            Flag = True

        elif Operation == "-":
            print("Subtraction = " , N1 - N2)
            Flag = True

        elif Operation == "*":
            print("Multiplication = " , N1 * N2)
            Flag = True

        elif Operation == "/":
            if N2 == 0:
                print("Infinity...")
                Flag = True
            else:
                print("Division = " , N1 / N2)
                Flag = True
        else:
            print("Invalid operator... Re-Enter The Operation Again! \n ")
            Flag = False
except ValueError:
    print("Invalid Input. Please Enter Integer Numbers... ")