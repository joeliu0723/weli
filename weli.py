def weli(a,b,c,d,e,f):
	i = 0
	zonex = [a,b,c,d,e,f]
	zone1 = []
	while i < 6:
		x = input('請輸入第一區號碼: ')
		if x == "" or int(x)>38 or int(x)<1 :
			print('輸入錯誤')
			continue
		if int(x) in zonex:
			zone1.append(x)
		i += 1
	return len(zone1)
	
def weli_z2():
	zoney = '08'
	while True:
		zone2 = input('請輸入第二區號碼: ')
		if zone2 == "" or int(zone2)>10 or int(zone2)<1 :
			print('輸入錯誤')
			continue
		else:
			break	
	if zoney == zone2:
		return 10
	else:
		return 0

def reward():
	zone1 = weli(2,6,29,31,36,37)
	zone2 = weli_z2()
	x = zone1+zone2
	if x == 11:
		print('你中了普獎')
	elif x == 12:
		print('你中了8獎')
	elif x == 13:
		print('你中了7獎')
	elif x == 14:
		print('你中了5獎')
	elif x == 15:
		print('你中了3獎')
	elif x == 16:
		print('你中了頭獎')
	elif x == 3:
		print('你中了9獎')
	elif x == 4:
		print('你中了6獎')
	elif x == 5:
		print('你中了4獎')
	elif x == 6:
		print('你中了2獎')
	else:
		print('你沒中獎')
def main():
	while True:
		reward()
		x = input('繼續對嗎?Y OR N: ' )
		if x == 'N'or x == 'n':
			break
main()
