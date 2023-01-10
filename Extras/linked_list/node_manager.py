from node import SLNode

class SList:
    def __init__(self):
        self.head = None
# add_to_front Method
    def add_to_front(self, value):
# Can add check to see if List is empty - change to !=, put bulk of code into if body, return self once
        new_node = SLNode(value)
# Saving current head into variable, so I don't lose access to it
        current_head = self.head
# This line of code is so my new New Head has access to the previous current_head
        new_node.next = current_head
# Now making the new_node the New Head of the Linked List
        self.head = new_node
# Returning self to allow chaining
        return self

# Method to traverse Linked List's Nodes and print its Data
    def print_node_data(self):
# This line of code creates a Pointer named runner to start at the front of my List for Iteration
        runner = self.head
# While loop, best for list when not knowing when the end will be, to run while runner is not None
        while (runner != None):
# Print the value/data of each node
            print(runner.value)
# Now I need to Increment or Update the runner to Point to the next Nodes Data
            runner = runner.next
# Once Loop is done Return self to allow for chaining
        return self

# Method to add a Node to the back/end of my Linked List
    def add_to_back(self, value):
# Edge Case... if List is empty/ can change this - change to !=, put bulk of code into if body, return self once
        if self.head == None:
            self.add_to_front(value)
# Making sure the rest of this Function does not happen, since the beginning line resulted in True and to allow chaining
            return self
# Now I want to create a new node with the given value, New Instance of Node Class created
        new_node = SLNode(value)
# Create a variable to traverse through the List to reach the Node with the Next attribute that Points to None, because that means it is the last Node
        runner = self.head
# Loop to Iterate through List till I reach the last Node
        while (runner.next != None):
# While the Expression is true Increment/Update the runner to the Next Node, since I checked to make sure the current Node has a Next Pointer Value/Data via the Loop
            runner = runner.next
# When Loop has reached the final Node I want to set the New Node to be it's Next Value
        runner.next = new_node
# Return self to allow for chaining
        return self

# Remove Front Node from List and Return its Value Method
    def remove_from_front(self):
# Edge Case check if the List is empty
        if self.head != None:
# Point Head Node to its Next Attribute, making it no longer the Head Node
            self.head = self.head.next
# In any case return self
        return self

# Remove Last Node from list and Return its Value Method
    def remove_from_end(self):
# Check if List is empty
        if self.head != None:
# Check if Head Nodes Next Attribute is None
            if self.head.next != None:
# Create a Variable to store the Head of the List
                current = self.head
# Traverse the List, stopping one Node before the last Node and Removing the Absolute Last Node
                while(current.next.next != None):
# Update the current Variable to the Node just before the Last Node
                    current = current.next
# Update the current Variables Next Attribute to None to Remove the Actual Last Node
                current.next = None
# Remove Head Node if it is the only Node
            else:
                self.head = None
# Return self to allow chaining
        return self

# Remove a Node with the Selected Value
    def remove_value(self, val):
# Check if List is empty
        if self.head == None:
            raise IndexError("List is Empty, Sorry mate")
# Check if the Parameter/Input Value matches the Head Nodes Value
        if self.head.value == val:
# Example of how I can use other methods in the Class to keep my code DRY and Simple
            return self.remove_from_front()
# Now create Variable to hold each Node in order to check it against the Value
        current_node = self.head
# Traverse the List, stops one short of the node I need to remove
        while (current_node.next and current_node.next.value != val):
# While the expression continues to be evaluated as True I Update the current_node Variable
            current_node = current_node.next
# "Double" checking  to make sure this Node has a next node which is the Node I will be removing
        if current_node.next != None:
            # result = current_node.next.value
# Deletion of the Node that match the Input/Parameter value
            current_node.next = current_node.next.next
# Return self for chaining
            return self
# Else statement if the Value is not in the List
        else:
            print("Node not in List")
# This is the same thing but keeps my code DRY and is simpler
            # raise IndexError(f"Value ({val}) does not exist in the list.")


# Insert a Node at random in List
#     def insert_at(self, value, n):
# # n is the length of the List, So it must be positive before I check if the List is empty
#     if n < 0:
# # Either raise IndexError(simpler, Dryer), or return self
#         return self
# # Checking/Validating if Head Node or if a replacement for Head Node is Incoming
#     if not self.head or n == 0:
# # Add it to the Front of the List - using Method that I already created to make my code efficient, DRY, Simple, and Reusable
#         self.add_to_front()
# # If its not the Head or a Replacement
#     else:
# # Create a Variable to hold the already present Head Node, since I already checked for that
#         current_pointer = self.head
# 


    def insert_at(self, val, n):
        if n < 0:
            raise IndexError("n must be 0 or a positive integer.")

        if not self.head or n == 0:
            self.add_to_front(val)
        else:
            pointer = self.head
# In order to insert at the right position, I must decrement before the while loop so I can check the previous(parent) nodes
            # n -= 1
            while pointer.next and n > 0:
                n -= 1
                pointer = pointer.next
            new_node = SLNode(val)
            new_node.next = pointer.next
            pointer.next = new_node


# Creating new Instance of my Singly Linked List Manager
my_list = SList()
# Testing the Methods
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_node_data()
# Creating new Instance of my Singly Linked List Manager
sll2 = SList()
# Testing the Methods
sll2.add_to_front("z").add_to_front("y").remove_from_end().remove_from_end().remove_from_end().print_node_data()
# Creating new Instance of my Singly Linked List Manager
sll3 = SList()
# Testing the Methods
sll3.add_to_front(1).add_to_front(2).remove_value(1)
sll4 = SList()
sll4.insert_at("I love linked lists!", 6)
sll4.print_node_data()
sll4.insert_at(22, 0)
sll4.print_node_data()
sll4.insert_at(44, 1)
sll4.print_node_data()
sll4.insert_at(33, 1)
sll4.print_node_data()
sll4.insert_at(93, 1)
sll4.print_node_data()
sll4.insert_at(93, 1)
sll4.print_node_data()
sll4.insert_at(93, 1)
sll4.print_node_data()
sll4.insert_at(93, 1)
sll4.print_node_data()
sll4.insert_at(93, 1)
sll4.print_node_data()
sll4.insert_at(93, 1)
sll4.print_node_data()
sll4.insert_at(93, 1)
sll4.print_node_data()
sll4.insert_at(93, 1)
sll4.print_node_data()
sll4.insert_at("But this one is a little far out maybe?", 12345)
sll4.print_node_data()

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)