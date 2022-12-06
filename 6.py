with open("input6.txt","r") as file:
    data = file.readline()
    print(data)
    stop = 0
    bufor = data[:14]
    print(bufor)
    for i in range(14,len(data)):
        bufor = bufor[1:]+data[i]
        if len(bufor) == len(set(bufor)):
            stop = i+1
            break
    print(stop)
