# # # tao vong lap while voi iternable
length = 4
iter_ = (x for x in range(length))
c = 0

while c < length:
	print(next(iter_))
	c += 1

# # cach de dung 1 vong lap voi dieu kien luon dung
while 1:
	try:
		print(next(iter_))
	except StopIteration:
		break
iner = (x for x in range(3))
inter = ([1, 2, 3], [4, 5, 6], [7, 6, 9])

for value, value1, value2 in inter:
	print('==', value)

s = 'Nguyen An'

for ch in s:
	if ch == ' ':
		continue   # neu gap dieu kien if van se tiep tuc
		#break  # neu gap dieu kien if se dung lai
	else:
		print(ch)


# for else la khi thuc hien xong vong lap thi se thuc hien else
for k in (1, 2, 3, 4):
	if k % 2 == 0:
		continue
	print(k)
else:
	print('Done!')

# tinh tong cac so 
set_ = {5, 8, 1, 9, 4}
sum = 0
for k in set_:
	sum = sum + k
else:
	print(sum)