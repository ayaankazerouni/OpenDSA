# /* *** ODSATag: LList *** */
from Link import *
from List import *
# Linked list implementation
# /* *** ODSATag: LListVars *** */
class LList(List):
    # Class variables
    #   Link head           // Pointer to list header
    #   Link tail           // Pointer to last element
    #   Link curr           // Access to current element
    #   int listSize        // Size of list
# /* *** ODSAendTag: LListVars *** */

# /* *** ODSATag: LListCons *** */
    # Constructor
    def __init__(self, size=None):   # Ignore size 
        self.curr = self.tail = Link(None)  # Create trailer
        self.head = Link(self.tail)         # Create header
        self.listSize = 0

    # Remove all elements
    def clear(self):
        self.curr = self.tail = Link(None)  # Create trailer
        self.head = Link(self.tail)         # Create header
        self.listSize = 0
# /* *** ODSAendTag: LListCons *** */

    def __eq__(self, other):
        return (isinstance(other, LList) and self.curr == other.curr and 
                self.head == other.head and self.tail == other.tail and self.listSize == other.listSize)

    def __repr__(self):
        temp = self.head.next()
        out = ""
        out += "< "
        i = 0
        while i < self.currPos():
            out += str(temp.element())
            out += " "
            temp = temp.next()
            i += 1
        out += "| "
        #i = self.currPos()
        while i < self.listSize:
            out += str(temp.element())
            out += " "
            temp = temp.next()
            i += 1
        out += ">"
        return out
# /* *** ODSATag: LListInsert *** */
    # Insert "it" at current position
    def insert(self, it):   
        self.curr.setNext(Link(self.curr.next(), self.curr.element()))
        self.curr.setElement(it)
        if self.tail == self.curr:
            self.tail = self.curr.next()    # New tail
        self.listSize += 1
        return True
# /* *** ODSAendTag: LListInsert *** */

    # Append "it" to list
    def append(self, it):
        self.tail.setNext(Link(None))
        self.tail.setElement(it)
        self.tail = self.tail.next()
        self.listSize += 1
        return True

# /* *** ODSATag: LListRemove *** */
    # Remove and return current element
    def remove(self):
        if self.curr == self.tail:  # Nothing to remove
            raise IndexError("remove() in LList has current of " + str(self.curr.element()) + " and size of " + str(self.listSize) + " that is not a valid element")
        it = self.curr.element()     # Remember Value
        self.curr.setElement(self.curr.next().element())    # Pull forward the next element
        if self.curr.next() == self.tail:
            self.tail = self.curr   # Removed last, move tail
        #else:
        self.curr.setNext(self.curr.next().next())  # Point around unneeded link
        self.listSize -= 1  # Decrement element count
        return it   # Return value
# /* *** ODSAendTag: LListRemove *** */

    # Set to front
    def moveToStart(self):
        self.curr = self.head.next()    # Set curr at list start

    # Set to end
    def moveToEnd(self):
        self.curr = self.tail   # Set curr at list end

# /* *** ODSATag: LListPrev *** */
    # Move curr one step left; no change if now at front
    def prev(self):
        if self.head.next() == self.curr:   # No previous element
            return
        temp = self.head
        # March down list until we find the previous element
        while temp.next() != self.curr:
            temp = temp.next()
        self.curr = temp
# /* *** ODSAendTag: LListPrev *** */

# /* *** ODSATag: LListNext *** */
    # Move curr one step right; no change if now at end
    def next(self):
        if self.curr != self.tail:
            self.curr = self.curr.next()
# /* *** ODSAendTag: LListNext *** */

    # Return list size
    def length(self):
        return self.listSize

    # Return the position of the current element
    def currPos(self):
        temp = self.head.next()
        i = 0
        while self.curr != temp:
            temp = temp.next()
            i += 1
        return i

# /* *** ODSATag: LListPos *** */
    # Move down list to "pos" position
    def moveToPos(self, pos):
        if pos < 0 or pos > self.listSize:
            return False
        self.curr = self.head.next()
        i = 0
        while i < pos:
            self.curr = self.curr.next()
            i += 1
        return True
# /* *** ODSAendTag: LListPos *** */

    # Return true if current position is at end of the list
    def isAtEnd(self):
        return self.curr == self.tail

    # Return the current element
    def getValue(self):
        if self.currPos() < 0 or self.currPos() >= self.listSize: # No current element
            raise IndexError("getvalue() in AList has a current of " + str(self.curr.element()) + " and size of " + str(self.listSize) + " that is not a valid element")
        return self.curr.element()

    # Check if the list is empty
    def isEmpty(self):
        return self.listSize == 0
# /* *** ODSAendTag: LList *** */
