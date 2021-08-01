# 1st _ numpy(1)

import numpy as np

a1 = np.array(5)
a2 = np.array(3)
a3 = a1 + a2
print(a3)

# Scalar -----------

s = np.array(5)
x = s+3
print(x)

# Vector -----------

v = np.array([1,2,3])
x = v[0]
print(v)
print(x)
print(v[1:])


# Matrices ----------

m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m)
print(m[1][2])


# Tensor -----------

t = np.array([[[[1],[3]],[[2],[4]],[[5],[6]]],
[[[7],[8]],[[9],[10]],[[11],[12]]],
[[[13],[14]],[[15],[16]],[[17],[18]]]])
print(t.shape)

# Changing Shapes

v = np.array([1,2,3,4]) #(행,렬)
x = v.reshape(1,4)
print(x.shape)
x = v[None, :]
print(x)
x = v[:, None]
print(x)


# Simple Example ---------

# - Python's way

values = [1,2,3,4,5]

values = [values[i]+5 for i in range(len((values)))]
print(values[0],'end')
print(range(len(values)))
print(values)

# - Numpy's way 

values = [1,2,3,4,5]
values = np.array(values) + 5

print(values)


# Sum -----------

a = np.array([[1,3],[5,7]]) # 같은 자리 수들만 더해짐
b = np.array([[2,4],[6,8]])
print(a)
print(b)
print(a+b)