def dem_ky_tu_va_do_dai():
    # Nhập chuỗi từ bàn phím
    chuoi = input("Nhập vào một chuỗi: ")
    
    # 1. In ra độ dài chuỗi
    do_dai = len(chuoi)
    print(f"Độ dài của chuỗi là: {do_dai}")
    
    # 2. Đếm số lần xuất hiện của mỗi ký tự
    bang_dem = {}
    for ky_tu in chuoi:
        bang_dem[ky_tu] = bang_dem.get(ky_tu, 0) + 1
        
    # In kết quả số lần xuất hiện
    print("Số lần xuất hiện của mỗi ký tự:")
    for ky_tu, so_lan in bang_dem.items():
        print(f" - Ký tự '{ky_tu}': {so_lan} lần")

# Chạy chương trình
if __name__ == "__main__":
    dem_ky_tu_va_do_dai()