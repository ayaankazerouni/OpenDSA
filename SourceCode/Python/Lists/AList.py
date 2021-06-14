from List import *
# /* *** ODSATag: AList *** */
# Array-based list implementation
# /* *** ODSATag: AListVars *** */
class AList(List):
    # listArray         Array holding list elements
    # DEFAULT_SIZE      Default size
    # maxSize           Maximum size of list
    # listSize          Current # of list items
    # curr              position of current element
# /* *** ODSAendTag: AListVars *** */
    DEFAULT_SIZE = 10
# /* *** ODSATag: Constructors *** */
    # Constructor
    # Create a new list object with maximum size "size"
    def __init__(self, size=DEFAULT_SIZE):
        self.maxSize = size
        self.listSize = self.curr = 0
        self.listArray = []             # Create listArray
# /* *** ODSAendTag: Constructors *** */

    def __eq__(self, other):
        return (isinstance(other, AList) and self.maxSize == other.maxSize and 
                self.curr == other.curr and self.listSize == other.listSize and self.listArray == other.listArray)

    def __repr__(self):
        return ("Max size: " + str(self.maxSize) + "\nList size: " + str(self.listSize) + "\nCurrent position: " + str(self.curr) + "\nArray list: " + str(self.listArray))
    
    # Reinitialize the list
    def clear(self): 
        self.listSize = self.curr = 0   # Simply reinitialize values

# /* *** ODSATag: AListInsert *** */
    # Insert "it" at current position
    def insert(self, it):
        if self.listSize >= self.maxSize:
            return False
        #self.listArray.append(None)
        #i = self.listSize
        self.listArray.append(None)
        for i in range(self.listSize, self.curr, -1):
        #while i > self.curr:
            self.listArray[i] = self.listArray[i-1] # Makes room for insertion
            #i -= 1  # Shifts element up
        self.listArray[self.curr] = it
        self.listSize += 1  # Increment list size
        return True
# /* *** ODSAendTag: AListInsert *** */

# /* *** ODSATag: AListAppend *** */
    # Append "it" to list
    def append(self, it):
        if self.listSize >= self.maxSize:
            return False
        self.listArray.insert(self.listSize, it)
        self.listSize += 1
        return True
# /* *** ODSAendTag: AListAppend *** */

# /* *** ODSATag: AListRemove *** */
    # Remove and return the current element
    def remove(self):
        if (self.curr < 0) or (self.curr >= self.listSize): # No current element
            raise IndexError("remove() in AList has a current of " + str(self.curr) + " and size of " + str(self.listSize) + " that is not a valid element")
        it = self.listArray[self.curr]
        #i = self.curr
        #while i < self.listSize - 1:
        for i in range(self.curr, self.listSize-1):
            self.listArray[i] = self.listArray[i+1]
            #i += 1
        self.listArray.pop(self.listSize-1)
        self.listSize -= 1
        return it
# /* *** ODSAendTag: AListRemove *** */

    # Set to front
    def moveToStart(self):
        self.curr = 0

    # Set to end
    def moveToEnd(self):
        self.curr = self.listSize-1

    # Move left
    def prev(self):
        if self.curr != 0:
            self.curr -= 1

    # Move right
    def next(self):
        if self.curr < self.listSize:
            self.curr += 1

    # Return list size
    def length(self):
        return self.listSize

    # Return current position
    def currPos(self):
        return self.curr

    # Set current list position to "pos"
    def moveToPos(self, pos):
        if pos < 0 or pos > self.listSize:
            return False
        self.curr = pos
        return True

    # Return true if current position is at end of the list
    def isAtEnd(self):
        return self.curr == self.listSize-1

    # Return the current element
    def getValue(self):
        if self.curr < 0 or self.curr >= self.listSize: # No current element
            raise IndexError("getvalue() in AList has a current of " + self.curr + " and size of " + self.listSize + " that is not a vlaid element")
        return self.listArray[self.curr]

    # Check if the list is empty
    def isEmpty(self):
        return self.listSize == 0
# /* *** ODSAendTag: AList *** */

