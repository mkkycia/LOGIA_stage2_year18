def sciezka(start, lista, pom2 = []):
    odwiedzone = []
    dalej = [e[0] for e in lista]
    wsk = start
    while True:
        if wsk in odwiedzone:
            return odwiedzone
        if wsk in pom2:
            odwiedzone.append(wsk)
            return odwiedzone
        else:
            if wsk in dalej:
                nr = dalej.index(wsk)
                odwiedzone.append(wsk)
                wsk = lista[nr][1]
            else:
                odwiedzone.append(wsk)
                return odwiedzone

def droga(lista,starta="A",startb="Z"):
    x = sciezka(starta,lista)
    y = sciezka(startb,lista,x)
    if y[-1] in x:
        a = sciezka(startb,lista)
        b = sciezka(starta,lista, a)
        odl = x.index(y[-1])
        odl1 = a.index(b[-1])
        return min(odl+len(y)-1,odl1+len(b)-1)
    else:
        return -1
