def d(n):
    if n==11:
        return
    
    print(n)
    d(n+1)
    
d(1)


def string(n):
	if n == "":
		return
	print(n[0])
	string(n[1:])
string("hello")   


