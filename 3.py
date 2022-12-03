with open("input3.txt","r") as file:
    data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].rstrip()
    data_fixed = []
    for i in range(len(data)):
        pair = []
        word1 = data[i][:int(len(data[i])/2)]
        word2 = data[i][int(len(data[i])/2):]
        pair.append(word1)
        pair.append(word2)
        data_fixed.append(pair)
    sum_of_priorities = 0
    for i in range(len(data_fixed)):
        for letter in data_fixed[i][0]:
            if letter in data_fixed[i][1]:
                if ord(letter) >= 97:
                    sum_of_priorities += ord(letter) - 96
                else:
                    sum_of_priorities += ord(letter) - 38
                break
    print(sum_of_priorities)



