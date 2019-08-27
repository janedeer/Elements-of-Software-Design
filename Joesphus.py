#  File: Josephus.py

#  Description: HW 18

#  Student Name: Melanie Sifen

#  Student UT EID: MS69768

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/12

#  Date Last Modified: 4/15

class Link(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class CircularList(object):
    def __init__(self):
        self.first = None

    def insert(self, data):
        new_link = Link(data)
        current = self.first
        if current == None: # if list is empty
            self.first = new_link
            new_link.next = new_link
            return
        while current.next != self.first:
            current = current.next
            
        current.next = new_link
        new_link.next = self.first

    def find(self, data):
        current = self.first
        while current.data != data: # iterate thru list
            current = current.next
        return current

    def delete(self, data):
        current = self.first
        previous = self.first
        if current == None: # if list is empty
            return None
        while current.data != data:
            previous, current = current, current.next
        if current == self.first: # if current is first after loop
            while current.next != self.first:
                current = current.next
            current.next = self.first.next
        previous.next = current.next
        return current.data

    def delete_after(self, start, n):
        current = self.find(start)
        for i in range(1, n):
            current = current.next
        print(str(current.data))
        self.delete(current.data)
        return current.next

    def __str__(self):
        s = ""
        while current.next != self.first:
            s += str(current.data) + " "
            current = current.next

        return s

def main():
    
    # open and read file
    inf = open("josephus.txt", "r")
    num_ppl = int(inf.readline())
    start = int(inf.readline())
    elimination_num = int(inf.readline())
    count = 0
    # create circularList and insert numbers
    lst = CircularList()
    for i in range(1, num_ppl + 1):
        lst.insert(i)
        
    # eliminate soldiers from lst
    for j in range(1, num_ppl + 1):
        start = lst.delete_after(start, elimination_num)
        start = start.data
 

main()











        
            
            
            
