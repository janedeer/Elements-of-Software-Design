#  File: Graph.py

#  Description: HW 22

#  Student Name: Melanie Sifen

#  Student UT EID: MS69768

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/24

#  Date Last Modified: 4/29

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

class Link (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class LinkedList (object):
    def __init__(self):
        self.first = None
        self.length = 0
    
    # get number of links 
    def get_num_links (self):
        current = self.first
        count = 0
        while current != None: 
            count += 1
            current = current.next
        return count
        
  
    # add an item at the beginning of the list
    def insert_first (self, data):
        new_link = Link(data)
        new_link.next = self.first
        self.first = new_link

    # add an item at the end of a list
    def insert_last (self, data):
        new_link = Link(data)
        current = self.first
        if current == None:
            self.first = new_link
            return
        while current.next != None:
            current = current.next
        current.next = new_link
            
        
    # add an item in an ordered list in ascending order
    def insert_in_order (self, data):
        new_link = Link(data)
        current = self.first
        previous = self.first
        if self.first == None or data <= current.data:
            self.insert_first(data)
            return
        while data > current.data:
            if current.next == None:
                self.insert_last(data)
                return
            previous, current = current, current.next
        previous.next, new_link.next = new_link, current
        return    
            
        

    # search in an unordered list, return None if not found
    def find_unordered (self, data):
        current = self.first
        if current == None:
            return None
        while current.data != data:
            if current.next == None:
                return None
            else:
                current = current.next
        return current
        
      

    # Search in an ordered list, return None if not found
    def find_ordered (self, data):
        current = self.first
        if current == None:
            return None
        while current.data != data:
            if current.next == None:
                return None
            elif current.next > data:
                return None
            else:
                current = current.next
        return current
            
    # Delete and return Link from an unordered list or None if not found
    def delete_link (self, data):
        current = self.first
        previous = self.first
        
        if current == None:
            return None
        while current.data != data:
            if current.next == None:
                return None
            else:
                previous = current
                current = current.next
        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next
        return
            
        
        

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        s = ""
        current = self.first
        count = 0
        while current != None:
            s += str(current.data) + "  " # add two spaces
            current = current.next
            count += 1
            if count == 10: # go to next line and reset count
                s += "\n"
                count = 0

        return s
            

    # Copy the contents of a list and return new list
    def copy_list (self):
        new_linked_list = LinkedList()
        current = self.first
        while current != None:
            new_linked_list.insert_last(current.data)
            current = current.next

        return new_linked_list

    # Reverse the contents of a list and return new list
    def reverse_list (self):
        new_linked_list = LinkedList()
        current = self.first
        while current != None:
            new_linked_list.insert_first(current.data) # add next data first
            current = current.next

        return new_linked_list

    # Sort the contents of a list in ascending order and return new list
    def sort_list (self):
        new_linked_list = LinkedList()
        current = self.first
        while current != None:
            new_linked_list.insert_in_order(current.data)
            current = current.next

        return new_linked_list

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
        new_linked_list = LinkedList()
        current = self.first

        while current.next != None:
            if current.data > current.next.data:
                return False
            current = current.next
            
        return True

    # Return True if a list is empty or False otherwise
    def is_empty (self):
        return self.get_num_links() == 0

    # Merge two sorted lists and return new list in ascending order
    def merge_list (self, other):
        new_linked_list = LinkedList()
        self_current = self.first
        other_current = other.first
        while self_current != None:
            new_linked_list.insert_first(self_current.data)
            self_current = self_current.next

        while other_current != None:
            new_linked_list.insert_first(other_current.data)
            other_current = other_current.next
        return new_linked_list.sort_list()
            

    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        self_current = self.first
        other_current = other.first
        if self.get_num_links() != other.get_num_links():
            return False
        while self_current != None:
            if self_current != other_current:
                return False
            else:
                self_current = self_current.next
                other_current = other_current.next
        return True
                
    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates (self):
        new_linked_list = LinkedList()
        current = self.first
        duplicate_lst = []
        while current != None:
            if current.data not in duplicate_lst:
                duplicate_lst.append(current.data)
            current = current.next

        for num in duplicate_lst:
            new_linked_list.insert_last(num)

        return new_linked_list
        

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

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    # add Edge
    edge = Edge(self.Vertices[start], self.Vertices[finish], weight)
    self.Edges.append(edge)
    
  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight
    

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len(self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # do the depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack()

    # mark the vertex v as visited and push it on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1): 
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us reset the flags
    self.reset_visited()

  # do the breadth first search in a graph
  def bfs (self, v):
    # create a queue
    theQueue = Queue ()

    # mark the vertex as visited and enqueue
    self.Vertices[v].visited = True
    print(self.Vertices[v])
    theQueue.enqueue(v)

    while not theQueue.is_empty():
      # get first vertex
      v1 = theQueue.dequeue()
      # get an adjacent unvisited vertex
      v2 = self.get_adj_unvisited_vertex(v1)
      while v2 != -1:
        self.Vertices[v2].visited = True
        print(self.Vertices[v2])
        theQueue.enqueue(v2)
        v2 = self.get_adj_unvisited_vertex(v1)

    # let us reset the flags
    self.reset_visited()

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def get_edge_weight(self, fromVertexLabel, toVertexLabel):
    i, j = self.get_index(fromVertexLabel), self.get_index(toVertexLabel)
    if self.adjMat[i][j] != 0:
      return self.adjMat[i][j]
    return -1

  # get a list of neighbors that you can go to from a vertex
  # return empty list if there are none
  def get_neighbors(self, vertexLabel):
    nList = []
    idx = self.get_index(vertexLabel)
    for i in range(len(self.adjMat[idx])):
      if self.adjMat[idx][i] != 0:
        nList.append(self.Vertices[i])
    return nList

  # get a copy of the list of vertices
  def get_vertices(self):
    return self.Vertices[:]

  # delete an edge from the adj mat
  def delete_edge(self, fromVertexLabel, toVertexLabel):
    # remove from list of edges
    self.Edges = [edge for edge in self.Edges if edge.u.label != fromVertexLabel\
                  or edge.v.label != toVertexLabel]
    # change val in adj mat to 0
    i, j = self.get_index(fromVertexLabel), self.get_index(toVertexLabel)
    self.adjMat[i][j] = 0
    

  # delete a vertex from the vertex list and all edges from and
  # to it in the adj mat
  def delete_vertex(self, vertexLabel):
    # remove the row and column that corresponded to that vertex
    idx = self.get_index(vertexLabel)
    nVert = len(self.Vertices)
    self.adjMat = [row[:idx] + row[idx + 1:] for row in self.adjMat]
    self.adjMat.remove(self.adjMat[idx])
    
    # delete edges
    # creates copy of edge list
    copy_edges = self.Edges[:]
    self.Edges = []
    for edge in copy_edges:
      if edge.u.label != vertexLabel and edge.v.label != vertexLabel:
        self.Edges.append(edge)
    # delete the vertex for list
    del self.Vertices[idx]
    
  # resets was_visited bool
  def reset_visited(self):
    nVert = len(self.Vertices)
    for i in range(nVert):
      self.Vertices[i].visited = False
      
def main():
  # Create Graph object
  cities = Graph()

  # Open file for reading
  inf = open("graph.txt", "r")
  # Read the vertices
  num_vertices = int((inf.readline()).strip())

  for i in range (num_vertices):
    city = (inf.readline()).strip()
    cities.add_vertex(city)

  # Read the edges
  num_edges = int((inf.readline()).strip())

  for i in range(num_edges):
    edge = (inf.readline()).strip()
    edge = edge.split()
    start = int(edge[0])
    finish = int(edge[1])
    weight = int(edge[2])
    cities.add_directed_edge(start, finish, weight)

  # for BFS and DFS
  start_vertex = inf.readline().strip()
  start_index = cities.get_index(start_vertex)

  # for deletion of an edge
  line = inf.readline().split()
  from_vertex_label = line[0]
  to_vertex_label = line[1]

  # for deletion of a vertex
  del_vertex = inf.readline().strip()
  

  inf.close()

  # test depth first search
  print ("Depth First Search")
  cities.dfs(start_index)
  print()

  # test breadth first search
  print ("Breadth First Search")
  cities.bfs(start_index)
  print()

  # test deletion of an edge
  print("Deletion of an edge")
  print()
  print("Adjacency Matrix")
  cities.delete_edge(from_vertex_label, to_vertex_label)
  for i in range(num_vertices):
    for j in range(num_vertices):
      print(cities.adjMat[i][j], end = " ")
    print()
  print()

  # test deletion of a vertex
  print("Deletion of a vertex")
  print()
  print("List of Vertices")
  cities.delete_vertex(del_vertex)
  for city in cities.Vertices:
    print(city)
  print()
  print("Adjacency Matrix")
  for i in range(num_vertices - 1):
    for j in range(num_vertices - 1):
      print(cities.adjMat[i][j], end = " ")
    print()
  print()

if __name__ == "__main__":
    main()
