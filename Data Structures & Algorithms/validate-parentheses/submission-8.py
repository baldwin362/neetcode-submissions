class Solution:
    def isValid(self, s: str) -> bool:
        """
        Example of valid strings:
        >>> "(){}[]"
        True
        >>> "({)}"
        false
        >>> "({[]})
        True 
        """
        #we use a stack (allowing us to use pop, insert and top properties)
        # to store the opening brackets that still haven't been closed 
        stack = []
        #we use a hash data structure to store the associated opening bracket
        # to each closing bracket 
        # the core logic:
        # --> the last element of the stack should the first opening bracket to
        # be closed --> LIFO : last in first out 
        closeToOpen = {")":"(", "}": "{", "]": "["}
        for char in s:
            if char in closeToOpen:
                if stack and closeToOpen[char]==stack[-1]:
                    stack.pop()
                # we pop because that closing bracket is closing the last 
                # appended opening bracket in stack
                else: 
                    return False 
            else: 
                stack.append(char)
        return True if not stack else False 