import numpy as np

data8=np.zeros((256,256),dtype="uint8")
data16=np.zeros((256,256),dtype=np.uint16)
data32=np.zeros((256,256),dtype=np.uint32)
data64=np.zeros((256,256),dtype=np.uint64)

size8=data8.itemsize
size16=data16.itemsize
size32=data32.itemsize
size64=data64.itemsize

#print(size8,size16,size32,size64)

a = np.zeros((256,256), dtype="uint8")
b = np.ones((256,256), dtype="uint16")
c = np.zeros((256,256), dtype="uint32")
d = np.ones((256,256), dtype="uint64")
print(a)

# Leo cuanto ocupan en la memoria y lo paso a kilobytes
print("===> Memoria")
print("a %d kilobytes" % ((a.size * a.itemsize) / 1024))
print("b %d kilobytes" % ((b.size * b.itemsize) / 1024))
print("c %d kilobytes" % ((c.size * c.itemsize) / 1024))
print("d %d kilobytes" % ((d.size * d.itemsize) / 1024))