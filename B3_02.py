# 1. Nhập list a và k
k = int(input("Nhập số lượng phần tử k: "))
a = []
for i in range(k):
    phan_tu = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(phan_tu)
n= int(input("Nhập số dòng n: "))
m = int(input("Nhập số cột m: "))
    
# 2. Xây dựng ma trận
if n * m != k:
    print("NO")
else:
    X = []
    for i in range(n):
        row = a[i*m : (i+1)*m]
        X.append(row)
        
# 3. In kết quả
print("Ma trận X:")
for row in X:
    print(row)