class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringg = ""
        for c in s:
            if c.isalnum():
                stringg +=c.lower()



        left = 0
        right = len(stringg)-1

        while left<right:
            if stringg[left] != stringg[right]:
                return False
            left +=1
            right -=1
        return True
