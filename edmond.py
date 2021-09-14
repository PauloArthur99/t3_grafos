# -*- coding: UTF-8 -*-
from biblioteca_grafo import Grafo

def ford_fukerson(grafo,vert_origem,vert_destino):
    
    fluxo = 0
    caminho = edmond_karp(grafo,vert_origem,vert_destino)
    
    while len(caminho) != 0:   
        
        fluxo_i = 99999
        
        for i in range(len(caminho)-1):
            fluxo_i = min(grafo.peso(caminho[i],caminho[i+1]),fluxo_i)
        
        for i in range(len(caminho)-1):
            grafo.pesos[(caminho[i],caminho[i+1])] -= fluxo_i
        
        fluxo += fluxo_i
        caminho = edmond_karp(grafo,vert_origem,vert_destino)

    return(fluxo) 

def edmond_karp(grafo,vert_origem,vert_destino):
    
    c = [False] * (grafo.qtdVertices()+1)
    a = [None] * (grafo.qtdVertices()+1)
    c[vert_origem] = True
    q = [vert_origem]

    while len(q) != 0:
        u = q.pop()

        for vizinho in grafo.vizinhos(u):
            
            if c[vizinho] == False and grafo.peso(u,vizinho) > 0:
                c[vizinho] == True
                a[vizinho] = u
                
                if vizinho == vert_destino:
                    p = [vert_destino]
                    w = vert_destino
                    
                    while w != vert_origem:
                        w = a[w]
                        p.append(w)
                    
                    p.reverse()
                    return p
                q.append(vizinho)
    return []

grafo1 = Grafo("db128.gr")

#Observação: Por nós usarmos grafos como listas, não como matrizes, o primeiro vértice é o 1.

print("Edmond Carp:\n")
print(edmond_karp(grafo1,1,4))
print("\nFluxo Máximo por Ford Fukerson:\n")
print(ford_fukerson(grafo1,1,(grafo1.qtdVertices())))
