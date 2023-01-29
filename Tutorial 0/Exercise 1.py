number1 = 20
number2 = 30

def calculate(num1, num2):
    multiplication = num1 * num2
    sum = num1 + num2
    if multiplication < 1000:
        print(multiplication)
    else:
        print(sum)

calculate(number1, number2)