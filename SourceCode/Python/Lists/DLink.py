# /* *** ODSATag: DLink *** */
class Link:     # Doubly linked list node
    # Constructor
    def __init__(self, inp, inn, it=None):
        self.p = inp    # Pointer to previous ndoe
        self.n = inn    # Pointer to next node in list
        if it != None:
            self.e = it # Value for this node

    # Get and set methods for the data members
    def element(self):  # Return the value
        return self.e

    def setElement(self, it):   # Set element value
        self.e = it
        return self.e

    def next(self): # Return next link
        return self.n

    def setNext(self, nextval): # Set next link
        self.n = nextval
        return self.n

    def prev(self): # Return prev link
        return self.p

    def setPrev(self, prevval): # Set prev link
        self.p = prevval
        return self.p
# /* *** ODSAendTag: DLink *** */
