from turtle import *


def zamien(litera, slowo):
    liczba = 0
    if litera == 'a':
        liczba = 1
    elif litera == 'b':
        liczba = 2
    elif litera == 'c':
        liczba = 3
    elif litera == 'd':
        liczba = 4
    elif litera == 'e':
        liczba = 5
    elif litera == 'f':
        liczba = 2
    elif litera == 'g':
        liczba = 3
    elif litera == 'h':
        liczba = 4
    elif litera == 'i' or litera == 'j':
        liczba = 5
    elif litera == 'k':
        liczba = 6
    elif litera == 'l':
        liczba = 3
    elif litera == 'm':
        liczba = 4
    elif litera == 'n':
        liczba = 5
    elif litera == 'o':
        liczba = 6
    elif litera == 'p':
        liczba = 7
    elif litera == 'q':
        liczba = 4
    elif litera == 'r':
        liczba = 5
    elif litera == 's':
        liczba = 6
    elif litera == 't':
        liczba = 7
    elif litera == 'u':
        liczba = 8
    elif litera == 'v':
        liczba = 5
    elif litera == 'w':
        liczba = 6
    elif litera == 'x':
        liczba = 7
    elif litera == 'y':
        liczba = 8
    elif litera == 'z':
        liczba = 9
    a = 0
    for i in range(liczba):
        fd(780 / len(slowo) - 4 * i)
        lt(90)
        a = 780 / len(slowo) - 4 * i
    for i in range(liczba):
        rt(90)
        bk(a + 4 * i)
    pu()
    fd(6/5 * 780 / len(slowo))
    pd()

def koduj(slowo):
    speed(0)
    pu()
    bk(390)
    lt(90)
    bk(780 / len(slowo) - 2)
    rt(90)
    pd()
    for i in slowo:
        zamien(i, slowo)


koduj("fghjastuz")
