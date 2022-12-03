with open("input.txt","r") as file:
    dane = file.readlines()
    for i in range(len(dane)):
        dane[i]= dane[i].rstrip()
    kalorie = []
    suma = 0
    for i in range(len(dane)):
        if dane[i] != '':
            suma += int(dane[i])
        else:
            kalorie.append(suma)
            suma = 0
    kalorie.append(suma)
    print(max(kalorie))
    kalorie.sort()
    trzy = kalorie[-1] + kalorie[-2] + kalorie[-3]
    print(trzy)