
import longitud
def longitudes(nombre1):
	lon1=longitud.longitud1(nombre1)
	print (f'la longitud del primer nombres: {lon1}')
	return lon1


def longitudes2(nombre2):
	lon2=longitud.longitud2(nombre2)
	print (f'la longitud del segundo nombres: {lon2}')
	return lon2



nombre1=input("Ingrese un nombre: ")
nombre2=input("Ingrese un nombre: ")	


longitudNombre1= longitudes(nombre1)
longitudNombre2= longitudes2(nombre2)

if (longitudNombre1 > longitudNombre2):
	print("El PRIMER nombre es mas largo")
else:
	print ("El SEGUNDO nombre es mas largo")


