def operation():
    operation = 0
    print(" ")
    otv = float(input("Введеите число:"))
    while operation != "q":
        operation = input("Введите операцию:")
        if operation == "+":
            int_1 = float(input("Введеите число:"))
            otv += int_1

if  __name__ ==  "__main__" :