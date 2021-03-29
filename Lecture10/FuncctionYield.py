# khi su dung return
# ta phai tao mot list de return tra gia tri ve

def square(lst):
	sq_lst = []
	for num in lst:
		sq_lst.append(num ** 2)
	return sq_lst

stu = square([1, 2, 3, 4])
for value in stu:
	print(value)


# khi su dung yield
# yield se truc tiep chay vao va sinh ra gia tri cho ham
def square(lst):
	for num in lst:
		yield num ** 2

stu = square([1, 2, 3, 4])
for value in stu:
	print(value)

#khi su dung yeild
# khi yeu cau thi yield ms sinh ra lenh

def gen():
	for value in range(3):
		print('yield', value + 1, 'times')
		yield value

for value in gen():
	print(value)


def gen():
	yield 'Hello'
	print('this is the second yield')
	yield 'Student'
	print('this is the last yield')
	yield 'Da Nang'
	print('Will not return anything')

for value in gen():
	print(value)

def gen():
	while True:
		x = yield   # gia tri yield dang la none
		yield x ** 2

g = gen()
print(next(g))    # tai vi lay gia tri yield nen van con la none
print(g.send(2))	# send(gui) gia tri 2 vao yield
print(next(g))
print(g.send(10))