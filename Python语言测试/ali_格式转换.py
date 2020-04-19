def formatConvert():
    title = True
    data = {}
    with open('text.txt','r') as f:
        for i in f:
            if title:
                print("time       cpu0_col1 cpu0_col3 cpu0_col10 cpu6_col1 cpu6_col3 cpu6_col10 cpu8_col1 cpu8_col3 cpu8_col10")
                title = False
            else:
                strArr = i.split()
                time_ = strArr[0]+strArr[1]
                if not time_ in data:
                    data[time_] = ['0']*9
                if strArr[2] == '0':
                    data[time_][0] = strArr[3]
                    data[time_][1] = strArr[5]
                    data[time_][2] = strArr[12]
                if strArr[2] == '6':
                    data[time_][3] = strArr[3]
                    data[time_][4] = strArr[5]
                    data[time_][5] = strArr[12]
                if strArr[2] == '8':
                    data[time_][6] = strArr[3]
                    data[time_][7] = strArr[5]
                    data[time_][8] = strArr[12]
    for i in data:
        print(" ".join(data[i]))

formatConvert()