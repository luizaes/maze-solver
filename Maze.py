import numpy, collections
from Graph import Graph

class Maze(object):
	"""docstring for Maze"""	

	def __init__(self, start, end, graph):
		self.listNodes = PriorityQueue()
		self.listNodes.put(start, 0)
		self.cameFrom = {}
		self.costSoFar = {}
		self.cameFrom[start] = None
		self.costSoFar[start] = 0
		self.end = end
		self.graph = graph
		self.aStar()

	def heuristic(self, a, b):
		# Euclidean distance between point a and b
		return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2))

	def aStar(self):

		while not listNodes.empty():
			current = listNodes.get()

			if current == self.end:
				break
		
			for next in graph.neighbors(current):
				newCost = costSoFar[current] + graph.cost(current, next)
				if next not in costSoFar or newCost < costSoFar[next]:
					costSoFar[next] = newCost
					priority = newCost + heuristic(end, next)
					listNodes.put(next, priority)
					cameFrom[next] = current

