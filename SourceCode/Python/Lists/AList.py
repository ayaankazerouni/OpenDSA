from List import *
# /* *** ODSATag: AList *** */
# Array-based list implementation
# /* ODSATag: AListVars *** */
class AList(List):
    # listArray         Array holding list elements
    # DEFAULT_SIZE      Default size
    # maxSize           Maximum size of list
    # listSize          Current # of list items
    # curr              position of current element
# /* *** ODSAendTag: AListVars *** */
    DEFAULT_SIZE = 10
# /* *** ODSATag: Constructors *** */
    # Constructors
    # Create a new list object with maximum size "size"
    def __init__(self, size):
        self.maxSize = size
        self.listSize = self.curr = 0
        self.listArray = []             # Create listArray

    def __init__(self):
        self.maxSize = DEFAULT_SIZE
        self.listSize = self.curr = 0
        self.listArray = []
# /* *** ODSAendTag: Constructors *** */
    
    def clear():                        # Reinitialize the list
        self.listSize = self.curr = 0   # Simply reinitialize values

# /* *** ODSATag: AListInsert *** */
    # Insert "it" at current position
    def insert(self, it):
        if self.listSize >= self.maxSize:
            return False
        i = self.listSize
        while i > self.curr:
            self.listArray[i] = self.listArray[i-1] # Makes room for insertion
            i -= 1  # Shifts element up
        self.listArray[self.curr] = it
        self.listSize += 1  # Increment list size
        return True
# /* *** ODSAendTag: AListInsert *** */

# /* *** ODSATag: AListRemove *** */
    # Remove and return the current element
    def remove(self):
        if (self.curr < 0) or (self.curr >= self.listSize): # No current element
            raise IndexError("remove() in AList has a current of " + self.curr + " and size of " + self.listSize + " that is not a valid element")
        it = self.listArray[self.curr]
        i = self.curr
        while i < self.listSize - 1:
            self.listArray[i] = self.listArray[i+1]
            i += 1
        self.listSize -= 1
        return it
# /* *** ODSAendTag: AListRemove *** */

    def moveToStart(self):  # Set to front
        self.curr = 0

    def moveToEnd(self):    # Set to end
        self.curr = self.listSize

    def prev(self):         # Move left
        if self.curr != 0:
            self.curr -= 1

    def next(self):         # Move right
        if self.curr < self.listSize:
            self.curr += 1

    def length(self):       # Return list size
        return self.listSize

    def currPos(self):
        return self.curr    # Return current position

    # Set current list position to "pos"
    def moveToPos(self, pos):
        if pos < 0 or pos > self.listSize:
            return False
        self.curr = pos
        return True

    # Return true if current position is at end of the list
    def isAtEnd(self):
        return self.curr == self.listSize

    # Return the current element
    def getValue(self):
        if self.curr < 0 or self.curr >= self.listSize: # No current element
            raise IndexError("getvalue() in AList has a current of " + self.curr + " and size of " + self.listSize + " that is not a vlaid element")
        return self.listArray[self.curr]

    # Check if the list is empty
    def isEmpty(self):
        return self.listSize == 0
# /* *** ODSAendTag: AList *** */

