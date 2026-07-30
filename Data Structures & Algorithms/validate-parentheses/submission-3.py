class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]":"[", ")": "(", "}": "{"}

        for char in s:
            if char in dict: #if it is a closing bracket
                if stack and stack[-1] == dict[char]: #if char is closing bracket, then we check if it correctly matches something on the stack. (array -> stack, only put on stack if not matching)
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
        
 #As we loop through the string:
#If we see an opening bracket ((, [, {) → we push it onto the stack.
#If we see a closing bracket (), ], }) → we check whether it correctly matches the top of the stack.

# if stack means - if stack is not empty