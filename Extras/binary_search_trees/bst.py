from bt_node import BTNode

class BST:
    def __init__(self):
        self.root = None

# Add to BST
    def add(self, val):
# Check if this is the First/Root Node
        if(not self.root):
# Create new Binary Node with specified Value
            self.root = BTNode(val)
# If not, then create a runner variable to check the left and right of each node; starting from the Root
        runner = self.root
# While runner has Nodes to traverse through
        while(runner is not None):
# Checking to see if runner.value is less than or equal to the Parameter Value to determine where the new Node should be placed left or right
            if(runner.value <= val):
# Check to see if current Node has a right or if its None
                if(runner.right is not None):
# If the current Node has a right Node iterate the runner to the right Node and continue checking to see if the new Node will go to the left or right of this Right Node
                    runner = runner.right
# Else If the current Nodes Right branch is empty, create the new Node with the given Value and place as this current Nodes new right branch
                else:
# Creating new right Node
                    runner.right = BTNode(val)
# Return self for chaining
                    return self
# Else if the current Nodes value is greater than the Parameter Value, check the cases for the left side branch
            else:
# checking to see if the current Node has a left Node
                if(runner.left is not None):
# Then iterate to the left Node and continue the While loop checking the right and left side branches to see where this new Node will be placed
                    runner = runner.left
# Else If the current Nodes left branch is empty, create the new Node with the given Value and place as this current Nodes new left branch
                else:
# Creating new left Node
                    runner.left = BTNode(val)
# Returning self to allow chaining
                    return self

# Find max method for BST
    def max():

# Find min method for BST
    def min():

# Find out if this BST contains a certain Node
    def contains():

# See if this BST is empty
    def is_empty():

# Size of BST method done Recursively
    def size(self, root_node):
# Base Case to check for leaf Nodes to return 0 for its "children"
        if(root_node is None):
            return 0
# Else, using Forward Progress(and including the root Node, which is where we always start), traverse through the BST recursively - checking each node.
        return 1 + self.size(root_node.left) + self.size(root_node.right)

# Instantiating a new BST
bst = BST()
bst.add(20).add(30).add(10)
print(bst.size(bst.root))

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)