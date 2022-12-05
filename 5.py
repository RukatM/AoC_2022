with open("input5_1.txt","r") as file:
    data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].rstrip()
        data[i] = data[i].split(" ")
    print(data)
    data_fixed = []
    maxlen = 0
    for line in data:
        if len(line) > maxlen:
            maxlen = len(line)
    print(maxlen)
    for line in data:
        counter = 0
        line_fixed = []
        for char in line:
            if char == '':
                counter += 1
                if counter == 4:
                    line_fixed.append('')
                    counter = 0
            else:
                line_fixed.append(char[1])
        if len(line) != maxlen:
            line_fixed.append('')
        data_fixed.append(line_fixed)
    # print(data_fixed)
    kolumny = []
    for i in range(len(data_fixed[0])):
        kolumna = []
        for j in range(len(data_fixed)):
            if data_fixed[j][i] != "":
                kolumna.append(data_fixed[j][i])
        kolumny.append(kolumna)
    print(kolumny)
    with open("input5_2.txt","r") as file2:
        orders = file2.readlines()
        for i in range(len(orders)):
            orders[i]=orders[i].rstrip()
        orders_fixed = []
        for i in range(len(orders)):
            order_f = []
            orders[i] = orders[i].split()
            order_f.append(int(orders[i][1]))
            order_f.append(int(orders[i][3]))
            order_f.append(int(orders[i][5]))
            order_f[1] -= 1
            order_f[2] -= 1
            orders_fixed.append(order_f)
        print(orders_fixed)
        for i in range(len(orders_fixed)):
            temp = []
            for j in range(orders_fixed[i][0]):
                # print(kolumny[orders_fixed[i][1]][0])
                temp.append(kolumny[orders_fixed[i][1]][0])
                # print(temp)
                kolumny[orders_fixed[i][1]].pop(0)
                # print(kolumny[orders_fixed[i][1]])
            # temp = temp[::-1]
            temp.extend(kolumny[orders_fixed[i][2]])
            # print(temp)
            # print(kolumny[orders_fixed[i][2]])
            kolumny[orders_fixed[i][2]] = temp
            print(kolumny)
            # print(kolumny[orders_fixed[i][2]])
            # print()
        haslo = ''
        for i in range(len(kolumny)):
            print(kolumny[i])
            haslo += kolumny[i][0]
        print(haslo)