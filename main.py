import pandas as pd
from tabulate import tabulate
import lxml
import html5lib
import bs4
import wikipedia

import analysis

print('Привет! Вас приветствует Автоматизированная Информационно-аналитическая система викидатум!')
n = 1
while(n != 0):
    s1 = str(input("Введите то, о чем вы хотите узнать:"))
    if (s1 != ""):
        s = wikipedia.page(s1)
        df = pd.read_html(s.url)
        for i in range(len(df)):
            print(tabulate(df[i], headers="keys", tablefmt="psql"))
            b = ["да", "нет"]
            c = "/".join(b)
            print(f"Хотите ли вы сохранить данную таблицу для анализа данных?{c}")
            d = str(input("Введите ответ:"))
            if (d == b[0]):
                name = str(input("Введите название таблицы:"))
                df[i].to_csv(f"{name}.csv")
                with open("1.txt", "a+") as f:
                    f.write(f'{name}\n')
            elif (d == b[1]):
                print("OK")
            else:
                print("??????")

    else:
        print("Пусто!")

    a = ["да", "нет"]
    r = "/".join(a)
    print(f"Хотите ли вы провести анализ одной из уже имеющихся таблиц?{r}")
    l = str(input("Введите ответ:"))
    if (l == a[0]):
        analysis.csv()

    elif (l == a[1]):
        print("ОК!")

    else:
        print("Ничего непонятно! Уточните запрос!")

    ans = ["да", "нет"]
    ans_n = "/".join(ans)
    print(f"Хотите ли вы продолжить работу с данным ПО?{ans_n}")
    s = str(input("Введите ответ:"))
    if (s == ans[0]):
        n += 1
    elif (s == ans[1]):
        break
    else:
        print("Ничего непонятно")



print("Спасибо за использование!")