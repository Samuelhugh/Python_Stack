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



my_list = SList()


if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)