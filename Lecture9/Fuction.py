# khai bao ham
def student(name, add):
	print(name)
	print(add)

student('An', 'Hue')

#co the truyen vao gia tri defau
Age = '20'
def student(name, add = 'Da Nang', age = Age):
	print(name)
	print(add)
	print(age)

student('Hoa')
student('Huong', 'Hue')

# thay doi gia tri trong ham
def st(student =[]):
	student.append('A')   # cu moi lan goi ham thi se them gia tri vao trong bien
	print(student)
st()
st()