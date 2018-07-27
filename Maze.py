import numpy, collections
from Queue import *
from Graph import Graph

class Maze(object):
	"""docstring for Maze"""	

	def __init__(self, graph):
		self.listNodes = PriorityQueue(0)
		self.graph = graph
		self.listNodes.put(self.graph.start, 0)
		self.cameFrom = {}
		self.costSoFar = {}
		self.cameFrom[self.graph.start] = None
		self.costSoFar[self.graph.start] = 0
		self.aStar()

	def heuristic(self, a, b):
		# Euclidean distance between point a and b
		return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2))

	def aStar(self):

		while not self.listNodes.empty():
			current = self.listNodes.get()

			if current == self.graph.end:
				print("Got to the end!!")
				break

			#print(self.graph.neighbors(current))

			for next in self.graph.neighbors(current):
				newCost = self.costSoFar[current] + self.graph.cost(current, next)
				if next not in self.costSoFar or newCost < self.costSoFar[next]:
					print("Passed by " + current)
					self.costSoFar[next] = newCost
					priority = newCost + self.heuristic(self.graph.end, next)
					self.listNodes.put(next, priority)
					self.cameFrom[next] = current

