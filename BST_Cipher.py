#  File: BST_Cipher.py

#  Description: hw 20

#  Student Name: Melanie Sifen

#  Student UT EID: MS69768

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/18/19

#  Date Last Modified: 4/23/19

class Node (object):
    def __init__(self, data = None):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree (object):
    def __init__(self, encrypt_str):
        self.root = None
        for ch in encrypt_str:
            if ord(ch) >= 97 and ord(ch) <= 122: # only lower case letters
                self.insert(ch.lower())
            elif ord(ch) == 32:
                self.insert(ch.lower())
            else:
                pass
        return

    def insert(self, ch):
        new_node = Node(ch)
        current = self.root
        parent = self.root
        while current != None:
            parent = current
            if ch == current.data:
                break
            elif ch < current.data:
                current = current.lchild
            else:
                current = current.rchild
        if self.root == None:
            self.root = new_node
        elif ch < parent.data:
            parent.lchild = new_node
        elif ch > parent.data:
            parent.rchild = new_node

    def search(self, ch):
        if self.root.data == ch:
            return "*"
        current = self.root
        s = ""
        while current != None:
            if ch == current.data:
                return s
            elif ch < current.data:
                s += "<"
                current = current.lchild
            elif ch > current.data:
                s += ">"
                current = current.rchild
        return s

    def encrypt(self, s):
        message = ""
        encrypted = ""
        for ch in s:
            ch = ch.lower()
            if ord(ch) == 32 or (ord(ch) >= 97 and ord(ch) <= 122):
                message += ch
        for i, ch in enumerate(message):
            if i != len(message) - 1:
                encrypted += self.search(ch) + '!'
            else:
                encrypted += self.search(ch) # for last character don't add !
        return encrypted

    def traverse(self, s):
        current = self.root
        for item in s:
            if current != None:
                if item == "*":
                    return current.data
                elif item == "<":
                    current = current.lchild
                elif item == ">":
                    current = current.rchild
            else:
                return ""

        return current.data

    def decrypt(self, s):
        decrypted = ""
        s = s.split("!")
        for item in s:
            decrypted += self.traverse(item)
        
        return decrypted

def main():
    key = input("Enter encryption key: ")
    tree = Tree(key)
    
    enc = input("Enter string to be encrypted: ")
    print("Encrypted string: ", tree.encrypt(enc))
    
    dec = input("Enter string to be decrypted: ")
    print("Decrypted string: ", tree.decrypt(dec))

main()
