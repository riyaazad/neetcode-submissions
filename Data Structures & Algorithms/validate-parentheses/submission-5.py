class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]":"[", ")":"(", "}":"{"}

        for char in s: #closing
            if char in dict:
                if stack and stack[-1] == dict[char]: #if last item is opening
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack #to make sure nothing left in stack
