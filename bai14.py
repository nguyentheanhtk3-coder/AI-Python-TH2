s = input()
mang = [int(x) for x in s.split()]
mangmoi = []
for i in mang:
    if i > 10:
        mangmoi.append(i)
print(mangmoi)