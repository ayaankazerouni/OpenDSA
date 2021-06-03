# /* *** ODSATag: LList *** */
from Link import *
# Linked list implementation
# /* *** ODSATag: LListVars *** */
class LList:
    # Class variables
    #   Link head           // Pointer to list header
    #   Link tail           // Pointer to last element
    #   Link curr           // Access to current element
    #   int listSize        // Size of list
# /* *** ODSAendTag: LListVars *** */

# /* *** ODSATag: LListCons *** */
    # Constructors
    def __init__(self):
        clear()

    def __init__(self, size):   # Ignore size
        clear()

    def clear(self):
        self.curr = self.tail = Link(None)  # Create trailer
        self.head = Link(self.tail)         # Create header
        self.listSize = 0
# /* *** ODSAendTag: LListCons *** */

# /* *** ODSATag: LListInsert *** */
    def insert(self, it):   # Insert "it" at current position
        self.curr.setNext(Link(self.curr.element(), self.curr.next()))
        self.curr.setElement(it)
        if self.tail == self.curr:
            self.tail = self.curr.next()    # New tail
        self.listSize += 1
        return True
# /* *** ODSAendTag: LListInsert *** */

    def append(self, it):   # Append "it" to list
        self.tail.setNext(Link(None))
        self.tail.setElement(it)
        self.tail = self.tail.next()
        self.listSize += 1
        return True

# /* *** ODSATag LListRemove *** */
    def remove(self):
        if self.curr == self.tail:  # Nothing to remove
            raise IndexError("remove() in LList has current of " + self.curr + " and size of " + self.listSize + " that is not a valid element")
        it = curr.element()     # Remember Value
        self.curr.setElement(self.curr.next().element())    # Pull forward the next element
        if self.curr.next() == self.tail:
            self.tail = self.curr   # Removed last, move tail
        self.curr.setNext(self.curr.next().next())  # Point around unneded link
        self.listSize += 1  # Decrement element count
        return it   # Return value
# /* *** ODSAendTag: LListRemove *** */

# /* *** ODSAendTag: LList *** */
