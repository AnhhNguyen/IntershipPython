a = "Hello"
a += " everybody"
print(a)
print(a * 5) 

b = 'H'
print(b in a)   # phaan biet chu hoa va chu thuong nen khi ghi 'h' se cho ra ket qua la false

strc = a[6]  #xuaat ra ki tu o vi tri so 6 trong chuoi, vi tri phai la so nguyen


# lay ki tu cuoi cung trong chuoi = do dai cua chuoi - 1
print(a[len(a) -1]) #ham len xuat ra do dai cua chuoi nam trong dau ngoac don cua no

# Cach lay ki tu cua chuoi
c = a[1:5]  
c1 = a[1:len(a)]   #lay tu ki tu so 1 den het chuoi,  len(a)= None



c2 = a[7:len(a):2]   # 7 la so thu tu cua chuoi, 2 la buoc nhay, buoc nhay phai la so nguyen


#Cach lay ki tu cua chuoi tu phai sang trai
c3 = a[9:5:-1]

# Ép kiểu
d = int("7")  # d đang là chuỗi # ép kieu d thành số nguyên
print(d)
d1 = int(5.4)  # ep số thực thành số nguyên nhưng chỉ lấy phần nguyên
print(d1)

d2 = str(34)   #ép kiểu số nguyên thành chuỗi
print(d2)


#thay đổi giá trị của chuỗi
h = "hello today"
h = h[None:4] + "0" + h[5:None]
print(hash(h))