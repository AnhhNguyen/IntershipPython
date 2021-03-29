ave = lambda a, b, c: (a + b + c)/3

print(ave(1, 3, 2))

# su dung lambda voi defaut argument
x_power_a = lambda x, a = 2: x ** a
print(x_power_a(2, 5))

def student():
	mem = lambda x: x + ' is a member of IT'
	return mem

call_mem = student()
print(call_mem('An'))
print(call_mem)

# su dung nhieu lambda
student = [lambda x: x ** 2, lambda x: x**3, lambda x: x**4]
for func in student:
	print(func(3))

# su dung cho dic
key = 'student'
print({'Google': lambda: 'Goooo', 'YouTube': lambda: 'Youuuuu', 'student': lambda: 'class IT'}[key]())

# su dung lambda trong cau lenh if
find_greater = lambda x, y: x if x > y else y  # neu x > y thi thuc hien x, con k thi y
print(find_greater(1, 2))

# tim uoc chung cua 3 va 2
cd_of_2_3 = lambda x: (1 if x % 3 == 0 else 0) if x % 2 == 0 else 0
print(cd_of_2_3(6))

# thu gon bieu thuc
cd_of_2_3 = lambda x: (1 if not (x % 3) else 0) if not (x % 2) else 0
print(cd_of_2_3(6))


# su dung lambda trong def
def student(first_string):
	return lambda second_string: first_string + second_string
slogan = student('Hello ')
print(slogan('Da Nang'))