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
        if self.length == 0:
# Set both the head and tail attributes to the new Node because it is the beginning and end of the new DList, and so that reading the list from either end will point to the same node
            self.head = new_node
            self.tail = new_node
# Increment the helper Attribute that makes telling if the DList is empty or not easier
            self.length += 1
# Return self to allow for chaining
            return self
# Else if the list is not empty, add to the front
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

# Add to back method
    def add_to_back(self, val):
# Create a var/reference/pointer to hold the address of the instantiated DList Node
        new_node = DLNode(val)
# Check for Special/Corner/Edge Cases - like an empty list
        if self.length == 0:
# Making my code Reuseable, DRY, and Simpler
            self.add_to_front(val)
# Returning self for chaining
            return self
# Else if the list is not empty, add to the back
        else:
# Create a Variable/Pointer/Reference to hold the address of the Value that self.tail is pointing to currently only
            old_tail = self.tail
# Use the new_node's .prev attribute to make a link to the old_tail to begin adding the new_node to the back
            new_node.prev = old_tail
# Point the self.tail attribute itself to the new_node's location
            self.tail = new_node
# Now I can point the old_tail's .next Attribute to the self.tail or new_node
            old_tail.next = self.tail
# Increment the helper Attribute
            self.length += 1
# Return self for chaining
            return self

# Print DList Node's Values method
    def print_values(self):
# Check for Special/Edge/Corner Cases - like list is empty
        if not self.head:
# Raise IndexError for empty list
            raise IndexError("List is empty.")
# If not, create a Variable/Pointer/Reference to the Head Node to begin printing out each Nodes Values starting at the beginning of the list
        runner = self.head
# Use while loop to traverse the DList
        while(runner != None):
            print(runner.value)
# Update to the next Node
            runner = runner.next
# Return self for chaining
        return self


dll = DList()
dll.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()