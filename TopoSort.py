#  File: Graph.py

#  Description: HW 23

#  Student Name: Melanie Sifen

#  Student UT EID: MS69768

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 5/1

#  Date Last Modified: 5/1

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack is empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))


class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

# Edge class
class Edge(object):
  def __init__(self, start, finish, weight):
    self.u = start
    self.v = finish
    self.weight = weight

class Graph (object):
  def __init__ (self):
    self.Vertices = []      # list of Vertex objects
    self.adjMat = []        # adjacency matrix
    self.Edges = []

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given a label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (not self.has_vertex(label)):
      self.Vertices.append (Vertex (label))
      
      # add a new column in the adjacency matrix
      nVert = len (self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append(0)

      # add a new row for the new Vertex
      new_row = []
      for i in range (nVert):
        new_row.append (0)
      self.adjMat.append (new_row)

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len(self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # determine if a directed graph has a cycle
  # this function should return a boolean and not print the result
  def has_cycle(self):
    nVert = len(self.Vertices)
    for i in range(nVert):
      # create the Stack
      theStack = Stack()
      # mark the vertex as visited and push it on the stack
      (self.Vertices[i]).visited = True
      theStack.push (i)

      # visit the other vertices according to depth
      while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
        for edge in self.Edges:
          if edge.u == self.Vertices[theStack.peek()] and edge.v == self.Vertices[i]:
            return True
        u = self.get_adj_unvisited_vertex(theStack.peek())
        if (u == -1): 
          u = theStack.pop()
        else:
          (self.Vertices[u]).visited = True
          theStack.push (u)

      # the stack is empty, let us reset the flags
      self.reset_visited()
      
    return False

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    # add Edge
    edge = Edge(self.Vertices[start], self.Vertices[finish], weight)
    self.Edges.append(edge)

  # get a list of neighbors that you can go to from a vertex
  # return empty list if there are none
  def get_neighbors(self, vertexLabel):
    nList = []
    idx = self.get_index(vertexLabel)
    for i in range(len(self.adjMat[idx])):
      if self.adjMat[idx][i] != 0:
        nList.append(self.Vertices[i])
    return nList

  # resets was_visited bool
  def reset_visited(self):
    nVert = len(self.Vertices)
    for i in range(nVert):
      self.Vertices[i].visited = False

  # return a list of vertices after a topological sort
  # this function should not print the list
  def toposort(self):
    if not self.has_cycle():
      theStack = Stack()
      for vertex in self.Vertices:
        if vertex.visited == False:
          self.topo_helper(self.get_index(vertex.label), theStack)
          
      # let us reset the flags
      self.reset_visited()
      return theStack
    return None
    

  def topo_helper(self, v, theStack):
      # vertex visited
      self.Vertices[v].visited = True
      neighbors = self.get_neighbors(self.Vertices[v].label)
      for vertex in neighbors:
        if vertex.visited == False:
          self.topo_helper(self.get_index(vertex.label), theStack)
      theStack.push(v)
               
def main():

  graph = Graph()
  inf = open("topo.txt", "r")
  num_vertices = int(inf.readline().strip())
  for i in range(num_vertices):
    vertex = inf.readline().strip()
    graph.add_vertex(vertex)

  num_edges = int(inf.readline().strip())
  for i in range(num_edges):
      edge = inf.readline().strip()
      edge = edge.split()
      start = graph.get_index(edge[0])
      finish = graph.get_index(edge[1])
      graph.add_directed_edge(start, finish, weight = 1)

  inf.close()
  # test if a directed graph has a cycle
  print(graph.has_cycle())

  # test topological sort
  theStack = graph.toposort()
  if theStack != None: # if it does not have a cycle
    for i in range(theStack.size()):
      print(graph.Vertices[theStack.pop()])
  print()

      
  
if __name__ == "__main__":
    main()
