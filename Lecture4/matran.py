a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(a[0][1])
# print(a[1][0])
# print(a[2][-1])

b = list(a)

b[0] = 'hello'     # neu thay doi phan tu list con thi k duoc

print(a)
print(b)