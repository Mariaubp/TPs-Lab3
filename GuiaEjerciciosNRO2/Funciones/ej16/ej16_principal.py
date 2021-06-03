
import calculos
def operaciones(lista):
	su=calculos.sumar(lista)
	ma=calculos.mayor(lista)
	me=calculos.menor(lista)
	print(f'La suma de los elementos de la lista es {su}')

lista =[100, 20, 14, 56, 23, 8]

operaciones(lista)


