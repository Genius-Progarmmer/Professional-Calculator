def basic_operation(num1, num2, operation):
                    
    if operation == "+":
        return num1 + num2

    elif operation == "-":
        return num1 - num2

    elif operation == "*":
        return num1 * num2

    elif operation == "/":
        if num2 == 0:
           return "erorr! division by zero..."
            
        else:
            return num1 / num2
        
def power(num1, num2):
    result = num1 ** num2
    return result



def sqrt(num):
    result = "Erorr!..." if (num < 0) else num ** 0.5
    return result



def persentage(num1, num2):
    return (num1 * num2) / 100



def exit_open_function():
    exit_open = input("typing 'open' or 'exit' : ")
    while exit_open != "exit" and exit_open != "open":
        exit_open = input("Erorr....please typing 'open' or 'exit' : ")
    return exit_open











def main():
    print("welcome to Calculator! type /open/ to start and /exit/ to turn off")
    while True:
        
        exit_open = exit_open_function()
        if exit_open == "exit":
            print("Calculator turned off. you can restart by typing 'open' anytime")
            continue

        elif exit_open == "open":

            while True:
                operation = input("enter operation(+, -, *, /, ^, % and √(square root) or 'exit' ): ")

                if operation == "exit":
                    print("Calculator turned off. you can restart by typing 'open' anytime")
                    exit_open = input("typing 'open' to start : ")
                    break
                elif operation == "√":
                    num = float(input("enter number for square root : "))
                    result = sqrt(num)
                    print(f"√{num} = {result}")

                elif operation == "%":
                    num1 = float(input("enter first number : "))
                    num2 = float (input("enter second number : "))
                    result = persentage(num1, num2)
                    print(f"{num1} % of {num2}")

                elif operation == "^":
                    num1 = float(input("enter first number : "))
                    num2 = float (input("enter second number : "))
                    result = power(num1, num2)
                    print(f"{num1} {operation} {num2} = {result}")

                elif operation == "+" or operation == "-" or operation == "*" or operation == "/":
                    num1 = float(input("enter first number : "))
                    num2 = float (input("enter second number : "))
                    result = basic_operation(num1, num2, operation)
                    print(f"{num1} {operation} {num2} = {result}")

                    



                    

                else:
                    result = "invalid operation"
                    
                    


main()