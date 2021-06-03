from ej20.operaciones import
def operaciones(lista):
	sumar= calculos.sumar(lista)
	mayor=calculos.mayor(lista)
	menor= calculos.menor(lista)
	print(f'La suma de los elementos de la lista es {sumar}')

lista =[100, 20, 14, 56, 23, 8]


operaciones(lista)