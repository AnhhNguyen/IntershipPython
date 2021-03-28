k = 3
while k  > 0:
	print('k =', k)
	k -= 1

s = "Hello"
idx = 0
length = len(s)

while idx < length:
	print(idx, 'stands for', s[idx])
	idx += 1

# break dung vong lap
five_even_numbers = []
k_number = 1

while True:
	if k_number % 2 == 0:
		five_even_numbers.append(k_number)
		if len(five_even_numbers) == 5:
			break
	k_number +=1
print(five_even_numbers)
print(k_number)


#continue la tiep tuc
h_number = 0
while h_number < 10:
	h_number +=1
	if h_number % 2 == 0:
		continue
	print(h_number, 'is odd number')

print(h_number)