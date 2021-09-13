import math

class Grafo:
	def __init__(self, file_name):
		self.inf = math.inf #infinito
		self.file_name = file_name
		self.labels = []
		self.pesos    = {}
		self.num_vertices = None
		self.num_arestas =  None
		self.source = None
		self.target = None
		self.read_data()

	def qtdVertices(self):
		return self.num_vertices

	def qtdArestas(self):
		return self.num_arestas

	def grau(self, v):
		grau = 0
		for aresta in self.pesos.keys():
			if v == aresta[0]:
				grau += 1
		return grau

	def rotulo(self, v):
		return self.labels[v - 1]

	def vizinhos(self, v):
		vizinhos = []
		for aresta in self.pesos.keys():
			if v == aresta[0]:
				vizinhos.append(aresta[1])
		return vizinhos

	def haAresta(self, u, v):
		for aresta in self.pesos.keys():
			if (u, v) == aresta:
				return True
		return False

	def peso(self, u, v):
		try:
			peso = self.pesos[(u, v)]
		except KeyError:
			peso = float("inf")  
		return peso

	def read_data(self):
		with open(self.file_name) as f:
			conteudo_grafo = f.readlines()
		for linha in conteudo_grafo:
			linha = linha.split()
			if linha[0] == 'n':
				if linha[-1] == 's':
					self.source = linha[1]
				else:
					self.target = linha[1]
			elif linha[0] == 'e' or linha[0] == 'a':
				arco = (int(linha[1]), int(linha[2]))
				self.pesos[arco] = float(linha[3])
		self.num_arestas = len(self.pesos.keys())
		if self.source == None:
			self.source = 1
		if self.target == None:
			self.target = self.num_arestas

	def transpor(self):
		b = {}
		for key, value in self.pesos.items():
			b[(key[1],key[0])]=value
		self.pesos = b

grafo1 = Grafo("db128.gr")