# /* *** ODSATag: ListADT *** */
# /* *** ODSATag: ListADT1 *** */
# List class ADT
class List:
    # Remove all contents from the list, so it is once again empty
    def clear(self):
        pass
    
    # Insert "it" at the current location
    # The client must ensure that the list's capacity is not exceeded 
    def insert(self, it):               
        pass

    # Append "it" at the end of the list
    # The client must ensure that the list's capacity is not exceeded
    def append(self, it):
        pass

    # Remove and return the current element
    def remove(self):                   
        pass
# /* *** ODSAendTag: ListADT1 *** */

# /* *** ODSAendTag: ListADT2 *** */
    # Set the current position to the start of the list
    def moveToStart(self):              
        pass

    # Set the current position to the end of the list
    def moveToEnd(self):                
        pass

    # Move the current position one step left, no change if already at beginning
    def prev(self):                     
        pass

    # Move the current position one step right, no change if already at end
    def next(self):                     
        pass

    # Return the number of elements in the list
    def length(self):                   
        pass
# /* *** ODSAendTag: ListADT2 *** */

# /* *** ODSATag: ListADT3 *** */
    # Return the position of the current element
    def currPos(self):                  
        pass

    # Set the current position to "pos"
    def moveToPos(self, pos):           
        pass

    # Return True if current position is at end of the list
    def isAtEnd(self):                  
        pass

    # Return the current element
    def getValue(self):                 
        pass

    def isEmpty(self):
        pass
# /* *** ODSAendTag: ListADT3 *** */
# /* *** ODSAendTag: ListADT *** */


