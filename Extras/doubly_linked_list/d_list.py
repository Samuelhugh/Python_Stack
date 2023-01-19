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
# Printing the Values
            print(runner.value)
# Update to the next Node
            runner = runner.next
# Return self for chaining
        return self

# Remove from front method
    def remove_from_front(self):
# Check for Corner Case
        if self.length == 0:
# Raise IndexError
            raise IndexError("List is empty.")
# [Optional] Create a Reference to point to the address of the Value I want to remove
        # removed_front_node = self.head.value
# I want to sever the current Head and point it to the address of its next Attribute
        self.head = self.head.next
# Decrement the helper Attribute accordingly
        self.length -= 1
# return for chaining
        return self

# Remove from back method
    def remove_from_back(self):
# Check Edge Case
        if self.length == 0:
# Raise an IndexError
            raise IndexError("List is empty.")
# Edge Case if only one Node is in list
        if self.length == 1:
            self.head = None
            self.tail = None
            return self
# This will look at the Head Nodes next Node next - this is why it is the runner
        runner = self.head.next
# I need this walker variable in order to be able to sever the last node, because this will still hold a reference to the last Node if I don't have it and the function will not work
        walker_node_just_before_the_last = self.head
        while(runner.next != None):
            runner = self.head.next
            walker_node_just_before_the_last = walker_node_just_before_the_last.next
        walker_node_just_before_the_last.next = None
# When I get to the last Node, I want to sever its prev reference so that it can be removed from the list
        runner.prev = None
# Decrement helper attribute accordingly
        self.length -= 1
# Return self for chaining
        return self


# Instantiating a new Doubly Linked List
dll = DList()
# Testing DList methods
dll.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
print("*******************")
dll.remove_from_front().print_values()
print("*******************")
dll.remove_from_back()
dll.remove_from_back()