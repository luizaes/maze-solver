from Graph import Graph
from Maze import Maze
from PIL import Image

graph = Graph()
image = Image.open('maze.png')
pixels = image.load()
print("Maze before:")
#image.show()

width, height = image.size

# Adds all the nodes to our graph
for x in xrange(0,height):
	for y in xrange(0,width):
		if pixels[y,x] == (255,255,255,255):
			if x == 0:
				graph.edges['0'+str(y)] = []
				graph.start = '0'+str(y)
				graph.numVertices = graph.numVertices + 1
			elif x == height-1:
				graph.edges[str(x)+str(y)] = []
				graph.end = str(x)+str(y)
				graph.numVertices = graph.numVertices + 1
			else:
				added = False
				counter = 0
				if pixels[y,x-1] == (255,255,255,255):
					counter = counter + 1
				if pixels[y,x+1] == (255,255,255,255):
					counter = counter + 1
				if pixels[y-1,x] == (255,255,255,255):
					counter = counter + 1
				if pixels[y+1,x] == (255,255,255,255):
					counter = counter + 1
				if counter >= 3:
					graph.edges[str(x)+str(y)] = []
					graph.numVertices = graph.numVertices + 1
					added = True
				else:
					if pixels[y,x-1] == (0,0,0,255) and pixels[y-1,x] == (0,0,0,255):
						graph.edges[str(x)+str(y)] = []
						graph.numVertices = graph.numVertices + 1
						added = True
					elif pixels[y,x+1] == (0,0,0,255) and pixels[y+1,x] == (0,0,0,255):
						graph.edges[str(x)+str(y)] = []
						graph.numVertices = graph.numVertices + 1
						added = True
					elif pixels[y-1,x] == (0,0,0,255) and pixels[y,x+1] == (0,0,0,255):
						graph.edges[str(x)+str(y)] = []
						graph.numVertices = graph.numVertices + 1
						added = True
					elif pixels[y+1,x] == (0,0,0,255) and pixels[y,x-1] == (0,0,0,255):
						graph.edges[str(x)+str(y)] = []
						graph.numVertices = graph.numVertices + 1
						added = True

				# Adds the edges to our graph
				if added:
					counter = 0
					for z in reversed(range(0,y-1)):
						if pixels[z,x] == (0,0,0,255):
							break
						elif pixels[z,x] == (255,255,255,255):
							counter = counter + 1
							if str(x)+str(z) in graph.edges:
								graph.edges[str(x)+str(y)].append([counter, str(x)+str(z)])
								graph.edges[str(x)+str(z)].append([counter, str(x)+str(y)])
								break
					counter = 0
					for z in reversed(range(0,x-1)):
						if pixels[y,z] == (0,0,0,255):
							break
						elif pixels[y,z] == (255,255,255,255):
							counter = counter + 1
							if str(z)+str(y) in graph.edges:
								graph.edges[str(x)+str(y)].append([counter, str(z)+str(y)])
								graph.edges[str(z)+str(y)].append([counter, str(x)+str(y)])
								break

print(graph.edges)
maze = Maze(graph)
maze.aStar()

#pix[x,y] = value
#im.save('alive_parrot.png')
#print("Maze after:")
#image.show()