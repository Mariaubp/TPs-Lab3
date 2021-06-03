#lista por asignacion es

#my_list=[4,7,5,6,"hola","pera"]
my_list=[5,3,10,2,5]

#for x in my_list:
#	print(x)
res=0

for x in my_list:
	res=res+x

#formateo a res
#las {} indico la posicion en la que quiero q este res, res1
#toma el elemento de la posicion q quiero, le indico
print("la suma de todos los valores de la lista es: {}".format(res))	