# tách chuỗi

a = ' Hello my name is Anh'
b = a.split(' ', 2)   #cắt chuỗi ra thành list dựa vào phương thức trong ngoặc
					# khoảng trắng thì cắt theo khoảng trắng
					# nếu để chữ thì sẽ cắt từ chữ đó ở trong chuỗi
					# 2 là số lần cắt của chuỗi
b1 = a.rsplit('e', 1) #cắt phải

b2 = a.partition('y')	# cắt chuỗi thành 3 phần tử từ chũ trong ngoặc
						# thành chuỗi tuple
b3 = a.rpartition('y')  # căt phai

c = a.count('h')       # đếm kí tự trong chuỗi
c1 = a.count('h',0, 14)  # tìm trong chuỗi a từ 0 -14 có mấy lần chữ h xuất hiện

c3 = a.startswith('e', 4, 10)	#kiểm tra xem chữ e có bắt đầu trong chuỗi a không
							# 4 là bắt đầu từ vị trí số 4
							# bắt đầu từ 4 -10
c4 = a.endswith('l', 0, 5)     # giống với startswith nhưng bắt đầu từ cuối chuỗi

d = a.find("my")  	#tìm xem trong chuỗi có từ my không và bắt đầu từ vị trí thứ mấy trong chuỗi
d1 = a.rfind('is')   # tim tu bên phai
					# nếu tìm k thấy sẽ ra -1

d2 = a.index('k')      # giống find nhưng tìm không thấy sẽ lỗi
d3 = a.rindex('i')		# timg từ phải qua

g = a.islower() 		# kiểm tra xem chuỗi có viết thường hay k
g1 = a.isupper() 		# kiểm tra xe tất cả các chữ trong chuoix có viết hoa hay k

g2 = a.isdigit()		# kiểm tra xem a có phải là số hay không
g3 = a.isspace()		# kiểm tra xem tất cả các chữ trong chuỗi có phải khoảng trắng hay k

print(g)