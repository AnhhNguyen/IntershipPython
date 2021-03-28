#  positional argument va keyword argument
def student(a, b):
	pass 		# lenh giu cho

student(2, 'Da Nang')          # positional
student(b = "Da Nang", a = 2)	# keyword


def toan(a, b = 2, c = 4, d = 1):
	f = (a + d) * (b + c)
	print(f)

toan(1, d =4)			# khong truyen d cung duoc


# dau sao de hieu la tu sau dau sao se la keyword
# nen co the k can phai defau gia tri cho key
def student(pos_or_key_arg, *, key_arg1, key_arg2):
	print(pos_or_key_arg)
	print(key_arg1)
	print(key_arg2)

student(1, key_arg1 = 2, key_arg2 = 'IT')