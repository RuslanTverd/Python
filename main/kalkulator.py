print("\tКалькулятор\n")
print("Программа поддерживает следующие операции:\n")
print("\tСложение - \"+\"")
print("\tВычитание - \"-\"")
print("\tУмножение - \"*\"")
print("\tДеление - \"/\"")
print("\tРавно - \"=\"")
print("\tВыход - \"q\"\n")


print(" ")

operation = None
otv = float(input("Введеите число:"))
while operation != "q":
    operation = input("Введите операцию:")
    if operation == "+":
        int_1 = float(input("Введеите число:"))
        def plus():
            plus = otv + int_1
            return plus
        otv = plus()
    elif operation == "-":
        int_1 = float(input("Введеите число:"))
        def minus():
            minus = otv - int_1
            return minus
        otv = minus()
    elif operation == "*":
        int_1 = float(input("Введеите число:"))
        def multiply():
            multiply = otv * int_1
            return multiply
        otv = multiply()
    elif operation == "/":
        int_1 = float(input("Введеите число:"))
        def division():
            division = otv / int_1
            return division
        otv = division()
    elif operation == "q":
        print("")
    elif operation == "=":
        print("\nВаш ответ:", otv)
        print(" ")
        otv = float(input("Введеите число:"))
    else:
        print("Вы ввели не правильную операцию")



def addition(x,y):
    return x+y


