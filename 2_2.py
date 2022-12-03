with open("input2.txt","r") as file:
    data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].rstrip().split()
    print(data)
    wynik = 0
    for i in range(len(data)):
        if data[i][1] == 'X':
            if data[i][0] == 'A':
                wynik += 3
            elif data[i][0] == 'B':
                wynik += 1
            else:
                wynik += 2
        elif data[i][1] == 'Y':
            wynik += 3
            if data[i][0] == 'A':
                wynik += 1
            elif data[i][0] == 'B':
                wynik += 2
            else:
                wynik += 3
        else:
            wynik += 6
            if  data[i][0] == 'A':
                wynik += 2
            elif data[i][0] == 'B':
                wynik += 3
            else:
                wynik +=1
    print(wynik)