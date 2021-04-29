my_list= []
mayor=0


#genera una lista de enteros de 0 a 4
for x in range(5):
	val=int(input("Ingrese un nro entero: "))
	#le voy cargando valores a la lista
	my_list.append(val)


for x in my_list:
	if x> mayor:
		mayor=x

print("el mayor nro ingresado es {}".format(mayor))		