import numpy, collections, math
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

	def heuristic(self, a, b):
		# Euclidean distance between point a and b
		st = a.split(' ')
		st2 = b.split(' ')
		return math.sqrt(pow(int(st[0]) - int(st2[0]), 2) + pow(int(st[1]) - int(st2[1]), 2))

	def aStar(self, pixels):

		while not self.listNodes.empty():
			current = self.listNodes.get()
			print("Passed by " + current)
			
			if current == self.graph.end:
				st = current.split(' ')
				pixels[int(st[1]), int(st[0])] = (255, 0, 0, 255)
				print("Got to the end!!")
				break

			for next in self.graph.neighbors(current):
				newCost = self.costSoFar[current] + self.graph.cost(current, next[1])
				if next[1] not in self.costSoFar or newCost < self.costSoFar[next[1]]:
					self.costSoFar[next[1]] = newCost
					priority = newCost + self.heuristic(self.graph.end, next[1])
					self.listNodes.put(next[1], priority)
					self.cameFrom[next[1]] = current
					st = current.split(' ')
					pixels[int(st[1]), int(st[0])] = (255, 0, 0, 255)
