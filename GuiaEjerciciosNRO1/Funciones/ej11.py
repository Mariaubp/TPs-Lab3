nombre= input("Ingrese un Nombre en Minuscula: ")

letra=nombre[0]
print ("Primera letra del nombre")
print (letra)

def contar_caract(cadena):
	contador=0

	while cadena[contador]:
		contador +=1
		return contador

print("Cantidad de letras del nombre")	
frase=nombre
print(len(frase))		
