# 1.
import numpy as np
# Elijan un conjunto de datos (Hombres o Mujeres) y trabajen siempre sobre ese. No hace falta hacer los dos, si tienen tiempo y ganas
# y les picó la curiosidad, pueden compararlos. 
# Lo primero es cargar y leer los datos ANSUR I para mujeres (ansurWomen.csv) o ANSUR I para hombres (ansurMen.csv)

# Recordar que antes hay que montar el Drive y asegurarse que los dados esten en la ruta correcta. Aqui usamos 
# la ruta por efecto /content/drive/MyDrive/Colab Notebooks/Data/



# elijo mujeres
ansurWomen = np.genfromtxt(".\Archivos de datos/ansurWomen.csv", delimiter=",", skip_header=1)
# ansurMen = np.genfromtxt('ansurMen.csv', delimiter=",", skip_header=1)

# explorar los datos: dimensiones, forma, filas, columnas, etc. 
print("Shape:", ansurWomen.shape, "Dim:", ansurWomen.ndim)
print(ansurWomen[:,0])
print(ansurWomen[0,:])



# explorar los datos: dimensiones, forma, filas, columnas, etc. 
print("Shape:", ansurWomen.shape, "Dim:", ansurWomen.ndim)
print(ansurWomen[:,0])
print(ansurWomen[0,:])

# En el archivo al que dirige el link que les damos en Fuente, en las páginas 14 a 23 explican 
# a qué característica corresponde cada índice de la fila correspondiente a cada persona medida
print(' ')
# donde está el peso? (weight?) → Index = 124
pesos = ansurWomen[:,124]
print("Pesos de las primeras 10 mujeres de la base de datos:\n", pesos[:10])
# donde está la altura? (stature) → Index = 99
alturas = ansurWomen[:,99]
print("Alturas de las primeras 10 mujeres de la base de datos:\n", alturas[:10])
peso_stats = (pesos.min(), pesos.max(), round(pesos.mean(),4))
altura_stats = (alturas.min(), alturas.max(), round(alturas.mean(),4))
nombres_stats = ('Mínimo','Máximo','Promedio')
print('\n')
print("{:>10} {:>6} {:>8} {:>12}".format("  ", *nombres_stats))
print("{:>10} {:>6} {:>8} {:>12}".format("PESO:", *peso_stats))
print("{:>10} {:>6} {:>8} {:>12}".format("ALTURA:", *altura_stats))


# Ejemplo para ejecutar sobre las mujeres:
asur, datos, peso_stats, altura_stats, corr = ansurWomen(".\Archivos de datos/ansurWomen.csv")
# Imprimo una tabla con los datos. (No era necesario mostrarlo de esta forma)
print("Para las Mujeres")
print("{:>15} {:>8} {:>8} {:>10}".format("Característica", "Min", "Máx", "Promedio"))
print("{:>15} {:>8} {:>8} {:>10}".format("PESO:", *peso_stats))
print("{:>15} {:>8} {:>8} {:>10}".format("ALTURA:", *altura_stats))
print(f"Correlación: {corr[0,1]}")

# Podemos hacer lo mismo para los hombres ahora;
asur, datos, peso_stats, altura_stats, corr = ansurWomen(".\Archivos de datos/ansurMen.csv")
# Imprimo una tabla con los datos. (No era necesario mostrarlo de esta forma)
print('------------------------------------------------------')
print("Para los Hombres")
print("{:>15} {:>8} {:>8} {:>10}".format("Característica", "Min", "Máx", "Promedio"))
print("{:>15} {:>8} {:>8} {:>10}".format("PESO:", *peso_stats))
print("{:>15} {:>8} {:>8} {:>10}".format("ALTURA:", *altura_stats))
print(f"Correlación: {corr[0,1]}")