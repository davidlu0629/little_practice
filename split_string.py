#you can use this code to split your data in your like
file = open ('hw3.tr')
for  line in file:
	if line[0] == '+' :
		#strip>>discard string '\n'   split>>split data in line by blank
		temp = line.strip('\n').split(' ')
		print  temp
