print("\tКалькулятор\n")
print("Программа поддерживает следующие операции:\n")
print("\tСложение - \"+\"")
print("\tВычитание - \"-\"")
print("\tУмножение - \"*\"")
print("\tДеление - \"/\"")
print("\tРавно - \"=\"")
print("\tВыход - \"q\"\n")

print(" ")

def plus():
    int_1 = float(input("Введеите число3:"))
    plus = otv + int_1
    return plus

def minus():
    int_1 = float(input("Введеите число4:"))
    minus = otv - int_1
    return minus

def multiply():
    int_1 = float(input("Введеите число5:"))
    multiply = otv * int_1
    return multiply

def division():
    int_1 = float(input("Введеите число6:"))
    division = otv / int_1
    return division

operation = None
otv = float(input("Введеите число1:"))

while operation != "q":
    operation = input("Введите операцию:")
    if operation == "=":
        print("\nВаш ответ:", otv)
        print(" ")
        otv = float(input("Введеите число2:"))
    elif operation == "q":
        print(" ")
    elif operation == "+" or operation == "-" or operation == "*" or operation == "/":
        if operation == "+":
            plus()
            otv = plus()
        elif operation == "-":
            minus()
            otv = minus()
        elif operation == "*":
            multiply()
            otv = multiply()
        elif operation == "/":
            division()
            otv = division()
    else:
        print("Вы ввели не правильную операцию")
        otv = float(input("Введеите число1:"))









