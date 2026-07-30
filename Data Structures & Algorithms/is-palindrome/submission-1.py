class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = ''
        for c in s:
            if c.isalnum(): #no spaces or symbols/charac
                filtered_string += c.lower()
        
        left = 0
        right = len(filtered_string)-1

        while (left<right):
            if filtered_string[left] != filtered_string[right]:
                return False
            left +=1
            right -=1

        return True

