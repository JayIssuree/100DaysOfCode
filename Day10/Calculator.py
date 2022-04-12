def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(raw_input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    operation_symbol = raw_input("Pick an operation from the line above: ")

    num2 = float(raw_input("What's the second number?: "))


    answer = operations[operation_symbol](num1, num2)
    message = str(num1) + " " + operation_symbol + " " + str(num2) + " = " + str(answer)
    print(message)

    chain_operations = True

    while(chain_operations):

        proceed = raw_input("Would you like to continue? 'y' or 'n'? ")
        if(proceed is not 'y'):
            calculator()

        for symbol in operations:
            print(symbol)
        operation_symbol = raw_input("Pick an operation from the line above: ")
        num3 = float(raw_input("What's the next number?: "))
        old_answer = answer
        answer = operations[operation_symbol](old_answer, num3)
        message = str(old_answer) + " " + operation_symbol + " " + str(num3) + " = " + str(answer)
        print(message)

calculator()