#  File: TestBinaryTree.py

#  Description: HW 21

#  Student Name: Melanie Sifen

#  Student UT EID: MS69768

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/22

#  Date Last Modified: 4/27

class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def search(self, data):
        current = self.root
        while current != None and current.data != data:
            if data < current.data:
                current = current.lchild
            else:
                curretn = current.rchild
        return current
    # insert data in tree
    def insert(self, data):
        new_node = Node(data)
        current = self.root
        parent = self.root
        if self.root == None:
            self.root = new_node
        else:
            while current != None:
                parent = current
                if data < current.data:
                    current = current.lchild
                else:
                    current = current.rchild

            if data < parent.data:
                parent.lchild = new_node
            else:
                parent.rchild = new_node
            
    # in order traversal
    def in_order(self, aNode):
        if aNode != None:
            self.in_order(aNode.lchild)
            print(aNode.data)
            self.in_order(aNode.rchild)
            
    # find height of tree from a given node
    def get_height(self, aNode):
        if aNode == None:
            return 0
        lheight = self.get_height(aNode.lchild)
        rheight = self.get_height(aNode.rchild)
        if lheight > rheight:
            return lheight + 1
        return rheight + 1
        
    # total num of nodes  
    def num_nodes(self, aNode):
        aNode = self.root
        if aNode == None:
            return 0
        return self.num_nodes(aNode.lchild) + 1 + self.num_nodes(aNode.rchild)
            
    # calc. balance factor for a given node   
    def balance_factor(self, aNode):
        if aNode == None:
            return 0
        lheight = get_height(aNode.lchild)
        rheight = get_height(aNode.rchild)

        return lheight - rheight
    
    # determines if the tree is balanced
    def is_balanced(self, aNode):
        if aNode == None:
            return True
        lheight = get_height(aNode.lchild)
        rheight = get_height(aNode.rchild)

        if abs(lheight - rheight) == 1 or lheight - rheight == 0:
            if is_balanced(aNode.rchild) and is_balanced(aNode.lchild):
                return True
        return False
    
    # recursively builds tree from sorted list
    def create_tree(self, a_list):
        #find mid
        #set root = mid
        #insert rest of elems
            
        
    
    # print tree breadth first
    def print_level(self, aNode):
        for i in range(1, self.get_height(aNode) + 1):
            self.print_level_helper(aNode, i)
            
    # helper function for printing breadth first
    # prints node from a specific level
    def print_level_helper(self, aNode, level_num):
        if aNode == None:
            return None
        elif level_num == 1:
            print(aNode.data)
        elif level_num > 1:
            self.print_level_helper(aNode.lchild, level_num - 1)
            self.print_level_helper(aNode.rchild, level_num - 1)

def main():

    # lists of numbers to insert into trees
    lst1 = []
    for i in range(10):
        lst1.append(i)

    lst2 = [5, 6, 99, 106, 99, 8, 7, 6, 5, 9, 10]

    lst3 = []
    for i in range(2, 50, 4):
        lst3.append(i)

    # Create at least two binary search trees - one balanced and the other not    
    t1 = Tree()
    t2 = Tree() 
    t3 = Tree()
    t4 = Tree() # empty

    for num in lst1:
        t1.insert(num)
    for num in lst2:
        t2.insert(num)
    for num in lst3:
        t3.insert(num)

    tree1 = Tree()
    tree1.insert(33)
    new_tree = tree1.create_tree([1, 9, 11, 17])
    tree1.print_level(tree1.root)
    new_tree.print_level(new_tree.root)
    
    # test get_height
    

    # test num_nodes()
    

    # find if trees are balanced or not

    # create a balanced BST from a sorted list
    # check that it is balanced

    # print all the trees breadth first
    
    

main()

    
    
        

            

        
                
        
        
    
