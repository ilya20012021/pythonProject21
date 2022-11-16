import sys

import pandas as pd
from tabulate import tabulate

def csv():
    s = open("1.txt","r").readlines()
    v = "".join(s)
    u = v.split()
    print(u)
    h = str(input("Введите название таблицы для работы:"))
    if(h in u):
        mas = ["выбрать все данные(кнопка 1)","выбрать данные по условию столбца(кнопка 2)","выбрать данные по условиям столбца(кнопка 3)","создать новый столбец с данными(кнопка 4)","внести данные(кнопка 5)"]
        mas1 = "/".join(mas)
        print(f"Сделайте выбор:{mas1}")
        num = str(input("Нажмите на кнопку:"))
        if(num == "1"):
            df = pd.read_csv(f"{h}.csv")
            print(tabulate(df,headers="keys",tablefmt="psql"))
        elif(num == "2"):
            df = pd.read_csv(f"{h}.csv")
            print(tabulate(df, headers="keys", tablefmt="psql"))
            print("----------------------------------------------")
            c = str(input("Введите столбец для дальнейшей работы:"))
            if(c == "" or c not in df):
                print("Столбец не введен или отсутствует!")
            elif(c != ""):
                s = str(input("Введите знак:"))
                if(s != ""):
                    if (s == ">"):
                        r = int(input("Введите значение:"))
                        d = df[df[f"{c}"] > f"{r}"]
                        print(tabulate(d, headers="keys", tablefmt="psql"))
                    elif (s == ">="):
                        r = int(input("Введите значение:"))
                        d = df[df[f"{c}"] >= f"{r}"]
                        print(tabulate(d, headers="keys", tablefmt="psql"))
                    elif (s == "<"):
                        r = int(input("Введите значение:"))
                        d = df[df[f"{c}"] < f"{r}"]
                        print(tabulate(d, headers="keys", tablefmt="psql"))
                    elif (s == "<="):
                        r = int(input("Введите значение:"))
                        d = df[df[f"{c}"] <= f"{r}"]
                        print(tabulate(d, headers="keys", tablefmt="psql"))
                    elif (s == "=="):
                        mass = ["строка","число"]
                        mass_n = "/".join(mass)
                        print(f"Выберите, с чем вы работаете:{mass_n}")
                        res = str(input())
                        if(res == mass[1]):
                            r1 = [int(i) for i in input("Введите значения:").split()]
                            d = df[df[f"{c}"].isin(r1)]
                            print(tabulate(d, headers="keys", tablefmt="psql"))
                        if (res == mass[0]):
                            r1 = [i for i in input("Введите значения:").split()]
                            d  = df[df[f"{c}"].isin(r1)]
                            print(tabulate(d, headers="keys", tablefmt="psql"))
                    else:
                        print("Попробуйте еще раз!")
                else:
                    print("Знак не введен!")
        elif(num == "4"):
            p = []
            df = pd.read_csv(f"{h}.csv")
            print(df)
            for i in range(len(df)):
                y = str(input("Введите значение:"))
                p.append(y)
            n = str(input("Введите название столбца:"))
            df[f"{n}"] = p
            print(tabulate(df, headers="keys", tablefmt="psql"))
            name = str(input("Озаглавьте таблицу:"))
            with open("1.txt","a+") as f:
                f.write(f'{name} \n')
            df.to_csv(f"{name}.csv")

        elif(num == "5"):
            df = pd.read_csv(f"{h}.csv")
            print(tabulate(df, headers="keys", tablefmt="psql"))
            print("-------------------------------------------")
            mas_1 = list(df.keys())
            print("-------------------------------------------")
            print(mas_1)
            mas_2 = [i for i in input("Введите значения:").split()]
            if(len(mas_1) == len(mas_2)):
                d = dict(zip(mas_1, mas_2))
                df = df.append(d, ignore_index=True)
                print(df)
                name = str(input("Озаглавьте таблицу:"))
                with open("1.txt", "a+") as f:
                    f.write(f'{name}  \n')
                df.to_csv(f"{name}.csv")
            else:
                print("Несовпадение размеров!")

        elif (num == "3"):
            n = 1
            for i in range(n):
                df = pd.read_csv(f"{h}.csv")
                print(tabulate(df, headers="keys", tablefmt="psql"))
                print("----------------------------------------------")
                c = str(input("Введите столбец для дальнейшей работы:"))
                if (c == "" or c not in df):
                    print("Столбец не введен или отсутствует!")
                    break
                if (c != ""):
                    s = str(input("Введите знак:"))
                    if (s != ""):
                        if (s == ">"):
                            r = int(input("Введите значение:"))
                            d = df[df[f"{c}"] > f"{r}"]
                            print(tabulate(d, headers="keys", tablefmt="psql"))
                            dd = pd.DataFrame(d)
                            name = str(input("Озаглавьте таблицу:"))
                            with open("1.txt", "a+") as f:
                                f.write(f'{name}  \n')
                            dd.to_csv(f"{name}.csv")
                        elif (s == ">="):
                            r = int(input("Введите значение:"))
                            d = df[df[f"{c}"] >= f"{r}"]
                            print(tabulate(d, headers="keys", tablefmt="psql"))
                            dd = pd.DataFrame(d)
                            name = str(input("Озаглавьте таблицу:"))
                            with open("1.txt", "a+") as f:
                                f.write(f'{name}  \n')
                            dd.to_csv(f"{name}.csv")
                        elif (s == "<"):
                            r = int(input("Введите значение:"))
                            d = df[df[f"{c}"] < f"{r}"]
                            print(tabulate(d, headers="keys", tablefmt="psql"))
                            dd = pd.DataFrame(d)
                            name = str(input("Озаглавьте таблицу:"))
                            with open("1.txt", "a+") as f:
                                f.write(f'{name}  \n')
                            dd.to_csv(f"{name}.csv")
                        elif (s == "<="):
                            r = int(input("Введите значение:"))
                            d = df[df[f"{c}"] <= f"{r}"]
                            print(tabulate(d, headers="keys", tablefmt="psql"))
                            dd = pd.DataFrame(d)
                            name = str(input("Озаглавьте таблицу:"))
                            with open("1.txt", "a+") as f:
                                f.write(f'{name}  \n')
                            dd.to_csv(f"{name}.csv")
                        elif (s == "=="):
                            mass = ["строка", "число"]
                            mass_n = "/".join(mass)
                            print(f"Выберите, с чем вы работаете:{mass_n}")
                            res = str(input())
                            if (res == mass[1]):
                                r1 = [int(i) for i in input("Введите значения:").split()]
                                d = df[df[f"{c}"].isin(r1)]
                                print(tabulate(d, headers="keys", tablefmt="psql"))
                                dd = pd.DataFrame(d)
                                name = str(input("Озаглавьте таблицу:"))
                                with open("1.txt", "a+") as f:
                                    f.write(f'{name}  \n')
                                dd.to_csv(f"{name}.csv")
                            if (res == mass[0]):
                                r1 = [i for i in input("Введите значения:").split()]
                                d = df[df[f"{c}"].isin(r1)]
                                print(tabulate(d, headers="keys", tablefmt="psql"))
                                dd = pd.DataFrame(d)
                                name = str(input("Озаглавьте таблицу:"))
                                with open("1.txt", "a+") as f:
                                    f.write(f'{name}  \n')
                                dd.to_csv(f"{name}.csv")
                        else:
                            print("Попробуйте еще раз!")
                    else:
                        print("Знак не введен!")

        else:
            print("????????")


    else:
        print("Такой таблицы нет! Пока")
