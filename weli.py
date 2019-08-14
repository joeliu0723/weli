def weli():
	i = 0
	zone = [1,2,3,4,5]
	zone1 = []
	while i < 5:
		x = input('請輸入第一區第個號碼: ')
		if int(x) in zone:
			zone1.append(x)
		i += 1
	return zone1

k = weli()
print(k)
