file = open ('hw3.tr')
for  line in file:
	if line[0] == '+' :
		temp = line.strip('\n').split(' ')
		print  temp
