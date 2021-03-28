def cal(width, height):
	per = (width + height) * 2
	return per

width = 1
height = 2

print(cal(width, height))
print(cal(3, 2))


def cal_area_per(width, height):
	perimeter = (width + height) * 2
	area = width * height
	return perimeter, area

print(cal_area_per(width, height))