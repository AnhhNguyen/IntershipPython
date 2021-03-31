class SieuNhan:
	suc_manh = 50
	def __init__(self, para_ten, para_vu_khi, para_mau_sac):
		self.ten = para_ten
		self.vu_khi = para_vu_khi
		self.mau_sac = para_mau_sac

	@classmethod
	def cap_nhap_suc_manh(cls, smanh):
		cls.suc_manh = smanh
snA = SieuNhan("Sieu nhan do", "Kiem", "Do")

print(SieuNhan.suc_manh)
print(snA.suc_manh)

snA.cap_nhap_suc_manh(40)

print(SieuNhan.suc_manh)
print(snA.suc_manh)

#tao doi tuong bang class method
class SieuNhan:
	suc_manh = 50
	def __init__(self, para_ten, para_vu_khi, para_mau_sac):
		self.ten = para_ten
		self.vu_khi = para_vu_khi
		self.mau_sac = para_mau_sac

	@classmethod
	def from_string(cls, s):
		lst = s.split('-')   # tach chuoi 
		new_lst = [st.strip() for st in lst] # xoa khoang trang bang list comprehension
		ten, vu_khi, mau_sac = new_lst  #gan cac thong tin xu ly cho list moi
		return cls(ten, vu_khi, mau_sac)

infor_str = "Sieu Nhan do - Kiem - Do"

snA = SieuNhan.from_string(infor_str)

print(snA.__dict__)   # in theo kieu du lieu dic


