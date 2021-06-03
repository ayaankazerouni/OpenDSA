# /* *** ODSATag: LQueue1 *** */
from Link import *
# Linked queue implementation
class LQueue(Queue):
    # Constructors
    def __init__(self):
        self.front = self.rear = Link(None)
        self.size = 0

    def __init__(self, size):                           # Ignores Size
        self.front = self.rear = Link(None)
        self.size = 0
# /* *** ODSAendTag: LQueue1 *** */
    
    def clear(self):                                    # Reinitialize queue
        self.front = self.rear = Link(None)
        self.size = 0

    def __repr__(self):
        out = ""
        temp = self.front.next()
        while temp != None:
            out.append(temp.element())
            out.append(" ")
            temp = temp.next()
        return out
# /* *** ODSATag: LQueue2 *** */

# /* *** ODSATag: LQueueEnqueue *** */
    def enqueue(self, it):                              # Put element on rear
        self.rear.setNext(Link(it, None))
        self.rear = self.rear.next()
        self.size += 1
        return True
# /* *** ODSAendTag: LQueueEnqueue *** */

# /* *** ODSATag: LQueueDequeue *** */
    def dequeue(self):                                  # Remove and return element from front
        if self.size == 0:
            return None
        it = self.front.next().element()                # Store the value
        self.front.setNext(self.front.next().next())    # Advance front
        if self.front.next() == None:                   # Last element
            self.rear = self.front
        size -= 1
        return it                                       # Return element
# /* *** ODSAendTag: LQueueDequeue *** */

    def frontValue(self):                               # Return front element
        if self.size == 0:
            return None
        return self.front.next().element()

    def length(self):                                   # Return queue size
        return self.size

    def isEmpty(self):                                  # Check if the queue is empty
        return (self.size == 0)
# /* *** ODSAendTag: LQueue2 *** */
