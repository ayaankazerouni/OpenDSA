from Link import *
from Queue import *
# /* *** ODSATag: LQueue1 *** */
# Linked queue implementation
class LQueue(Queue):
    # Class variables
    #   Link front  // Pointed to front queue node
    #   Link rear   // Pointer to rear queue node
    #   int size    // Number of elements in queue

    # Constructor
    def __init__(self, size=0): # Ignores Size
        self.front = self.rear = Link(None)
        self.size = 0
# /* *** ODSAendTag: LQueue1 *** */
   
    # Reinitialize queue
    def clear(self):
        self.front = self.rear = Link(None)
        self.size = 0

    def __eq__(self, other):
        return (isinstance(other, LQueue) and self.size == other.size and 
                self.rear == other.rear and self.front == other.front)
    
    def __repr__(self):
        out = ""
        temp = self.front.next()
        while temp != None:
            out += str(temp.element())
            out += " "
            temp = temp.next()
        return out
# /* *** ODSATag: LQueue2 *** */

# /* *** ODSATag: LQueueEnqueue *** */
    
    # Put element on rear
    def enqueue(self, it):
        self.rear.setNext(Link(None, it))
        self.rear = self.rear.next()
        self.size += 1
        return True
# /* *** ODSAendTag: LQueueEnqueue *** */

# /* *** ODSATag: LQueueDequeue *** */
    # Remove and return element from front
    def dequeue(self):
        if self.size == 0:
            return None
        it = self.front.next().element()                # Store the value
        self.front.setNext(self.front.next().next())    # Advance front
        if self.front.next() == None:                   # Last element
            self.rear = self.front
        self.size -= 1
        return it                                       # Return element
# /* *** ODSAendTag: LQueueDequeue *** */

    # Return front element
    def frontValue(self):
        if self.size == 0:
            return None
        return self.front.next().element()

    # Return queue size
    def length(self):
        return self.size

    # Check if the queue is empty
    def isEmpty(self):
        return (self.size == 0)
# /* *** ODSAendTag: LQueue2 *** */
