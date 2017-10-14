print("\tКалькулятор\n")
print("Программа поддерживает следующие операции:\n")
print("\tСложение - \"+\"")
print("\tВычитание - \"-\"")

print(" ")

def fnom2(x, stroka):
    if stroka.find("-", x + 1) == -1 and stroka.find("+", x + 1) == -1:
        nom = int(stroka[x + 1:])
    elif stroka.find("+", x + 1) < stroka.find("-", x + 1) and stroka.find("+", x + 1) != -1 or stroka.find("-", x + 1) == -1 and stroka.find("+", x + 1) > -1:
        nom = int(stroka[x + 1:stroka.find("+", x + 1)])
    elif stroka.find("+", x + 1) > stroka.find("-", x + 1) and stroka.find("-", x + 1) != -1 or stroka.find("-", x + 1) > -1 and stroka.find("+", x + 1) == -1:
        nom = int(stroka[x + 1:stroka.find("-", x + 1)])
    return nom

def fstroka(m1,nom1,stroka):
    if stroka.find("+", m1 + 1) != -1:
        stroka = stroka.replace(stroka[:stroka.find("+", m1 + 1)], str(nom1),1)
        return stroka
    elif stroka.find("-", m1 + 1) != -1:
        stroka = stroka.replace(stroka[:stroka.find("-", m1 + 1)], str(nom1),1)
        return stroka
    else:
        return str(nom1)




if __name__ == '__main__':
    stroka = input("Введите строку:")
    nom1 = None
    nom2 = None
    while stroka.isdigit() == False or stroka.find("-") != 0 and stroka[1:].isdigit() == False:
        m1 = stroka.find("+")
        m2 = stroka.find("-")

        if m2 == 0:
            if stroka[:stroka.find("-", m2 + 1)] > stroka[:stroka.find("+", m2 + 1)]:
                nom1 = int(stroka[:stroka.find("+", m2 + 1)])
                nom2 = fnom2(m1, stroka)
                nom1 += nom2
                stroka = fstroka(m1, nom1, stroka)
                print(stroka, nom1, nom2)



            elif stroka[:stroka.find("-", m2 + 1)] < stroka[:stroka.find("+", m2 + 1)]:
                nom1 = int(stroka[:stroka.find("-", m2 + 1)])
                nom2 = fnom2(m2, stroka)
                nom1 -= nom2
                m3 = stroka.find("-", m2 + 1)
                m4 = stroka.find("-", m3 + 1)
                m5 = stroka.find("+", m3 + 1)
                if m4 == -1 and m5 == -1:
                    stroka = stroka.replace(stroka[:], str(nom1),1)
                else:
                    if m4 != -1:
                        stroka = stroka.replace(stroka[:m4], str(nom1),1)
                    elif m5 != -1:
                        stroka = stroka.replace(stroka[:m5], str(nom1),1)
                print(stroka, nom1, nom2)



        elif m2 > m1 and m1 != -1 or m2 == -1:
            nom1 = int(stroka[:m1])
            nom2 = fnom2(m1,stroka)
            nom1 += nom2
            stroka = fstroka(m1,nom1,stroka)
            print(stroka, nom1, nom2)


        elif m1 > m2 and m2 != -1 or m1 == -1:
            nom1 = int(stroka[:m2])
            nom2 = fnom2(m2,stroka)
            nom1 -= nom2
            stroka = fstroka(m2,nom1,stroka)
            print(stroka, nom1, nom2)
