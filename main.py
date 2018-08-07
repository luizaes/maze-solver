from Graph import Graph
from Maze import Maze
from random import randint
from PIL import Image

graph = Graph()
graphMaze = Graph()
width = 0
height = 0
image = 0
pixels = 0

def mazeGeneration():
	cells = []
	visited = []
	found = False
	x = randint(1, width-2)
	start = '0 ' + str(x)
	visited.append(start)
	cells.append(start)
	pixels[x, 0] = (255,255,255,255)
	pixels[x, 1] = (255,255,255,255)

	print str(x)+' 1'

	while len(cells) != 0:
		print graphMaze.edges[cells[0]]
		for x in graphMaze.edges[cells[0]]:
			st = x[1].split(' ')
			if x[1] not in visited and pixels[int(st[1]), int(st[0])] == (255,255,255,255):
				found = True
				visited.append(x[1])
				cells.append(x[1])
				if int(st[0]) == height-1:
					cells = []
					break
				y = randint(1,3)
				if y == 1 and int(st[1]) > 1:
					pixels[int(st[1])-1, int(st[0])] = (255, 255, 255, 255)
				elif y == 2 and int(st[1]) < width-2:
					pixels[int(st[1])+1, int(st[0])] = (255, 255, 255, 255)
					pixels[int(st[1]), int(st[0])+1] = (255, 255, 255, 255)
				elif int(st[1]) > 1 and int(st[1]) < width-2:
					pixels[int(st[1]), int(st[0])+1] = (255, 255, 255, 255)
					pixels[int(st[1])+1, int(st[0])] = (255, 255, 255, 255)
					pixels[int(st[1])-1, int(st[0])] = (255, 255, 255, 255)
		if not found:
			cells.pop(0)
		found = False

print("Do you want to: \n1 - generate the maze or \n2 - use an existing image?")
input = raw_input()
if input == '1':
	print("Width:")
	width = int(raw_input())
	print("Height:")
	height = int(raw_input())
	image = Image.new('RGBA', (height, width), (0,0,0,255))
	pixels = image.load()
	for x in xrange(0,height):
		for y in xrange(0,width):
			graphMaze.edges[str(x)+ ' ' +str(y)] = []
			graphMaze.numVertices = graphMaze.numVertices + 1
	print(graphMaze.edges)
	for x in xrange(0,height):
		for y in xrange(0,width):
			if x == 0 and y == 0:
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x+1)+ ' ' +str(y)])
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x)+ ' ' +str(y+1)])
			elif x == height-1 and y == 0:
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x-1)+ ' ' +str(y)])
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x)+ ' ' +str(y+1)])
			elif y == width-1 and x == height-1:
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x-1)+ ' ' +str(y)])
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x)+ ' ' +str(y-1)])
			elif y == width-1 and x == 0:
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x+1)+ ' ' +str(y)])
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x)+ ' ' +str(y-1)])
			elif x == 0:
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x+1)+ ' ' +str(y)])
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x)+ ' ' +str(y-1)])
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x)+ ' ' +str(y+1)])
			elif y == width-1:
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x-1)+ ' ' +str(y)])
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x+1)+ ' ' +str(y)])
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x)+ ' ' +str(y-1)])
			elif x == height-1:
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x-1)+ ' ' +str(y)])
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x)+ ' ' +str(y+1)])
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x)+ ' ' +str(y-1)])
			elif y == 0:
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x+1)+ ' ' +str(y)])
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x-1)+ ' ' +str(y)])
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x)+ ' ' +str(y+1)])
			else:
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x+1)+ ' ' +str(y)])
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x)+ ' ' +str(y+1)])
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x-1)+ ' ' +str(y)])
				graphMaze.edges[str(x)+ ' ' +str(y)].append([1, str(x)+ ' ' +str(y-1)])
	print(graphMaze.edges)
	mazeGeneration()
	image.show()

elif input == '2':
	print("What's the name and extension of the image?")
	name = raw_input()
	image = Image.open(name)
	pixels = image.load()
	width, height = image.size

#print("Maze before:")
#image.show()

# Adds all the nodes to our graph
for x in xrange(0,height):
	for y in xrange(0,width):
		if pixels[y,x] == (255,255,255,255):
			if x == 0:
				graph.edges[str(x)+ ' ' +str(y)] = []
				graph.start = str(x)+ ' ' +str(y)
				graph.numVertices = graph.numVertices + 1
				added = True
			elif x == height-1:
				graph.edges[str(x)+ ' ' +str(y)] = []
				graph.end = str(x)+ ' ' +str(y)
				graph.numVertices = graph.numVertices + 1
				added = True
			else:
				graph.edges[str(x)+ ' ' +str(y)] = []
				graph.numVertices = graph.numVertices + 1
				added = True

			# This part is more optimized, but it's harder to track which path the algorithm took
			'''else:
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
						added = True'''

			# Adds the edges to our graph
			if added:
				counter = 0
				for z in reversed(range(0,y)):
					if pixels[z,x] == (0,0,0,255):
						break
					elif pixels[z,x] == (255,255,255,255):
						counter = counter + 1
						if str(x)+ ' ' +str(z) in graph.edges:
							graph.edges[str(x)+ ' ' +str(y)].append([counter, str(x)+ ' ' +str(z)])
							graph.edges[str(x)+ ' ' +str(z)].append([counter, str(x)+ ' ' +str(y)])
							break
				counter = 0
				for z in reversed(range(0,x)):
					if pixels[y,z] == (0,0,0,255):
						break
					elif pixels[y,z] == (255,255,255,255):
						counter = counter + 1
						if str(z)+ ' ' +str(y) in graph.edges:
							graph.edges[str(x)+ ' ' +str(y)].append([counter, str(z)+ ' ' +str(y)])
							graph.edges[str(z)+ ' ' +str(y)].append([counter, str(x)+ ' ' +str(y)])
							break
			added = False

print(graph.edges)
print(len(graph.edges))
maze = Maze(graph)
maze.aStar(pixels)

'''for x in xrange(0,height):
	for y in xrange(0,width):
		for z in xrange(y,width):
			if pixels[z, x] == (255, 0, 0, 255):
'''

image.save('maze3.png')
image = image.resize((width+200, height+150))
print("Maze after:")
image.show()
