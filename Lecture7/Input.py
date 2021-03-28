print("Apple", "Mango", "Grapefruit")
print("Apple", "Mango", "Grapefruit", sep=' & ')
print("It's fruit", end=' @ ')

from time import sleep 		#import sleep thu vien vao thu vien time

print('start...')
sleep(3)				#truyen vao so giay
print('end...')

from time import sleep 		#import sleep thu vien vao thu vien time

# flush yeu cau bo nho dem xuat ra het ket qua
print('start...', end='', flush=True)   # boi vi k co newline nen con tro se doi newline tiep theo ms in ra
sleep(3)				#truyen vao so giay
print('end...')


# #tao file moi va ghi vao flie
with open('printText.txt', 'w') as f:
	print("It's never too late to learn", file=f)


from time import sleep

your_name = 'Kim Anh'
your_great = 'Hello! My name is '

for c in your_great + your_name:
	print(c, end='', flush=True)
	sleep(0.2)
print()