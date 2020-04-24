a = 'abcdisajodoenfoiasjd'
a = [a[i:i+5] for i in range(0,len(a),5)][::-1]
print(a.sort())