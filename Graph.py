class Graph(object):
	"""docstring for Graph"""
	def __init__(self):
		self.edges = {}
		self.numVertices = 0
		self.start = ""
		self.end = ""

	def neighbors(self, id):
		return self.edges[id]

	def cost(self, current, next):
		for x in self.edges[current]:
			if x[1] == next:
				return x[0]
