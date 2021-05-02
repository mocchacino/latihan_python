def swapNumbersWithoutTemp(num1, num2):
    print("Before swap : {} , {}".format(num1, num2))
    # num1 = (num1 + num2) - (num2 = num1)
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    print("After Swap : {} , {}".format(num1, num2))

swapNumbersWithoutTemp(11111,77777)