print("\tКалькулятор\n")
print("Программа поддерживает следующие операции:\n")
print("\tсложение")
print("\tвычитание")
print("\tумножение")
print("\tделение\n")

int_1 = int(input("Введеите число:"))
operation = input("Введите операцию:")
int_2 = int(input("Введите второе число:"))
print(" ")
if operation == "сложение":
    otvet = int_1 + int_2
    print("Ваш ответ:", otvet)
elif operation == "вычитание":
    otvet = int_1 - int_2
    print("Ваш ответ:", otvet)
elif operation == "умножение":
    otvet = int_1 * int_2
    print("Ваш ответ:", otvet)
elif operation == "деление":
    otvet = int_1 / int_2
    print("Ваш ответ:", otvet)
else:
    print("Вы ввели не правильную операцию")

input("\nНажмите Enter чтобы выйти")



