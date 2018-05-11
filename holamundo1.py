nombre = "sonja2"
nombrelista=[2,3,4,7]
nombrelista.append(10) #Agrega  nuevo numero
print(len(nombrelista))#Da el tamaño
nombrelista.sort()#Ordena
print(nombrelista) 
nombrelista.reverse()#Invierte el orden
print(nombrelista) 
print(nombrelista[0])
nombrediccionario={"nombre":"david" , "apellido": "ordoñez"}#Crear biblioteta
print(nombrediccionario)
print(nombrediccionario["nombre"])
print(nombrediccionario["apellido"])
nombrediccionario["color_favorito"]="azul" #añade un nuevo elemento 
print (len(nombrediccionario))
nombrediccionario["apellido"]="castillo" #cambia el valor de un argumento
nombrediccionario.pop("nombre") #elimina el argumento
print(nombrediccionario)

if nombre == "Ola":
	print("Hey Ola!")
elif nombre == "Sonja":
	print("Hey Sonja!")
elif nombre=="sonja2":
	print("La vuelta2")	
else:
	print("Hey anonymous!")

def hola(nombre1):
	print("hola " + nombre)
	print("how are you?")

hola(nombre)
hola("joven")

personas=["David","Ricardo","Ana","Diana"]

for nombre in personas: #completa la variable nombre, hasta quue pase por todo personas
	hola(nombre) #imprime el contenido

for i in range(1,10):
	print (i)