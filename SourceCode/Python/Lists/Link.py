# /* *** ODSATag: Link *** */
class Link:
    #Constructors
    def __init__(self, inn, it=None):   # Singly linked list node class
        self.e = it                     # Value for this node
        self.n = inn                    # Point to next node in list
    
    def element(self):              # Return the value
        return self.e

    def setElement(self, it):       # Set element value
        self.e = it
        return self.e

    def next(self):                 # Return next link
        return self.n

    def setNext(self, inn):         # Set next link
        self.n = inn
        return self.n
# /* *** ODSAendTag: Link *** */
