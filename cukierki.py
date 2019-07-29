def ilerazy(liczba, lista):
    for i in range(len(lista)):
        if i % 2 == 1:
            lista[i] = -lista[i]
    a = [0]
    for i in range(len(lista)):
        for j in range(abs(lista[i])):
            if lista[i] > 0:
                a.append(a[-1] + 1)
            else:
                a.append(a[-1] - 1)
    wynik = 0
    for i in a:
        if i == liczba:
            wynik += 1
    return wynik

print(ilerazy(2, [3, 2]))
        
