while 1:
    n = input()
    n_list = list(str(n))
    for i in range(len(n_list)):
        if n_list[i] > "1":
            n_list[i] = "1"
            if i + 1 < len(n_list):
                n_list[i+1] = "9"
    print(n_list)
    print(int("".join(n_list),2))