from Stack import *
# /* *** ODSATag: AStack1 *** */
# Array-based stack implementation
class AStack(Stack):

    DEFAULT_SIZE = 10
    
    # Constructor
    def __init__(self, size=DEFAULT_SIZE):
        self.maxSize = size     # Maximum size of stack
        self.top = 0            # First free position at top
        self.stackArray = []    # Array holding stack
# /* *** ODSAendTag: AStack1 *** */    

    def __eq__(self, other):
        return (isinstance(other, AStack) and self.maxSize == other.maxSize and 
                self.top == other.top and self.stackArray == other.stackArray)
    
    def __repr__(self):
        out = ""
        for i in reversed(range(self.top)):
            out += str(self.stackArray[i])
            if i != 0:
                out += "\n"
        return out
# /* *** ODSATag: AStack2 *** */

    # Reinitialize stack
    def clear(self):
        self.top = 0
    
# Push "it" onto stack
# /* *** ODSATag: AStackPush *** */
    def push(self, it):
        if self.top >= self.maxSize:
            return False
        self.stackArray.insert(self.top, it)
        self.top += 1
        return True
# /* *** ODSAendTag: AStackPush *** */

# Remove and return top element
# /* *** ODSATag: AStackPop *** */
    def pop(self):
        if self.top == 0:
            return None
        self.top -= 1
        return self.stackArray[self.top]
# /* *** ODSAendTag: AStackPop *** */

    # Return top element
    def topValue(self):
        if self.top == 0:
            return None
        return self.stackArray[self.top-1]

    # Return stack size
    def length(self):
        return self.top

    # Check if the stack is empty
    def isEmpty(self):
        return self.top == 0
# /* *** ODSAendTag: AStack2 *** */
