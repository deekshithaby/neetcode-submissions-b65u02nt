import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        l=0
        r = len(clean_s) - 1

        while l < r:
            if clean_s[l] != clean_s[r]:
                return False
            l += 1
            r -= 1

        return True