# Phuong thuc tien ich
d = {'name': "Anh", (1, 2, 3):86, 'gioitinh': 'nu'}

d2 = d.copy()
d2.clear()

value = d.get(('name'))		# lay ra gia tri trong dict

value_1 = list(d.items())      # chuyen doi thnah list co the lay tung phan tu

print(value_1[0])

value_2 = d.keys()   # lay ra cac key
value_3 = d.values()  # lay ra value

value_4 = d.pop('name')    # bo di phan tu co key va tra ve value
value_5 = d.pop('aaaa', 'Da Nang')		# lay gia tri k co se bao lỗi , nhưng thêm giá trị defaut values sẽ hết lỗi

value_6 = d.popitem()   #tra về giá trị bất kì trong dict

value_7 = d.setdefault('name')  # co key sẽ trả ra value,k có sẽ mặc định giá trị vào

value_8 = d.update(name='Thao')  # neu chua có sẽ tạo theemm còn có rồi sẽ update

print(d)