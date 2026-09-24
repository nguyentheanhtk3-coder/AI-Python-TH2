arr = input().strip()
for i in range(len(arr)):
    if arr[i] != arr[-(i+1)]:
        print("Không đối xứng")
        break
else:
    print("Đối xứng")