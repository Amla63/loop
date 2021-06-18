i=1
while i<=100:
	p=0
	j=1
	while j<=i:
		if i%j==0:
			p=p+1
		j=j+1
	if p==2:
		print(i)
	i=i+1
