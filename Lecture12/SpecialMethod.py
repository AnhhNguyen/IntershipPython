class Truonghoc():
	Address = "Da Nang"
# cau truc cua special la __ten__
	def __init__(self, para_ten, para_phong):
		self.ten = para_ten
		self.phong = para_phong
	def __str__(self):  # co tac dung giup in ra ro rang thong tin
		return 'Day la {}, co {} phong'.format(self.ten, self.phong)
	def __repr__(self):
		return 'ten: {}\nso phong: {}'.format(self.ten, self.phong)
	def __len__(self):
		return len(self.ten)
	def __add__(self, truong_hai):
		return self.Address + truong_hai.Address

truong = Truonghoc('Dai Hoc', 20)
lop = Truonghoc("Cao Dang", 10)
# ham s se luon duoc uu tien hon ham r
print(truong)
print('%s' %truong)
print('%r' %truong)
print(Truonghoc.__len__(truong))
print(Truonghoc.__add__(truong, lop))

# ham len cung la special method
s = "Dai Hocc"
print(len(s))
print(s.__len__())