archivo = open("alumnos.csv","r")
print (len(archivo.readlines()))
archivo.close
archivos = open("alumnos.csv","r")
hola=len(archivos.readlines())
print(hola)
archivos.close