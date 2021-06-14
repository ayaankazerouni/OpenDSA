# /* *** ODSATag: Freelink *** */
freelist = None # Extenstions to support freelists
class Link:
    
    # Constructor
    def __init__(self, inn, it=None):
        self.e = it         # Value for this node
        self.n = inn        # Point to next node in list

    def element(self):      # Return the value
        return self.e

    def setElement(self, it):   # Set element value
        self.e = it
        return self.e

    def next(self):     # Return next Link
        return self.n

    def setNext(self, inn): # Set next link
        self.n = inn
        return self.n

    # Return a new link, from freelist if possible
    def get(self, inn, it=None):
        global freelist
        if freelist == None:
            return Link(inn, it)    # Get from "new"
        temp = freelist             # Get from freelist
        freelist = freelist.next()
        temp.setElement(it)
        temp.setNext(inn)
        return temp
    
    # Return a Link node to the freelist
    def release(self):
        self.e = None       # Drop reference to the element
        self.n = freelist
        freelist = self
# /* *** ODSAendTag: Freelink *** */
