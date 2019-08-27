#  File: TestLinkedList.py

#  Description: HW 17

#  Student Name: Melanie Sifen

#  Student UT EID: MS69768

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/10

#  Date Last Modified: 4/12


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
        
                

def main():

    test = [11, 22, 33, 99, 88, 77, 66, 55, 44, 33, 33, 55, 54]
    test2 = [55, 65, 76, 1]
    
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    lst1 = LinkedList()
    for num in test:
        lst1.insert_first(num)
    print("lst1: ")
    print(str(lst1))

    # Test method insert_last()
    lst2 = LinkedList()
    for num in test2:
        lst2.insert_last(num)
    print("lst2: ")
    print(str(lst2))

    # Test method insert_in_order()
    lst3 = LinkedList()
    for num in test:
        lst3.insert_in_order(num)
    print("lst3: ")
    print(str(lst3))
    
    # Test method get_num_links()
    print(lst1.get_num_links())
    print(lst2.get_num_links())

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    print(lst1.find_unordered(99))
    print(lst1.find_unordered(1))

    # Test method find_ordered() 
    # Consider two cases - data is there, data is not there
    print(lst3.find_unordered(99))
    print(lst3.find_unordered(1))

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    lst1.delete_link(99)
    print(lst1)
    lst1.delete_link(1)
    print(lst1)

    # Test method copy_list()
    print("copy: ", lst1.copy_list())

    # Test method reverse_list()
    print("reverse: ", lst1.reverse_list())

    # Test method sort_list()
    print(lst1.sort_list())

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    lst4 = lst1.sort_list()
    print(lst4.is_sorted())
    print(lst2.is_sorted())

    # Test method is_empty()
    lst5 = LinkedList()
    print(lst5.is_empty())

    # Test method merge_list()
    print(lst1.merge_list(lst2))

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print(lst1.is_equal(lst1))
    print(lst2.is_equal(lst1))

    # Test remove_duplicates()
    print(lst1.remove_duplicates())



if __name__ == "__main__":
  main()
