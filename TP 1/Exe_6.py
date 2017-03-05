#Mathieu Thomas
#coding:utf-8
#TP - 1


def cycle(A,i):
	for z in range (len(A)):
		if A[z]==i :
			return True
		else:
			return False

A = { 1 : [  2 ], 0 : [ 3,2 ], 3 : [ 4,2,0], 2 : [ 3 ,1,0 ], 4 : [ 3]}
print cycle(A,2)
