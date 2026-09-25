s = input()
mang = [int(x) for x in s.split()]
tong = 0;
for i in mang:
    if i % 2 == 0:
        tong+=i
print(tong)