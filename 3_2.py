with open("input3.txt","r") as file:
    data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].rstrip()
    data_divided = []
    sum_of_priorities = 0
    for i in range(0,len(data)-2,3):
        threesome = []
        threesome.append(data[i])
        threesome.append(data[i+1])
        threesome.append(data[i+2])
        data_divided.append(threesome)
    for i in range(len(data_divided)):
        for letter in data_divided[i][0]:
            if letter in data_divided[i][1] and letter in data_divided[i][2]:
                if ord(letter) >= 97:
                    sum_of_priorities += ord(letter) - 96
                else:
                    sum_of_priorities += ord(letter) - 38
                break
    print(sum_of_priorities)

