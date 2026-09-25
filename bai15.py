doan = input().split()
#xoa dau cau
for tu in range(len(doan)):
    if '.' in doan[tu] or ',' in doan[tu] or '!' in doan[tu] or '?' in doan[tu]:
        n = len(doan[tu])
        doan[tu] = doan[tu][:(n-1)]
print(doan)
#dem so lan xuat hien
so_lan = {}
for i in doan:
    so_lan[i] = so_lan.get(i, 0) + 1
for i,j in so_lan.items():
    print(f"{i}: {j}")
#sap xep danh sach tu theo tan suat giam dan?