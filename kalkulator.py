print("\tКалькулятор\n")
print("Программа поддерживает следующие операции:\n")
print("\tсложение - \"+\"")
print("\tвычитание - \"-\"")
print("\tумножение - \"*\"")
print("\tделение - \"/\"\n")

int_1 = float(input("Введеите число:"))
operation = input("Введите операцию:")
int_2 = float(input("Введите второе число:"))
print(" ")
if operation == "+":
    otvet = int_1 + int_2
    print("Ваш ответ:", otvet)
elif operation == "-":
    otvet = int_1 - int_2
    print("Ваш ответ:", otvet)
elif operation == "*":
    otvet = int_1 * int_2
    print("Ваш ответ:", otvet)
elif operation == "/":
    otvet = int_1 / int_2
    print("Ваш ответ:", otvet)
else:
    print("Вы ввели не правильную операцию")

input("\nНажмите Enter чтобы выйти")



