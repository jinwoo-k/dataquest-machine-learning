import numpy as np

def e1(i,j):
    i3 = np.eye(3)
    t =  np.copy(i3[j,])
    i3[j,] = i3[i,]
    i3[i,] = t
    return i3

def e2(i,k):
    i3 = np.eye(3)
    i3[i,] = k*i3[i,]
    return i3

def e3(i,j,k):
    i3 = np.eye(3)
    t = np.copy(i3[j,]*k)
    i3[i,] = i3[i,] + t
    return i3

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("a",a,sep="\n")
print("e1(0,2)",e1(0,2),sep="\n")
b1 = np.dot(e1(0,2),a)
print("b1= e1*a",b1,sep="\n")
print("inv(e1)",np.linalg.inv(e1(0,2)),sep="\n")
b2 = np.dot(e1(0,2),b1)
print("b2 = inv(e1)*b1",b2,sep="\n")

print("e2(0,2)",e2(0,2),sep="\n")
c1 = np.dot(e2(0,2),a)
print("c1 = e2*a",c1,sep="\n")
print("inv(e2)", np.linalg.inv(e2(0,2)),sep="\n")
c2 = np.dot(e2(0,0.5),c1)
print("c2 = inv(e2)*c1",c2,sep="\n")

print("e3(0,1,2)",e3(0,1,2),sep="\n")
d1 = np.dot(e3(0,1,2),a)
print("d1 = e3*a",d1,sep="\n")
print("inv(e3)",np.linalg.inv(e3(0,1,2)),sep="\n")
d2 = np.dot(e3(0,1,-2),d1)
print("d2 = inv(e3)*d1",d2,sep="\n")