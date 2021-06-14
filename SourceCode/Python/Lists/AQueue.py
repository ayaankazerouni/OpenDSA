# Array-based queue implementation
from Queue import *
# /* *** ODSATag: AQueue1 *** */
class AQueue(Queue):
    DEFAULT_SIZE = 10
    # Constructor
    def __init__(self, size=DEFAULT_SIZE):
        self.maxSize = size + 1     # Maximum size of queue, one extra space is allocated
        self.rear = 0               # Index of rear element
        self.front = 1              # Index of front element
        self.queueArray = [None]*self.maxSize  # Array holding queue elements
# /* *** ODSAendTag: AQueue1 *** */

    def __eq__(self, other):
        return (isinstance(other, AQueue) and self.maxSize == other.maxSize and 
                self.rear == other.rear and self.front == other.front and self.queueArray == other.queueArray)
    
    def __repr__(self):
        out = ""
        i = self.front
        while i != (self.rear + 1) % self.maxSize:
            out += str(self.queueArray[i])
            out += " "
            i = (i + 1) % self.maxSize
        return out
# /* *** ODSATag: AQueue2 *** */

    # Reinitialize
    def clear(self):
        self.rear = 0
        self.front = 1

    # Put "it" in queue
    def enqueue(self, it):
        if ((self.rear + 2) % self.maxSize) == self.front:  # Full
            return False
        self.rear = (self.rear + 1) % self.maxSize  # Circular increment
        self.queueArray[self.rear] = it
        return True

    # Remove and return front value
    def dequeue(self):
        if self.length == 0:
            return None
        it = self.queueArray[self.front]
        self.front = (self.front+1) % self.maxSize
        return it

    # Return front value
    def frontValue(self):
        if self.length == 0:
            return None
        return self.queueArray[self.front]

    # Return queue size
    def length(self):
        return ((self.rear + self.maxSize) - self.front + 1) % self.maxSize

    # Check if the queue is empty
    def isEmpty(self):
        return (self.front - self.rear) == 1
# /* *** ODSAendTag: AQueue2 *** */
