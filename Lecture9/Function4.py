lst = [1, 2, 3]

def change(parameter):
	parameter[1] = 'New value'        # tro truc tiep vao gia tri cua list
	print('Change successfully!')

print(lst)
change(lst)          # thay doi gia tri cua list khi tro truc tiep vao list
print(lst)

# LUU Y: han che su dung global vi se lam roi loan code
def make_global():   #khi mot bien duoc tao ra trong ham, thi no la bien cuc bo(local)
	global x		# muon no co the su dung ngoai ham thi ta dung global(toan cau)
	x = 1


#truong hop bien cuc bo(local) trung ten voi bien toan cau(global)
# thi chi khi tac dong vao bien thi gia tri bien moi thay doi

def local():		
	x = 5
	print('x in local', x)

make_global()
print(x)
local()    # tac dong vao bien
print(x)	# khong tac dong vao bien nen bien ve gia tri global(toan cau)
