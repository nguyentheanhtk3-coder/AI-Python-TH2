#loai bo cac phan tu trung nhau trong mang, in ra theo thu tu tang dan
n = input()
mang = [int(i) for i in n.split()]
mang.sort()
i = 0
while i < len(mang) - 1:
    if mang[i] == mang[i + 1]:
        mang.remove(mang[i])
    else:
        i += 1
print(mang)