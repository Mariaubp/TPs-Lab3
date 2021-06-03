my_list=[]
mayor=0

for x in range(5):
	val= input("Ingrese un nombre: ")
	my_list.append(val)

my_list.sort()

#crea una copia de la mylist
#otralista= list(my_list)

print("El primer nombre en orden alfabetico es: {}".format(my_list[0]))	