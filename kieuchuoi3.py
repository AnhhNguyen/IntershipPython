a = 'My team is %s' %('Python')

b = 'My team is %s years old' %('1')   # gia tri truyen vao phai vua du chu k dc thua hay thieu

c = '%s %s'
d = c %('1', '2')

e = '%.3f' %(3.9999)   # LAM tron so


g = 'Hello my name is A'
f = f'{g} -I"m Good boy'


#dinh dang chuoi bang f-string

name =""
add = ""
phone = ""
clas = f'Studen: {{name}}\nAdd:{{add}}\nPhone:{phone}'


p = '1: {one}, 2:{two}'.format(one=111, two=222)


hhhh = 'today {:_^50} aukay'.format('hello word')   # căn giữa


hhh= 'today {:*>50} aukay'.format('hello word')  #Căn lề trái

hh= 'today {:*<50} aukay'.format('hello word')   #căn lề phải

# phần định dạng
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano', 'Japanese')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Sunny Leone', 'Canada')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)