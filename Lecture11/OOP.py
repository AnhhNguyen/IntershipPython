class SieuNhan:       # tao 1 class sieu nhan
	pass
snA = SieuNhan()   # khai bao doi tuong anA thuoc class sieu nhan

snA.ten = 'Sieu nhan do'   #gan gia tri cho thuoc tinh ten
snA.vu_khi = 'Kiem'
snA.mau = 'Do'

print("Ten cua sieu nhan la: ", snA.ten)
print("Vu khi cua sieu nhan la: ", snA.vu_khi)
print("Mau : ", snA.mau)

# thuoc tinh voi ham constructor
class SieuNhan:
	def __init__(self, para_ten, para_vu_khi, para_mau_sac):  #ham constructor
		self.ten = 'Sieu Nhan ' + para_ten
		self.vu_khi = para_vu_khi
		self.mau_sac = para_mau_sac

sieu_nhanA = SieuNhan("Gone", "Ho long dao", "Trang")

print("Ten cua sieu nhan la: ", sieu_nhanA.ten)
print("Vu khi cua sieu nhan la: ", sieu_nhanA.vu_khi)
print("Mau : ", sieu_nhanA.mau_sac)

# phuong thuc
class SieuNhan:
	def __init__(self, para_ten, para_vu_khi, para_mau_sac):  #ham constructor
		self.ten = 'Sieu Nhan ' + para_ten
		self.vu_khi = para_vu_khi
		self.mau_sac = para_mau_sac
	def xin_chao(self):
		return "Xin chao, ta chinh la " + self.ten

sieu_nhanA = SieuNhan("Gone", "Ho long dao", "Trang")
print(sieu_nhanA.xin_chao())