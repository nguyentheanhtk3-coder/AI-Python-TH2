s = input()
mang = [int(i) for i in s.split()]
nhieu_nhat = 0
for i in mang:
    n = mang.count(i);
    if n > nhieu_nhat:
        nhieu_nhat = n;
        so = i;
print(so, "voi so lan xuat hien:", nhieu_nhat)