a = "hello  My name is Anh"

a1 = a.capitalize()  #viet hoa chu cai dau tien cua cau
a2 = a.upper()   #tat ca cac chu deu duoc viet hoa
a3 = a.lower()    #tat ca cac chu deu duoc viet thuong
a4 = a.swapcase()     #chu nao viet hoa thi viet thuong chu nao viet thuong thi viet hoa
a5 = a.title()     # viet in hoa chu cai dau tien cua tu

# b = a.center(width,[fillchar])    width độ dài của chuỗi b
  # fillchar kí tự của chuỗi, fillchar chỉ được băng 1
  # 						  fillchar = null thì là khoảng trắng

b1 = a.center(50, '*')     # can giữa
b2 = a.rjust(50)		 #   căn phải
b3 = a.ljust(59, '-')			# căn trái

# PHƯƠNG THỨC XỬ LÝ
c = a.encode()     					# mã hóa chuỗi về một mã code nào đó do bạn chọn
c1 = a.join(['1', '2', '3'])  		 # cộng dồn chuỗi 
c2 = a.replace('a', 'hihi', 1)   	 # thay thế a = hihi   , 1 là số lần thay thế
c3 = a.strip('H')   				# cắt đi phần tử đầu và cuối ở trong giấu ngoặc, null sẽ cắt khoảng trắng
c4 = a.rstrip('h')   				# cắt phải
c5 = a.lstrip('h')  				 # cắt từ trái


print(c3)