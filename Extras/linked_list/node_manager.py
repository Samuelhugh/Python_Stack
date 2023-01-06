from node import SLNode

class SList:
    def __init__(self):
        self.head = None
# add_to_front Method
    def add_to_front(self, value):
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
# Edge Case... if List is empty
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





my_list = SList()


if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)