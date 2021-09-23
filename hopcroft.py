# -*- coding: UTF-8 -*-
from biblioteca_grafo import Grafo

# get v1 e v2
def func1(grafo):
	v1 = [0]
	v2 = []
	t = [False] * (grafo.qtdVertices()+1)
	t[0] = True
	k = 0

	while(False in t):
		if (k in v1):
			for v in grafo.vizinhos(k):
				if (not t[v]):
					v2.append(v)
					t[v] = True

		if (k in v2):
			for v in grafo.vizinhos(k):
				if (not t[v]):
					v1.append(v)
					t[v] = True
		
		k = (k + 1) % grafo.qtdVertices()
	return v1, v2 

# BFS 
def BFS(grafo, x, mate, d):
	lista = []

	for v in x:
		if (mate[v] == -1):
			d[v] = 0
			lista.insert(0, v)
		else:
			d[v] = grafo.inf
	
	d[-1] = grafo.inf
	
	while (lista):
		v = lista.pop()

		if (d[v] < d[-1]):
			vizinhos = grafo.vizinhos(v)
			for vizinho in vizinhos:
				if (d[mate[vizinho]] == grafo.inf):
					d[mate[vizinho]] = d[v] + 1
					lista.insert(0, mate[vizinho])
	
	return d[-1] != grafo.inf, d

# DFS
def DFS(grafo, mate, xx, d):
	if xx != -1:
		for y in grafo.vizinhos(xx):
			if (d[mate[y]] == d[xx] + 1):
				validez, d, mate2 = DFS(grafo, mate, mate[y], d)
				if (validez == True):
					mate = mate2.copy()
					mate[y] = xx
					mate[xx] = y
					return True, d, mate

		d[xx] = grafo.inf
		return False, d, mate
	return True, d, mate

# hopcroft_karp
def hopcroft_karp(grafo):
	d = [grafo.inf] * (grafo.qtdVertices() + 2)
	mate = [-1] * (grafo.qtdVertices() + 1)
	x, y = func1(grafo)
	m = 0

	while(True):
		validez, d = BFS(grafo, x, mate, d)
		if (False in validez):
			break
		for xx in x:
			if (mate[xx] < 0):
				validez, d, mate2 = DFS(grafo, mate, xx, d)
				if (validez):
					mate = mate2.copy()
					m += 1

	return m, mate, x

if __name__ == "__main__":
	grafo1 = Grafo("gr128_10.gr")
	hopcroft_karp(grafo1)
