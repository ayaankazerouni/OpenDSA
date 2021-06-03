# /* *** ODSATag: LStack1 *** */
from Link import *
# Linked stack implementation
class LStack:
    # Constructors
    def __init__(self):
        self.top = None                 # Pointer to first element
        self.size = 0                   # Number of elements

    def __init__(self, size):
        self.top = None
        self.size = 0
# /* *** ODSAendTag: LStack1 *** */

    def __repr__(self):
        out = ""
        temp = self.top
        while temp != None:
            out.append(temp.element())
            out.append(" ")
            temp = temp.next()
        return out
# /* *** ODSATag: LStack2 *** */

    def clear(self):                    # Reinitialize stack
        self.top = None
        self.size = 0

# /* *** ODSATag: LStackPush *** */
    def push(self, it):                 # Put "it" on stack
        self.top = Link(it, self.top)
        self.size += 1
        return True

# /* *** ODSAendTag: LStackPush *** */

# /* *** ODSATag: LStackPop *** */
    def pop(self):                      # Remove "it" from stack
        if self.top == None:
            return None
        it = self.top.element()
        top = self.top.next()
        size -= 1
        return it
# /* *** ODSAendTag: LStackPop *** */

    def topValue(self):                 # Return top value
        if self.top == None:
            return None
        return self.top.element()

    def length(self):                   # Return stack length
        return self.size

    def isEmpty(self):                  # Tell if the stack is empty
        return (self.size == 0)
# /* *** ODSAendTag: LStack2 *** */
