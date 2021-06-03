from Stack import *
# Array-based stack implementation
# /* *** ODSATag: AStack1 *** */
class AStack(Stack):

    DEFAULT_SIZE = 10
    
    # Constructor
    def __init__(self, size=DEFAULT_SIZE):
        self.maxSize = size     # Maximum size of stack
        self.top = 0            # First free position at top
        self.stackArray = []    # Array holding stack
# /* *** ODSAendTag: AStack1 *** */    

    def __repr__(self):
        out = ""
        i = self.top-1
        while i >= 0:
            out.append(stackArray[i])
            out.append(" ")
            i--
        return out
# /* *** ODSATag: AStack2 *** */

    # Reinitialize stack
    def clear(self):
        self.top = 0
    
# /* *** ODSATag: AStackPush *** */
    # Push "it" onto stack
    def push(self, it):
        if self.top >= self.maxSize:
            return False
        self.stackArray[self.top]
        self.top += 1
        return True
# /* *** ODSAendTag: AStackPush *** */

# /* *** ODSATag: AStackPop *** */
    # Remove and return top element
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
