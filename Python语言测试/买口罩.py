import sys
for line in sys.stdin:
    money = int(line)
    price = [1, 2, 2, 5, 2 , 3]
    nums = [5, 3, 3, 4, 2, 1]
    numsGet = 0
    while money >= price[0] or (len(price)>1 and money >= price[1]):
        if money >= price[0]:
            money -= price.pop(0)
            numsGet += nums.pop(0)
            continue
        if money >= price[1]:
            money -= price.pop(1)
            numsGet += nums.pop(1)
            continue
    print(numsGet)

