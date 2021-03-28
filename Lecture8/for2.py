# 1 - - = 2 range(start, stop - step, step)
list(range(4, 1, -1)) 

st = [5, (1, 2, 3), {'abc', 'xyz'}]
for i in range(len(st)):
	print(st[i])

# sequence scan  // gia tri trong doi ngoai khong doi
lst = [1, 2, 3]
for value in lst:
	value += 1
print(lst)

# indexing scan // gia tri trong doi dan den ngoai doi
for value in range(len(lst)):
	lst[value] += 1
print(lst)

lt = ['--'.join((a.capitalize(), b.upper() + c.lower())) for a, b, c in [('it', 'is', 'comprehension'), ('truy', 'cap', 'nhanh hon')]]
print(lt)

# cach lam khac cham hon nhungg khong phai conprehension
lt1 = []
for a, b, c in [('It', 'is', 'not conprehension'), ('ton', 'time', 'hon')]:
	a = a.capitalize()
	b = b.upper()
	c = c.lower()
	lt1.append('--'.join((a, b + c)))
print(lt1)

# cung la conprehension
lst1 = {key:value + 1 for key, value in (('Nam', 20), ('An', 21), ('Trang', 34), ('Ngoc', 17)) if value % 2 != 0}
print(lst1)

student = ['Nam', "An", 'Trang', 'Ngoc']
for i in student:		# khi dung for
	print(i)

# su dung enumerate
gen = enumerate(student)
print(list(gen))

#su dung enumerate trong for
for iid, i in enumerate(student, 5):   # 5 la so bat dau tuy chon
	print(iid, '==>', i)