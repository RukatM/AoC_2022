
with open("input2.txt","r") as file:
    data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].rstrip().split()
    # print(data)
    wynik = 0
    for i in range(len(data)):
        if data[i][1] == 'X':
            wynik += 1
            if data[i][0] == 'A':
                wynik += 3
            elif data[i][0] == 'C':
                wynik += 6
        elif data[i][1] == 'Y':
            wynik += 2
            if data[i][0] == 'B':
                wynik += 3
            elif data[i][0] == 'A':
                wynik += 6
        else:
            wynik += 3
            if  data[i][0] == 'C':
                wynik += 3
            elif data[i][0] == 'B':
                wynik += 6


    print(wynik)