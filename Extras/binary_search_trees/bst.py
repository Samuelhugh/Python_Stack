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
# Return self
            return self
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
    def max(self):
# Create a variable to start at the Root
        runner = self.root
# Create a variable to hold the max value starting at the Root
        max = self.root.value
# Create a while loop to traverse through only the right side/branches of the BST, because that is the greater than side
        while(runner.right is not None):
# Compare the runners Value to all the right sides Nodes
            if(runner.right.value <= max):
# If the current Node is less than the max then iterate to the next right Node
                runner = runner.right
# Else update the max value
            else:
# Updating max
                max = runner.right.value
# return max
        return max


# Find min method for BST
    def min(self):
# Create a variable to start at the Root
        runner = self.root
# Create a variable to hold the min starting at the Root
        min = self.root.value
# While the left side has Nodes to traverse, Compare all left side/branches/Nodes to min
        while(runner.left is not None):
# Compare the current runner Nodes left Value to that of the min's Value
            if(runner.left.value >= min):
# Updating to next left Node
                runner = runner.left
# Else Update the min to the current runners left side/branch/Node Value
            else:
# Updating min
                min = runner.left.value
# Return min
        return min

# Find out if this BST contains a certain Node
    def contains(self, val):
# Create a variable to start at the Root (almost always)
        runner = self.root
# While the runner is not pointing to None, compare/check BST Nodes against that Value
        while(runner is not None):
# Check if the Value matches the current runners Value
            if(runner.value is val):
# Return true
                return True
# If not, check left and right Nodes respectively
            if(runner.value < val):
# Check if there is a right Node to iterate to next
                if(not runner.right):
# If the runner does not have a right Node, return false
                    return False
# Else if it does, point the runner to the next right Node to continue searching for the Value
                runner = runner.right
# Else if the value is less than the runners Value, check the left side
            else:
# Checking if left side has a Node to iterate to
                if(not runner.left):
# Return false, because the Value is not in the BST
                    return False
# If there is a Node to iterate to, then update the runner to the left side to continue searching the BST
                runner = runner.left
# If the whole BST is check and the value is not found return False
        return False

# See if this BST is empty
    def is_empty(self):
# Check to see if Root Node is not None
        if(not self.root):
# If Root Node is not None, return true
            return True
# Else the BST is empty and return False
        return False

# Size of BST method done Recursively
    def size(self, root_node):
# Base Case to check for leaf Nodes to return 0 for its "children"
        if(root_node is None):
            return 0
# Else, using Forward Progress(and including the root Node, which is where we always start), traverse through the BST recursively - checking each node.
        return 1 + self.size(root_node.left) + self.size(root_node.right)

# Instantiating a new BST
bst = BST()
# Testing BST methods
bst.add(20).add(30).add(38).add(3).add(9)
print(bst.size(bst.root))
print(bst.max())
print(bst.min())
print(bst.contains(38))
print(bst.is_empty())

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)