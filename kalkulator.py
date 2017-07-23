print("\tКалькулятор\n")
print("Программа поддерживает следующие операции:\n")
print("\tСложение - \"+\"")
print("\tВычитание - \"-\"")
print("\tУмножение - \"*\"")
print("\tДеление - \"/\"")
print("\tРавно - \"=\"")
print("\tВыход - \"q\"\n")

operation = 0
print(" ")
otv = float(input("Введеите число:"))
while operation != "q":
    operation = input("Введите операцию:")
    if operation == "+":
        int_1 = float(input("Введеите число:"))
        otv += int_1
    elif operation == "-":
        int_1 = float(input("Введеите число:"))
        otv -= int_1
    elif operation == "*":
        int_1 = float(input("Введеите число:"))
        otv *= int_1
    elif operation == "/":
        int_1 = float(input("Введеите число:"))
        otv /= int_1
    elif operation == "q":
        print("")
    elif operation == "=":
        print("\nВаш ответ:", otv)
        print(" ")
        otv = float(input("Введеите число:"))
    else:
        print("Вы ввели не правильную операцию")






