class Student:
	def __init__(self, ho, ten):
		self.ho = ho
		self.ten = ten
# get lay gia tri ra
	@property
	def email(self):
		return self.ho + '-' + self.ten + '@gmail.com'
	@property
	def ho_va_ten(self):
		return '{} {}'.format(self.ho, self.ten)
# set gan gia tri vao
	@ho_va_ten.setter
	def ho_va_ten(self, ten_moi):
		ho_moi, ten_moi = ten_moi.split(' ')
		self.ho = ho_moi
		self.ten = ten_moi
# xoa gia tri
	@ho_va_ten.deleter
	def ho_va_ten(self):
		self.ho = None
		self.ten = None
		print('Da xoa')
# khoi tao 
hs = Student("Nguyen", "An")
# gan lai ho ten
hs.ho_va_ten = "Tran An"
# in ho ten
print(hs.ho_va_ten)
# xoa
del hs.ho_va_ten

print(hs.ho)
print(hs.ten)

	