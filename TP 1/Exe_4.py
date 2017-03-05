#Mathieu Thomas
#coding:utf-8
#TP - 1


def chaine(A,s,t):
	visite={}
	pred={}
	pile=[]
	for i in A:
		visite[i] =False
	pred[s]=s
	while(len(pile)>0):
		y=pile.pop()
		if (visite[y]==False):

			visite[y]=True
			for i in A:
				if (visite[i]==False):
					pile.append(i)
	return pile

A = { 1 : [  2 ], 0 : [ 3,2 ], 3 : [ 4,2,0], 2 : [ 3 ,1,0 ], 4 : [ 3]}
chaine(A,1,3)
