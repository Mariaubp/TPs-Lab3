
def cargar():
	nro1= int(input("Ingrese un nro entero: "))
	nro2= int(input("Ingrese un nro entero: "))
	nro3= int(input("Ingrese un nro entero: "))
	nro4= int(input("Ingrese un nro entero: "))
	nro5= int(input("Ingrese un nro entero: "))
	mostrar(nro1, nro2, nro3, nro4, nro5)


def mostrar(nro1, nro2, nro3, nro4, nro5):
	lista=[nro1, nro2, nro3, nro4, nro5]
	print("Elementos mayores a 10 de la lista: ")
	for i in lista:
		if(i>10):
			print(i)

