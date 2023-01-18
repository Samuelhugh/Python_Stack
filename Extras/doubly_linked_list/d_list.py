from dl_node import DLNode

class DList:
    def __init__(self):
        self.head = None
        self.tail = None
# Helper to make traversing DList easier
        self.length = 0

# Add to front method
    def add_to_front(self, val):
# Same with SList, I need to instantiate a new Node from the Node class with the value passed in
        new_node = DLNode(val)
# Check for Special/Edge/Corner Cases - like if list is empty
        if self.length is 0:
# Set both the head and tail attributes to the new Node because it is the beginning and end of the new DList, and so that reading the list from either end will point to the same node
            self.head = new_node
            self.tail = new_node
# Increment the helper Attribute that makes telling if the DList is empty or not easier
            self.length += 1
# Return self to allow for chaining
            return self
# Else if the list is not empty
        else:
# Create a var/reference/pointer to hold the current address of the Value that the Head is pointing to
            old_head = self.head
# Use the new_node .next attribute to hold the address of the Node in the old_node var
            new_node.next = old_head
# Point self.head to the new_node's location
            self.head = new_node
# Increment our helper Attribute - that makes determining if our list is empty or not easier
            self.length += 1
# Return self for chaining
            return self