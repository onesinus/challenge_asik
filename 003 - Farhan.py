def digit(a,b=''):
	b += '9'
	if len(b) < a:
		return digit(a, b)
	else:
		return b

def palindromTerbesar(n):
	max = int(digit(n))
	a = max
	while True:
		b = max
		while True:
			s = str(a * b)
			if s == s[::-1]:
				return a * b
			b-=1
			if b == 0:
				break
		a-=1

print(palindromTerbesar(2))