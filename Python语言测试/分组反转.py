a = 'abcdisajodoenfoiasjd'
a = [a[i:i+5] for i in range(0,len(a),5)][::-1]
print(a.sort())






a = {'1':1,'4':4,'5':5,'0':0}
a = sorted(a,key= lambda i:a[i])
print(a)