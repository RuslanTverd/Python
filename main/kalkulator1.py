print("\tКалькулятор\n")
print("Программа поддерживает следующие операции:\n")
print("\tСложение  - \"+\"")
print("\tВычитание - \"-\"")
print("\tИстория операций - \"h\"")
print("\tОчистить историю операций - \"с\"")
print("\tВыйти - \"q\"")
print(" ")
import csv
def kalkulator(stroka):
    nom1 = None
    nom2 = None
    z = 0  # Регулирует роботу цикла " while z != 1: "
    while z != 1:
        find_plus = stroka.find("+")  # Индекс символа " + " Если символа нет - индекс = -1
        find_minus = stroka.find("-")  # Индекс символа " - " Если символа нет - индекс = -1

        if find_minus == 0:
            if stroka[:stroka.find("-", find_minus + 1)] > stroka[:stroka.find("+", find_minus + 1)]:
                nom1 = int(stroka[:stroka.find("+", find_minus + 1)])
                nom2 = fnom2(find_plus, stroka)
                nom1 += nom2
                stroka = fstroka(find_plus, nom1, stroka)
                z = fz(stroka)  # Регулирует роботу цикла " while z != 1: "



            elif stroka[:stroka.find("-", find_minus + 1)] < stroka[:stroka.find("+", find_minus + 1)]:
                nom1 = int(stroka[:stroka.find("-", find_minus + 1)])
                nom2 = fnom2(find_minus, stroka)
                nom1 -= nom2
                m3 = stroka.find("-", find_minus + 1)
                m4 = stroka.find("-", m3 + 1)
                m5 = stroka.find("+", m3 + 1)
                if m4 == -1 and m5 == -1:
                    stroka = stroka.replace(stroka[:], str(nom1), 1)
                else:
                    if m4 != -1:
                        stroka = stroka.replace(stroka[:m4], str(nom1), 1)
                    elif m5 != -1:
                        stroka = stroka.replace(stroka[:m5], str(nom1), 1)
                z = fz(stroka)  # Регулирует роботу цикла " while z != 1: "



        elif find_minus > find_plus and find_plus != -1 or find_minus == -1:
            nom1 = int(stroka[:find_plus])
            nom2 = fnom2(find_plus, stroka)
            nom1 += nom2
            stroka = str(fstroka(find_plus, nom1, stroka))
            z = fz(stroka)  # Регулирует роботу цикла " while z != 1: "

        elif find_plus > find_minus and find_minus != -1 or find_plus == -1:
            nom1 = int(stroka[:find_minus])
            nom2 = fnom2(find_minus, stroka)
            nom1 -= nom2
            stroka = fstroka(find_minus, nom1, stroka)
            z = fz(stroka)  # Регулирует роботу цикла " while z != 1: "
    print("Отвевет:", nom1)
    return nom1

    # fnom2 - Отвечает За Создание Переменной nom2
    # Берет число после пременной nom1 и присваивает это число переменной nom2
def fnom2(find, stroka):
    if stroka.find("-", find + 1) == -1 and stroka.find("+", find + 1) == -1:
        nom = int(stroka[find + 1:])
    elif stroka.find("+", find + 1) < stroka.find("-", find + 1) and stroka.find("+", find + 1) != -1 or stroka.find("-", find + 1) == -1 and stroka.find("+", find + 1) > -1:
        nom = int(stroka[find + 1:stroka.find("+", find + 1)])
    elif find == 0 and stroka.find("-", stroka.find("-", find + 1) + 1) == -1:
        nom = int(stroka[stroka.find("-", find + 1) + 1:])
    elif find == 0:
        nom = int(stroka[stroka.find("-", find + 1) + 1:stroka.find("-", stroka.find("-", find + 1) + 1)])
    elif stroka.find("+", find + 1) > stroka.find("-", find + 1) and stroka.find("-", find + 1) != -1 or stroka.find("-", find + 1) > -1 and stroka.find("+", find + 1) == -1:
        nom = int(stroka[find + 1:stroka.find("-", find + 1)])
    return nom

    # fstroka - Заменяет в переменной stroka первые 2 числа на переменную nom1
def fstroka(find,nom1,stroka):
    if stroka.find("+", find + 1) != -1:
        stroka = stroka.replace(stroka[:stroka.find("+", find + 1)], str(nom1),1)
        return stroka
    elif stroka.find("-", find + 1) != -1:
        stroka = stroka.replace(stroka[:stroka.find("-", find + 1)], str(nom1),1)
        return stroka
    else:
        return str(nom1)

    # fz - Отвечет за работу цикла " while z != 1: "
def fz(stroka):
    if stroka.isdigit() == True:
        z = 1
        return z
    elif stroka.find("-") == 0 and stroka[1:].isdigit() == True:
        z = 1
        return z
    else:
        z = 0
        return z



if __name__ == '__main__':
    stroka = None
    history = "history.csv"
    while stroka != "q":
        stroka = input("Введите строку:")
        if stroka == "q":
            break
        elif stroka == "h":
            print("История операций\n")
            with open(history, "r", newline="") as csv_file:
                for line in csv_file.readlines():
                    print(line)
            print(" ")
        elif stroka == "c":
            with open(history, "w", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerows("")
            print("История очищена")
        else:
            kalkulator(stroka)
            with open(history, "a", newline="") as csv_file:
                str1 = [stroka]
                writer = csv.writer(csv_file)
                writer.writerow(str1)
