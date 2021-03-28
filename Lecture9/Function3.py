# unpaking la lay het gia tri cua ham 
lst = ['123', 'abc', 62]
def st(k, t, e, *, r):
	print(k)
	print(t, e)
	print('end', r)

st(*lst, r = 90)    #lay het gia tri ra


def st(*args, kt):          # args laf paking
	print(args)
	print(kt)

st(*(x for x in range(6)), kt = 'abc')          # * vong lap la unpaking

# dic

dic = {'name': 'anh', 'member': 7}
def st(a, b):
	print(a)
	print(b)

st(*dic)      # lay key

# lay value
dic = {'name': 'anh', 'member': 7}
def st(name, member):
	print(name)
	print(member)

st(**dic)

# paking vs ** vs dic
def st(**kwargs):
	print(kwargs)

# st(name ='Anh', member =9)

def st(**kwargs):
	for key, value in kwargs.items():
		print(key, ' ==', value)

st(name ='Anh', member =9)