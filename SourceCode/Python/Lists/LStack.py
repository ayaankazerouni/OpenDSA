from Link import *
from Stack import *
# /* *** ODSATag: LStack1 *** */
# Linked stack implementation
class LStack(Stack):
    # Constructor
    def __init__(self, size=0):
        self.top = None                 # Pointer to first element
        self.size = 0                   # Number of elements
# /* *** ODSAendTag: LStack1 *** */

    def __eq__(self, other):
        return (isinstance(other, LStack) and self.maxSize == other.maxSize and 
                self.listSize == other.listSize and self.listArray == other.listArray)
    
    def __repr__(self):
        out = ""
        temp = self.top
        while temp != None:
            out += str(temp.element())
            if temp.next() != None:
                out += "\n"
            temp = temp.next()
        return out
# /* *** ODSATag: LStack2 *** */

    # Reinitialize stack
    def clear(self):
        self.top = None
        self.size = 0

# Put "it" on stack
# /* *** ODSATag: LStackPush *** */
    def push(self, it):                 
        self.top = Link(self.top, it)
        self.size += 1
        return True

# /* *** ODSAendTag: LStackPush *** */

# Remove "it" from stack
# /* *** ODSATag: LStackPop *** */
    def pop(self):
        if self.top == None:
            return None
        it = self.top.element()
        self.top = self.top.next()
        self.size -= 1
        return it
# /* *** ODSAendTag: LStackPop *** */

    # Return top value
    def topValue(self):
        if self.top == None:
            return None
        return self.top.element()

    # Return stack length
    def length(self):
        return self.size

    # Tell if the stack is empty
    def isEmpty(self):
        return (self.size == 0)
# /* *** ODSAendTag: LStack2 *** */
