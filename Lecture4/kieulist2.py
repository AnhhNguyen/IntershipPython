# dem so lan xuat hien cua phan tu trong list

a = [1, 1, 2, 2, 2, 4, 4, 5, 6, 6]

b = a.count(1)

# tim xem phan tuw nam o vi tri nao trong chuoi
c = a.index(2)

#copy list nhung k lam thay doi gia tri cua list
d = a.copy()
d[0] = 'hello'

#xoa moi phhan tu trong list
g = a.clear()

a.append(4)            # them phan tu vao list, neu append list thi se them list vao a

a.extend([4, 5])      # them tung phann tu vao trong list
a.insert(1, 2)			# them phan tu 2 vao vi tri i

h = a.pop(3)			#bo di phan thu tu i va tra ve gia tri do
						# neu i bang null thi mac dinh la gia tri cuoi cung

a.remove(4)			# bo di gia tri trong ngoac
a.reverse()			#hien thi list dao nguoc
a.sort()			# sap xep theo thu tu nho den lon
a.sort(reverse= True)		# Sap xep tu lon den be, k ghi dong nghia bang False

print(a)