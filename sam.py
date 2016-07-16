	
def call():
	c=0
	while True:
		c=c+1
		print c
		if(c==5):
			print "breaking"
			break
for i in range(2):
	call()
