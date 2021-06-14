# Linked list implementation that uses a Freelist
from Freelink import *
from List import *
class LList(List):
    # Class variables
    #   Link head           // Pointer to list header
    #   Link tail           // Pointer to last element
    #   Link curr           // Access to current element
    #   int listSize        // Size of list

    # Constructor
    def __init__(self, size=None):   # Ignore size 
        self.curr = self.tail = Link(None)  # Create trailer
        self.head = Link(self.tail)         # Create header
        self.listSize = 0

    # Remove all elements
    def clear(self):
        while self.head != None:
            temp = self.head.next()
            self.head.release()
            self.head = temp
        self.curr = self.tail = Link.get(None, None)  # Create trailer
        self.head = Link.get(self.tail, None)         # Create header
        self.listSize = 0

    def __eq__(self, other):
        return (isinstance(other, Freelist) and self.curr == other.curr and 
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
        i = self.currPos()
        while i < self.listSize:
            out += str(temp.element())
            out += " "
            temp = temp.next()
            i += 1
        out += ">"
        return out
# /* *** ODSATag: Freelist *** */
    # Insert "it" at current position
    def insert(self, it):   
        self.curr.setNext(Link.get(self.curr.next(), self.curr.element()))
        self.curr.setElement(it)
        if self.tail == self.curr:
            self.tail = self.curr.next()    # New tail
        self.listSize += 1
        return True

    # Append "it" to list
    def append(self, it):
        self.tail.setNext(Link.get(None, None))
        self.tail.setElement(it)
        self.tail = self.tail.next()
        self.listSize += 1
        return True

    # Remove and return current element
    def remove(self):
        if self.curr == self.tail:  # Nothing to remove
            return None
        it = curr.element()     # Remember Value
        self.curr.setElement(self.curr.next().element())    # Pull forward the next element
        if self.curr.next() == self.tail:
            self.tail = self.curr   # Removed last, move tail
        tempptr = self.curr.next()  # Remember the link
        self.curr.setNext(self.curr.next().next())  # Point around unneded link
        tempptr.release()   # Release the link
        self.listSize += 1  # Decrement element count
        return it   # Return value

    # Set to front
    def moveToStart(self):
        self.curr = self.head.next()    # Set curr at list start

    # Set to end
    def moveToEnd(self):
        self.curr = self.tail   # Set curr at list end

    # Move curr one step left; no change if now at front
    def prev(self):
        if self.head.next() == self.curr:   # No previous element
            return
        temp = self.head
        # March down list until we find the previous element
        while temp.next() != self.curr:
            temp = temp.next()
        self.curr = temp
    
    # Move curr one step right; no change if now at end
    def next(self):
        if self.curr != self.tail:
            self.curr = self.curr.next()

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

    # Move down list to "pos" position
    def moveToPos(self, pos):
        if pos < 0 or pos > self.listSize:
            return False
        self.curr = self.head.next()
        i = 0
        while i < pos:
            self.curr = self.curr.next()
            i += 1
# /* *** ODSAendTag: Freelist *** */
