with open("input4.txt","r") as file:
    data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].rstrip().split(",")
        data[i][0] = data[i][0].split("-")
        data[i][1] = data[i][1].split("-")
    # print(data)
    data_fixed = []
    for data_line in data:
        line = []
        for data_pair in data_line:
            list = []
            for i in range(int(data_pair[0]),int(data_pair[1])+1):
                list.append(i)
            line.append(list)
        data_fixed.append(line)
    # print(data_fixed)
    sum = 0
    for data_line in data_fixed:
        if all(i in data_line[0] for i in data_line[1]) or all(i in data_line[1] for i in data_line[0]):
            sum += 1

    print(sum)