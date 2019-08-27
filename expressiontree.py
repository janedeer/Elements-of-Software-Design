class Stack(object):
    
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self, item):
        self.stack.pop()

    def peek(self, item):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def __str__(self):
        s = ""
        for i in range(len(self.stack)):
            s += str(self.stack[i])
        return s
   

class Node(object):
    
    def __init(self, data):
        self.data - data
        self.lchild = None
        self.rchild = None

class Tree(object):

    def __init__(self):
        self.root = None

    def search(self, data):
        current = self.root
        while current != None and current.data != data:
            if key < current.data:
                current = current.lchild
            else:
                current = current.rchild
        return current
    
        

    def create_tree(self, expr):
        tokens = expression.split()
        s = Stack()
        self.root = Node()
        current = self.root
        operators = ["+", "-", "*", "/", "//"]
        for token in tokens:
            if token in operators:
                current.data = token
                s.push(current)
                current.rchild = Node()
                current = current.rchild
            elif token == "(":
                current.lchild = Node()
                s.push(current)
                current = current.lchild
            elif token == ")":
                if not s.is_empty():
                    current = s.pop()
            else: # token is a number
                current.data = eval(toke)
                current = s.pop()
            
                
    def evalutate(self, aNode):
        s = Stack()
        operators = ["+", "-", "*", "/", "//"]
        tokens = aNode.split()
        for token in tokens:
            if token in operators:
                op2 = s.

    def pre_order(self, aNode):
        aNode = list
        
    def post_order(self, aNode):
        ...
        
    
        
