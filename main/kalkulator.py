print("\tКалькулятор\n")
print("Программа поддерживает следующие операции:\n")
print("\tСложение - \"+\"")
print("\tВычитание - \"-\"")
print("\tУмножение - \"*\"")
print("\tДеление - \"/\"")
print("\tРавно - \"=\"")
print("\tВыход - \"q\"\n")

print(" ")

def plus(x, y):
    return x+y

def minus(x, y):
    return x-y

def multiply(x, y):
    return x*y

def division(x, y):
    return x/y

operation = None
otv = float(input("Введеите число:"))

if __name__ == '__main__':
    while operation != "q":
        operation = input("Введите операцию:")
        if operation == "=":
            print("\nВаш ответ:", otv)
            print(" ")
            otv = float(input("Введеите число:"))
        elif operation == "q":
            break
        elif operation == "+" or operation == "-" or operation == "*" or operation == "/":
            int_1 = float(input("Введеите число:"))
            if operation == "+":
                otv = plus(otv, int_1)
            elif operation == "-":
                otv = minus(otv, int_1)
            elif operation == "*":
                otv = multiply(otv, int_1)
            elif operation == "/":
                otv = division(otv, int_1)
        else:
            print("Вы ввели не правильную операцию")








