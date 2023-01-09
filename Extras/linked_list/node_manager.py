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
    def remove_value(self, value):
# Check if List is empty
        if self.head != None:
# Check if the Value matches the Head Node
            if self.head.data != value:
# Check/Validate if Head Node has a Next Node to Initiate a Traversal of the List
                if self.head.next != None:
# Now Create Variable to hold each Node in order to check it
                    runner = self.head
# Traverse the List
                    while runner.next != None:
# Already checked to see if Head Nodes Data was a match, so now I can start at the Head Nodes Next Nodes Data and check each Node accordingly to see if I can Remove it
                        if runner.next.data != value:
# Update the runner Variable to the Next Node in the List
                            runner = runner.next
# If runner Variable matches the Value
                        else:
# Since I already checked the Head Node I can update the runner Variable(that is Pointing to the Reference/Memory Address of the Head Node) to the current Nodes Next Nodes Next Node
                            runner = runner.next.next
# Then break out of the Loop to return the result
                            break
# Else if the Head Node does not have a Next Node, I cannot Initiate the start or a traversal of the List
                else:
# Print Validation/Error message
                    print("Node not found in List")
                    # return self
# If the Head Nodes Data matches the Value
            else:
# Check/Validate if the Head Node has a Next Node I can Reset/Point the Head to
                if self.head.next != None:
# If so then Reset/Point the Head to the Next Node
                    self.head = self.head.next
# Else Point/Reset the Head to None
                else:
# Pointing the Head Node to None
                    self.head = None
# Return self for chaining
        return self


# Insert a Node at random in List
    # def insert_at(self, value, n):

# Creating new Instance of my Singly Linked List Manager
my_list = SList()
# Testing the Methods
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_node_data()
# Creating new Instance of my Singly Linked List Manager
sll2 = SList()
# Testing the Methods
sll2.add_to_front("z").add_to_front("y").remove_from_end().remove_from_end().remove_from_end().print_node_data()



if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)