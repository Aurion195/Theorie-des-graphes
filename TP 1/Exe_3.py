#Mathieu Thomas
#coding:utf-8
#TP - 1


def Parcours(A,s):
	visite={}

	pile=[]
	for i in A:
		visite[i] = False
	pile.append(s)
	while(len(pile)>0):
		y=pile.pop()
		if (visite[y]==False):
			print y
			visite[y]=True
		for i in A:
			if (visite[i]==False):
				pile.append(i)

A = { 1 : [  2 ], 0 : [ 3,2 ], 3 : [ 4,2,0], 2 : [ 3 ,1,0 ], 4 : [ 3]}
Parcours(A,0)
