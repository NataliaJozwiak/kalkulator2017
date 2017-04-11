def get_help():
	print('To jest prosty program kalkulatora. Wproadz dwie liczby i zatwierdz.')
	
def dodawanie(a, b):
	wynik = a + b
	return wynik
	
get_help()
zm1 = int(input())
zm2 = int(input())
print(dodawanie(zm1,zm2))
