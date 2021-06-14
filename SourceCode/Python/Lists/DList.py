from DLink import *
from List import *
# Doubly Linked list implementation
class LList(List):
    # Constructor
    def __init__(self, size=0):     # Ignore size
        self.curr = self.tail = Link(None, None)    # Create trailer
        self.head = Link(None, self.tail)   # Create header
        self.tail.setPrev(self.head)    # Set prev link for trailer
        self.listSize = 0
   
    # Remove all elements
    def clear(self):
        self.curr = self.tail = Link(None, None)
        self.head = Link(None, self.tail)
        self.tail.setPrev(self.head)
        self.listSize = 0

# /* *** ODSATag: Dlist *** */
# Insert "it" at current position
# /* *** ODSATag: DListInsert *** */
    def insert(self, it):
        self.curr = Link(self.curr.prev(), self.curr, it)
        self.curr.prev().setNext(self.curr)
        self.curr.next().setPrev(self.curr)
        self.listSize += 1
        return True
# /* *** ODSAendTag: DListInsert *** */

# Append "it" to list
# /* *** ODSATag: DListAppend *** */
    def append(self, it):
        self.tail.setPrev(Link(self.tail.prev(), self.tail, it))
        self.tail.prev().prev().setNext(self.tail.prev())
        if self.curr == self.tail:
            self.curr = self.tail.prev()
        self.listSize += 1
        return True
# /* *** ODSAendTag: DListAppend *** */

# Remove and return current element
# /* *** ODSATag: DListRemove *** */
    def remove(self):
        if self.curr == self.tail:  # Nothing to remove
            return None
        it = self.curr.element()    # Remember value
        self.curr.prev().setNext(self.curr.next())  # Remove from list
        self.curr.next().setPrev(self.curr.prev())
        self.curr = self.curr.next()
        self.listSize -= 1      # Decrement node count
        return it   # Return value removed
# /* *** ODSAendTag: DListRemove *** */

# Move curr one step left; no change if at front
# /* *** ODSATag: DListPrev *** */
    def prev():
        if self.curr.prev() != self.head:   # Can't back up from list head
            self.curr = self.curr.prev()
# /* *** ODSAendTag: DListPrev *** */

# /* *** ODSAendTag: Dlist *** */

    def moveToStart(self):  # Set curr at list start
        self.curr = self.head.next()

    def moveToEnd(self):    # Set curr at list end
        self.curr = self.tail

    # Move curr one step right; no change if now at end
    def next(self):
        if self.curr != self.tail:
            self.curr = self.curr.next()

    def length(self):   # Return list length
        return self.listSize

    # Return the position of the current element
    def currPos(self):
        temp = self.head.next()
        i = 0
        while self.curr != temp:
            temp = temp.next()
            i += 1
        return i

    # Move down list to "pos" position
    def moveToPos(self, pos):
        if (pos < 0) or (pos > self.listSize):
            return False
        self.curr = self.head.next()
        i = 0
        while i < pos:
            self.curr = self.curr.next()
            i += 1
        return True

    # Return true if current position is at end of the list
    def isAtEnd(self):
        return self.curr == self.tail

    # Return current element value
    def getValue(self):
        if self.curr == self.tail:
            return None
        return self.curr.element()

    # Check if the list is empty
    def isEmpty(self):
        return self.listSize == 0
 
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
 
    # Test for XOR concept
    def XOR():
        a = 1
        b = 1
        c = 1
# /* *** ODSATag: XOR *** */
        a = a + b
        b = a - b   # Now b contains original value of a
        a = a - b   # Now a contains original value of b
# /* *** ODSAendTag: XOR *** */
