#Matrix - numpy
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[3,4],[2,3]])
print("Addition :")
print(a+b)
print("Subtraction :")
print(a-b)
print("Multiplication :")
print(a*b)
print("Division:")
print(a//b)


#Finding a range
l=range(10)
print(l)


#measuring the time
%timeit [i**2 for i in l]
arr=np.array(range(10))
%timeit arr**2


#Finding the dimensions
mat=np.array([[[1,2],[2,3]],[[3,4],[4,5]]])
print(mat.ndim)
print(mat.shape)
print(len(mat))
print(mat.size)


#arange function
np.arange(1,101,0.5)


#datatype conversion - dtype='datatype' or var.astype
a=np.array([1,2,3,4.8,5,6,7.0,8.4,9],dtype='int')
print(a)
b=np.array([1,2,3,4.8,5,6,7.0,8.4,9])
b.astype('float')
print(b)


#Statistical  functions
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10])
a
print(a.std())
print(a.mean())
print(np.median(a))


#Creation of random function
from numpy import random
a=random.randint(100, size=(10,))
print(a)


#Element wise arithmetic function
a=random.randint(50,size=(3,3))
b=random.randint(50,size=(3,3))
print(a+b)
print(a*b)
print(a-b)
print(a/b)


#Slicing 
a=np.random.randint(10,size=(5,5))
print(a)
print("Second row retrieving : ",a[1,])

a=np.array([1,2,3,4,5,6,7,8,9,10])
print(a[0:5])


#Reshape
a=np.array([1,2,3,4,5,6,7,8,9])
a.reshape(3,3)


#Flattening the array 
a=np.array([1,2,3,4,5,6,7,8,9])
b=a.reshape(3,3)
print(b)
c=b.flatten()
print("Flattened array ",c)


#Adding the value of two matrix into one
a=np.random.randint(10,size=(3,3))
print(a)
b=np.random.randint(10,size=(3,3))
print(b)
c=np.concatenate((a,b),axis=0)
print(c)
print(np.shape(c))


#Operating the array with a single element
a=np.array([1,2,3,4,5,6,7,8,9])
print(a.reshape((3,3)))
print((a**2).reshape(3,3))


#Dot operator
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(a.dot(b))


#Linear algorithm functions
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(np.linalg.inv(a))
print(np.linalg.det(b))


