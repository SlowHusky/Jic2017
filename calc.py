def add(pk,c1,c2):
	soma=gmpy2.add(c1,c2)
	return soma%pk.pkAsk[0]

def mul(pk,c1,c2):
	mul = gmpy2.mul(c1,c2)
	return mul%pk.pkAsk[0]
