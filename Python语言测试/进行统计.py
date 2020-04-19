li1 = ["a", "b", "d", "d", "a", "d", "a", "e", "d", "c"]
count = {}
for i in li1:
    if not i in count:
        count[i] = 1
    else:
        count[i] += 1
print(count.items())
a = sorted(count.items(),key=lambda i:i[1])
print(a)