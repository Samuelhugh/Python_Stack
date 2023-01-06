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





my_list = SList()


if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)