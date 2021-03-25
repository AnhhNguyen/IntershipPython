dic = {'name': 'Anh', 'class': 'IT1'}
dic_1 ={}

dic_2 = {key: value for key, value in [('name', 'Anh'), ('class', 'IT1')]}

#constructor
dic_3 = dict()
iter_ = [('name', 'Anh'), ('class', 'IT1')]
dic_4 = dict(iter_)

iter_ = ('name', 'class')
dic_5 = dict.fromkeys(iter_, 'ANH') 	#neu k dien gi thi mac dinh bang none

# lay gia tri ra
print(dic_4['name'])

# thay doi gia tri dict
dic_5['name'] = 'Hoa'
dic_5['address'] = 'Da Nang' # neu thay doi mot gia tri khong co thi no se tu them vao

dic_6 = dict(N = "Vann", H = "Nguyen", DN ="Da Nang")
dic_6['N'] = dic_6['N'] + ' - Hoa'

print(dic_6)
