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
				graph.edges.append([0, []]);
				graph.numVertices = graph.numVertices + 1
			elif x == height-1:
				graph.edges.append([graph.numVertices, []]);
				graph.numVertices = graph.numVertices + 1
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
					graph.edges.append([graph.numVertices, []]);
					graph.numVertices = graph.numVertices + 1



#print(graph.edges)

#pix[x,y] = value
#im.save('alive_parrot.png')
#print("Maze after:")
#image.show()