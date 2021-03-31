# su dung thuoc tinh trong lop ma k qua constructor

class SieuNhan:
	suc_manh = 50
	def __init__(self, para_ten, para_vu_khi, para_mau_sac):
		self.ten = para_ten
		self.vu_khi = para_vu_khi
		self.mau_sac = para_mau_sac

snA = SieuNhan("Sieu nhan do", "Kiem", "Do")
print(SieuNhan.suc_manh)
print(snA.suc_manh)

# cap nhap gia tri thuoc tinh thong qua lop
SieuNhan.suc_manh = 40
print(SieuNhan.suc_manh)
print(snA.suc_manh)

#cap nhap gia tri ngay trong constructor
class SieuNhan:
	so_thu_tu = 1
	suc_manh = 50
	def __init__(self, para_ten, para_vu_khi, para_mau_sac):
		self.ten = para_ten
		self.vu_khi = para_vu_khi
		self.mau_sac = para_mau_sac
		self.stt = SieuNhan.so_thu_tu
		SieuNhan.so_thu_tu += 1

snA = SieuNhan("Sieu nhan do", "Kiem", "Do")
snB = SieuNhan("Sieu nhan vang", "Bua", "Vang")

print(snA.stt)
print(snB.stt)
print(SieuNhan.so_thu_tu)

# cap nhap gia tri thuoc tinh thong qua doi tuong
snA.suc_manh = 20

print(SieuNhan.suc_manh)
print(snA.suc_manh)

# su dung thuoc tinh trong cac phuong thuc
class SieuNhan:
	suc_manh = 50
	def __init__(self, para_ten, para_vu_khi, para_mau_sac):
		self.ten = para_ten
		self.vu_khi = para_vu_khi
		self.mau_sac = para_mau_sac
	def xinchao(self):
		print("Xin chao, ta la ", self.ten)
		print("Suc manh cua ta la ", self.suc_manh)

snA = SieuNhan("Sieu nhan do", "Kiem", "Do")
snA.xinchao()