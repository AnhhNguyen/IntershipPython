def cal_sum(lst):
	if not lst:
		return 0
	else:
		return lst[0] + cal_sum(lst[1:])

print(cal_sum([1, 2, 3, 4]))

# voi n phan tu thi co n + 1 lan return
# chi co the cong so
def cal_sum(lst):
	return 0 if not lst else lst[0] + cal_sum(lst[1:])

print(cal_sum([1, 2, 3]))

#giam so lan return, nhung neu de ham rong se co loi
def cal_sum(lst):
	return lst[0] if len(lst) == 1 else lst[0] + cal_sum(lst[1:])

print(cal_sum([1,2 ,4]))

# paking
def cal_sum(lst):
	idx0, *r = lst
	return idx0 if not r else idx0 + cal_sum(r)

print(cal_sum([[7, 8], [1,2], [4,5]]))

#ham goi khac
def cal_sum(lst):
	if not lst: return 0
	return call_cal_sum(lst)
def call_cal_sum(lst):
	return lst[0] + cal_sum(lst[1:])

print(cal_sum([1, 2, 3, 4, 5]))