# khoi tao List

a = [1, 2, 'orange', 'apple', [1, 'black']]

b = [n for n in range(20)]

c = [[n*2, n, n*2*5] for n in range(1,4)]

d = list('Hello word')      #' hello word' la mot interable la mot cau truc tapp hop cac phan tu

#Toan tu trong list
# chuoi khong th cong vs list, chi co the cong list vs list
a += ['name', 'age']


# Toan tu nhan, chi co the nhan list len n lan
a *= 2

# Toan tu in, kiem tra xem g co trong hay k
g = 'name'  in a

h = a[3]   # lay phan tu thu 4 trong list a, phan tu bat dau tu 0
h1 = a[4][0]   # lay phan tu dau tien trong list cua phan tu thu 5 cua a
h2 = a[1:4]   # lay tu phan t u thu 2 den phan tu thu 5
h3 = a[:3]     # lay tu phan tu dau tien  den phan tu thu 4
h4 = a[2:]		#lay tu phan tu thu 3 den phan tu cuoi cung
h5 = a[::-1]	# lay tu phan tu cuoi cung den phan tu dau tien
h6 = a[::]       # lay toan bo list

# Thay doi phan tu cua list
a[3] = 7    #thay doi phan tu thu 4

print(a)