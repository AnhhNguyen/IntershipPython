file_object = open('pythonFile.txt')

data = file_object.read(10)		#doc file nếu k truyền giá trị vào thì sẽ auto đọc hết
# con trỏ nằm ở cuoioi file nên k thể đọc 2 lần
# phải đóng file rồi mở lại ms đọc lại được
# file_object.close()
# file_object.open('pythonFile.txt')
data2 = file_object.read(5)
# file_object.close()
# đọc từng dòng

data3 = file_object.readlines()

# doc file bang constructor
data4 = list(file_object)
data5 = tuple(file_object)

# them ki tu
file_object = open('pythonFile.txt', 'a+')
data6 = file_object.write('Dang o Da Nang')		#tra ve n ki tu

# kiem soat con tro file
data = file_object.read()
file_object.seek(0)      # dua con tro file ve vi tri dau tien
data = file_object.read()

# cau lenh with la mot cum lenh


print(data3)