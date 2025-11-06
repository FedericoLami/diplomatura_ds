import numpy as np

matriz_zeros3=np.zeros((3,3))
matriz_zeros256=np.zeros((256,256))
matriz_ones3=np.ones((3,3))
matriz_ones256=np.ones((256,256))
#print(matriz_zeros3)
#print(matriz_zeros256)
#print(matriz_ones3)
#print(matriz_ones256)

x=matriz_zeros3.itemsize
y=matriz_zeros256.itemsize
z=matriz_ones3.size
zz=matriz_ones256.size
print(x)
print(y)
print(z)
print(zz)