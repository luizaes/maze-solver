from Graph import Graph
from Maze import Maze
from PIL import Image

graph = Graph()
width = 0
height = 0
image = 0
pixels = 0

print("Do you want to: \n1 - generate the maze or \n2 - use an existing image?")
input = raw_input()
if input == '1':
	print("Width:")
	width = int(raw_input())
	print("Height:")
	height = int(raw_input())
	image = Image.new('RGB', (height, width))
elif input == '2':
	image = Image.open('maze2.png')
	pixels = image.load()
	width, height = image.size

#print("Maze before:")
#image.show()

# Adds all the nodes to our graph
for x in xrange(0,height):
	for y in xrange(0,width):
		if pixels[y,x] == (255,255,255,255):
			if x == 0:
				graph.edges[str(x)+str(y)] = []
				graph.start = str(x)+str(y)
				graph.numVertices = graph.numVertices + 1
				added = True
			elif x == height-1:
				graph.edges[str(x)+str(y)] = []
				graph.end = str(x)+str(y)
				graph.numVertices = graph.numVertices + 1
				added = True
			else:
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
				for z in reversed(range(0,y)):
					if pixels[z,x] == (0,0,0,255):
						break
					elif pixels[z,x] == (255,255,255,255):
						counter = counter + 1
						if str(x)+str(z) in graph.edges:
							graph.edges[str(x)+str(y)].append([counter, str(x)+str(z)])
							graph.edges[str(x)+str(z)].append([counter, str(x)+str(y)])
							break
				counter = 0
				for z in reversed(range(0,x)):
					if pixels[y,z] == (0,0,0,255):
						break
					elif pixels[y,z] == (255,255,255,255):
						counter = counter + 1
						if str(z)+str(y) in graph.edges:
							graph.edges[str(x)+str(y)].append([counter, str(z)+str(y)])
							graph.edges[str(z)+str(y)].append([counter, str(x)+str(y)])
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
