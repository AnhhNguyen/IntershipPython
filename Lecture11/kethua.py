class Truonghoc:
	Address = "Da Nang"
	def __init__(self, para_ten_lop, para_mon_hoc, para_si_so):
		self.ten = para_ten_lop
		self.mon_hoc = para_mon_hoc
		self.si_so = para_si_so
	def xin_chao(self):
		print("Xin chao, day la lop ", self.ten)

class Lop(Truonghoc):    #class con ke thua class Truong hoc
	Address = "Hue"    #thay doi thuoc tinh trong class con
	# ke thua va them moi consructor trong class con
	def __init__(self, para_ten_lop, para_mon_hoc, para_si_so, para_ten_gv):
		# goi lai thuoc tinh cua class cha
		super().__init__(para_ten_lop, para_mon_hoc, para_si_so)
		self.ten_gv = para_ten_gv


lopp = Lop("IT", "Lap trinh", 20, "Phan")
print(lopp.__dict__)
print(lopp.Address)
# ke thua thuoc tinh
lopp.xin_chao()

