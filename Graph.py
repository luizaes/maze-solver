class Graph(object):
	"""docstring for Graph"""
	def __init__(self):
		self.edges = []
		self.numVertices = 0

	def neighbors(self, id):
		return self.edges[id][1]

	def cost(self, current, next):
		for x in self.edges[current][0]:
			if x[0] == next:
				return x[1]

