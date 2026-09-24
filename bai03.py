arr = input().strip()
so_nguyen_am = 0
for i in arr:
    if i in 'aeiouAEIOU':
        so_nguyen_am += 1
print(f"Số nguyên âm: {so_nguyen_am}")
print(f"Số phụ âm: {len(arr) - so_nguyen_am}")