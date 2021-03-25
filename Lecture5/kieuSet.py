# set khong the chua unhashable --> list
# set khong the chua set
# set khong chua unhashable nhung no la unhashable
# khong the tao mot set rong {}/ empty_set
# co the tao mot empty_set thong qua mot constructor
# set khong quan tam so thu tu


set_1 = {1, 2, 'hello', 'name', (4, 5, 6)}

# tao set la mot comprehension
set_2 = {value for value in range(5)}

# su dung constructor cho một set
#constructor se phan tach mot chuoi
set_3 = set((2, 4, 5))
set_4 = set('hello')
set_5 = set()

# cac toán tử trong set
set_6 = 1 in set_1		# chi kiem tra phan tu nam trong set chu khong kiem tra mot set trong set

set_7 = {1, 2, 3} - {2, 3, 4, 5}	#ket qua con lai la nhung phan tu cua set 1

set_8 = {1, 2, 3, 4} & {5, 6, 3}	# chi lay phan tu chung

set_9 ={1, 2, 3} | {1, 4, 5}		# tap hop tat ca cac phan tu

set_10 = {1, 2, 3} ^ {1, 2, 5}		# khong lay nhung phan tu chung

#phuong thuc trong set
set_1.clear()

set_9.pop() 	#xoa di phan tu da tien
set_9.remove(2)    # xoa di phan tu ma muon xoa, nhung dua phan tu k co trong set se loi
set_8.discard(7)	# giong remove nhung k loi
set_2.copy()
set_3.add(10)

print(set_3)