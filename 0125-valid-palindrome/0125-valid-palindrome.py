class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s1= []
        for i in range(0,len(s)):
            if s[i].isalnum(): 
                s1.append(s[i])

        if s1 == s1[::-1]:
            return True
        else:
            return False

