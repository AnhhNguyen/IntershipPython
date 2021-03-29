# Ham ho tro trong python

# ham map, cau truc
def mymap(func, iterable):
	for x in iterable:      # di tung phan tu trong ds iterable
		yield func(x)

def inc(x): return x + 1
student = [1, 2, 3, 4]

print(list(map(inc, student)))   # ham map tra ve gia tri return tu ds student

# su dung vs lambda
student = [1, 2, 3, 4]
print(list(map(lambda x: x + 1, student)))

# list comprehension
inc = lambda x: x + 1
student = [1, 2, 3, 4]

print([inc(x) for x in student])

func = lambda x, y: x + y
student_1 = [1, 3, 5, 7]
student_2 = [2, 3, 4, 8]
student = map(func, student_1, student_2)   #tra ve func duyet qua student1 va student2

print(list(student))

# ham filter lay tung gia tri de loc
# gia tri chuyen qua boolean la True thi ms tra ve generater
func = lambda x: x > 0
student = [1, -2, 4,0, -9, 3, 6, 8]

print(list(filter(func, student)))    # tra ve func neu true, duyet trong danh sach student
# su dung comprehension
print([x for x in student if x > 0])

# ham filter khi dua vao la none
print(list(filter(None, student))) 

# ham reduce
## gia tri chuyen qua boolean la False thi k dc tra ve mot gia tri
from functools import reduce

student_add = lambda x, y: x + y
student_muti = lambda x, y: x * y

student = [1, 2, 3, 4]
print(reduce(student_add, student))  # reduce se lay gia tri 1 + 2, sau do lay 3 + 3, roi lay 6 + 4
print(reduce(student_muti, student))  # nhan tuong tu

# neu them gia tri argument vao thi reduce se lay 10 + 1, 11 + 2, 13 + 3, 16 + 4
# nhan tuong tu
print(reduce(student_add, student,10))  
print(reduce(student_muti, student,10))