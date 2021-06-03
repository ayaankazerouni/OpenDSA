# /* *** ODSATag: ListADT *** */
# /* *** ODSATag: ListADT1 *** */
class List:                             # List class ADT
    def clear(self):                    # Remove all contents from the list, so it is once again empty
        pass

    def insert(self, it):               # Insert "it" at the current location
        pass                            # The client must ensure that the list's capacity is not exceeded

    def append(self, it):               # Append "it" at the end of the list
        pass                            # The client must ensure that the list's capacity is not exceeded

    def remove(self):                   # Remove and return the current element
        pass
# /* *** ODSAendTag: ListADT1 *** */

# /* *** ODSAendTag: ListADT2 *** */
    def moveToStart(self):              # Set the current position to the start of the list
        pass

    def moveToEnd(self):                # Set the current position to the end of the list
        pass

    def prev(self):                     # Move the current position one step left, no change if already at beginning
        pass

    def next(self):                     # Move the current position one step right, no change if already at end
        pass

    def length(self):                   # Return the number of elements in the list
        pass
# /* *** ODSAendTag: ListADT2 *** */

# /* *** ODSATag: ListADT3 *** */

    def currPos(self):                  # Return the position of the current element
        pass

    def moveToPos(self, pos):           # Set the current position to "pos"
        pass

    def isAtEnd(self):                  # Return True if current position is at end of the list
        pass

    def getValue(self):                 # Return the current element
        pass

    def isEmpty(self):
        pass
# /* *** ODSAendTag: ListADT3 *** */
# /* *** ODSAendTag: ListADT *** */


