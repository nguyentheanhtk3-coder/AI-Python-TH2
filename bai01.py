arr = input().strip()
print(len(arr))
dem_ky_tu = {} #Xai thu vien de dem so lan xuat hien cua tung ky tu
for kt in arr:
    dem_ky_tu[kt] = dem_ky_tu.get(kt, 0) + 1
for kt, so_lan in dem_ky_tu.items():
    print(f"{kt}: {so_lan}")