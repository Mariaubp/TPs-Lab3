def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiou":
			contador += 1
	return contador


cadena=input("Ingrese la cadena: ")

cantidad = contar_vocales(cadena)
print(f"En la cadena '{cadena}' hay {cantidad} vocales")


'''
# Otra prueba
cadena = "aeiou"
cantidad = contar_vocales(cadena)
print(f"En la cadena '{cadena}'' hay {cantidad} vocales")

# Prueba final
cadena = "bcd"
cantidad = contar_vocales(cadena)
print(f"En la cadena '{cadena}' hay {cantidad} vocales")

'''