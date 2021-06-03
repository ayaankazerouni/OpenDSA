# /* *** ODSATag: Freelink *** */
class Link:
    # Constructor
    def __init__(self, inn, it=None):
        self.e = it         # Value for this node
        self.n = inn        # Point to next node in list

    def element(self):      # Return the value
        return self.e

    def setElement(self, it):   # Set element value
        self.n = inn
        return self.n

    def next(self):     # Return next Link
        return self.n

    def setNext(self, inn): # Set next link
        self.n = inn
        return self.n

    # Extenstions to support freelists
    freelist = None

    # Return a new linke, from freelist if possible
    def get(self, it, inn):
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
