s = input()
mang1 = [int(x) for x in s.split()]
e = input()
mang2 = [int(x) for x in e.split()]
mangplus = mang1 + mang2
mangplus.sort()
print(mangplus)