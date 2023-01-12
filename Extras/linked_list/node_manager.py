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
    def insert_at(self, val, n):
# n is the length of the List, So it must be positive so I can add to the List
        if n < 0:
# Use error checking/handling to raise an IndexError
            raise IndexError("n must be 0 or a positive integer.")
# Checking/Validating if Head Node or if a replacement for Head Node is being inserted
        if not self.head or n == 0:
# If so add it to the Front of the List - using the Method I already created making my code efficient, DRY, Simple, and Reusable
            self.add_to_front(val)
# If its not the Head Node being entered again or a Replacement
        else:
# Create a Reference Variable to the Head Node, to begin List Traversal and to ensure I have the correct link to each Node whilst Traversing the Linked List and so I can have a reference to the Parent Node of the position that is always one before the position I want to insert the Current Node I am wanting to insert
            pointer = self.head
# In order to insert at the right position, I must decrement before the while loop, because if I don't then the node will be inserted one position ahead of where it needs to be inserted (memory leak, garbage collection will clean it up at runtime depending on the language)so to solve that I would need to decrement the node one position before where the node is to be inserted so now I have a link from the parent(previous node(s)) so now each node will be connected/linked correctly and none will be left in a void, or a memory leak, and garbage collection will not have to handle it/clean it up
# Adding this is making the connection(link) to the parent node so I have the correct linking of nodes and the node I am currently working on won't be positioned one after/ahead of where it needs to be positioned/ be in a void
            n -= 1
# List Traversal begins if necessary
            while pointer.next and n > 0:
# This is making a connection to each node as well walking up the List to the position where the current node im working with needs to be positioned, i.e. this while loop will stop one before the position needed all while checking each previous(parent) node and making the correct links and still stopping one node before the position needed because I need to make the link of the parent nodes next attribute to be the current node im working with positioning it right where it needs to be still
                n -= 1
# Walking up the list still
                pointer = pointer.next
# This portion of code is linking the current node im working with to its parent node i.e. the node one position right before where the current node im working with needs to be positioned in the List
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
# Creating new Instance of my Singly Linked List Manager
sll4 = SList()
# Testing the Methods
sll4.insert_at("I love linked lists!", 6)
sll4.print_node_data()
sll4.insert_at(22, 0)
sll4.print_node_data()
sll4.insert_at(44, 1)
sll4.print_node_data()
sll4.insert_at(33, 1)
sll4.print_node_data()
sll4.insert_at("But this one is a little far out maybe?", 12345)
sll4.print_node_data()

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)