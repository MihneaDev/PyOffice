def main():
    operator = input("Are you (A)dding, (S)ubtracting, (M)ultiplyng, or (D)ividing? ")
    firstNum = int(input("Enter your first number: "))
    secondNum = int(input("Enter your second number: "))
    if operator.lower() == "a":
        print(firstNum + secondNum)
    elif operator.lower() == "s":
        print(firstNum - secondNum)
    elif operator.lower() == "m":
        print(firstNum * secondNum)
    elif operator.lower() == "d":
        print(firstNum / secondNum)
