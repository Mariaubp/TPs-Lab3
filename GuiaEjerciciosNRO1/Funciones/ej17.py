clave= input("Ingrese una Clave: ")



def contar_caract(cadena):
	contador=0

	while cadena[contador]:
		contador +=1
		return contador

print("Cantidad de letras de la clave")	
frase=clave
cantidad=len(frase)		
print(cantidad)


if cantidad>10 and cantidad<20:
	print("Clave valida")

else:
	print ("Clave no valida, ingrese una que contenga entre 10 y 20 caracteres")		