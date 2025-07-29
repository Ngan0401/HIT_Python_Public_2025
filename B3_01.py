# 1. Nhập list có N phần tử số nguyên
N = int(input("Nhập số lượng phần tử N: "))
danh_sach = []
for i in range(N):
    phan_tu = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach.append(phan_tu)
print("List ban đầu:", danh_sach)

# 2. Nhập X và đếm số lần xuất hiện
X = int(input("Nhập số X cần kiểm tra: "))
so_lan_xuat_hien = danh_sach.count(X)
print(f"Số {X} xuất hiện {so_lan_xuat_hien} lần trong list")

# 3. Thay thế phần tử từ vị trí 2 -> 7
thay_the = [8, 5, 4, 0, 1, 3]
danh_sach[2:8] = thay_the  
print("List sau khi thay thế:", danh_sach)

# 4. Tìm số lớn nhất và nhỏ nhất
so_lon_nhat = max(danh_sach)
so_nho_nhat = min(danh_sach)
print(f"Số lớn nhất trong list: {so_lon_nhat}")
print(f"Số nhỏ nhất trong list: {so_nho_nhat}")

# 5. Nhập Y và chèn vào đầu list
Y = int(input("Nhập số Y cần chèn vào đầu list: "))
danh_sach.insert(0, Y)
print("List sau khi chèn Y:", danh_sach)

# 6. Kiểm tra list có tăng dần, giảm dần hay không
tang_dan = all(danh_sach[i] <= danh_sach[i+1] for i in range(len(danh_sach)-1))
giam_dan = all(danh_sach[i] >= danh_sach[i+1] for i in range(len(danh_sach)-1))

if tang_dan:
    print("TĂNG")
elif giam_dan:
    print("GIẢM")
else:
    print("NO")