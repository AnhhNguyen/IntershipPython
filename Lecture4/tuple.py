#tuple can ban se kha giong voi list
# tuple cung co the la mot ma tran
# tuple khong cho phep thay doi noi dung, nhung list thi co the
# toc do truy xuat nhanh hon list
# dung luong bo nho nho  hon list
# bao ve du lieu khong bi thay doi

tup = (i for i in range(10) if i % 2 == 0)      
a = tuple(tup)			# phai thong qua mot bien thi range moi hien thi

# toan tu 
tu = (1, 5, 6)
tu += (4, 7)
tu *= 2
b = 2 in tu 

# lay phan tu trong tuple
c = tu[1]

d = len(tu)		#tinh do dai cua tuple

g = tu[::-1]		# dao nguoc tuple



k = tu.count(1)		# dem so lan xuat hien
k1 = tu.index(5)		# lay ra vi tri xuat hien


print(k1)