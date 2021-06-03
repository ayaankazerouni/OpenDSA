# Array-based queue implementation
from Queue import *
# /* *** ODSATag: AQueue1 *** */
class AQueue(Queue):
    DEFAULT_SIZE = 10
    # Constructors
    def __init__(self, size):
        self.maxSize = size + 1             # One extra space is allocated
        self.rear = 0
        self.front = 1
        self.queueArray = []                # Create queueArray
    
    def __init__(self):
        self.maxSize = DEFAULT_SIZE + 1     # Maximum size of queue
        self.read = 0                       # Index of rear element
        self.front = 1                      # Index of front element
        self.queueArray = []                # Array holding queue elements
# /* *** ODSAendTag: AQueue1 *** */

    def __repr__(self):
        out = ""
        i = self.front
        while i != (self.rear + 1) % self.maxSize:
            out.append(self.queueArray[i])
            out.append(" ")
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
        if length() == 0:
            return None
        return self.queueArray[self.front]

    # Return queue size
    def length(self):
        return ((self.rear + self.maxSize) - self.front + 1) % self.maxSize

    # Check if the queue is empty
    def isEmpty(self):
        return (self.front - self.rear) == 1
# /* *** ODSAendTag: AQueue2 *** */
