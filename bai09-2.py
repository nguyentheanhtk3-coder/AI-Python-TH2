#loai bo cac phan tu trung nhau trong mang, in ra theo thu tu xuat hien
s = input()
mang = [int(i) for i in s.split()]
danh_sach = {}
mang_moi = []
for i in mang:
    danh_sach[i] = danh_sach.get(i, 0) + 1
    if danh_sach[i] == 1:
        mang_moi.append(i)
print(mang_moi)