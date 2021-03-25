inter = (i for i in range(4))

next(inter)
sum(inter)		#tinh tong cua inter

print(sum(inter, 3))		# cong tu 3 tro len

print(max(inter))

print(max([], default='hello word'))	#neu k co gia tri max se tra ve gia tri default

print(min(inter))

inter_ =[1, 4,  6, 7]
print(sorted(inter_, reverse = True))     #k ghi thi de gia tri  la false, la sap xep theo thu tu nho den lon
									# true la sap xep tu lon den nho