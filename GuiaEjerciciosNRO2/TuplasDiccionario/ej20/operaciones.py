def sumar(lista):
	suma=0
	for elemento in lista:
		suma += elemento

	return suma	



def mayor(lista):
	length= len(lista)
	lista.sort()
	print("Mayor elemento: ", lista[length-1])	



def menor(lista):
	lista.sort()
	print("Menor elemento: ", lista[0])	