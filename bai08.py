n = input()
day_so = [int(i) for i in n.split()]
tong=sum(day_so)
day_so.sort()
print(tong)
print(tong/len(day_so))
print(day_so[-1])