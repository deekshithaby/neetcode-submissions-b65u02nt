from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        
        for word in strs:
            # store length + '#' + word
            encoded += str(len(word)) + "#" + word
        
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            
            # move j until we find '#'
            while s[j] != '#':
                j += 1
            
            # get length of word
            # Python slicing works like: s[start:end]
            # - includes the character at index `start`
            # - excludes the character at index `end`
            #
            # So:
            # s[0:1] → takes only the character at index 0 (not index 1)
            # Example:
            # s = "4#neet"
            # s[0:1] → "4"
            length = int(s[i:j])
            
            # extract the word
            start = j + 1
            end = start + length
            word = s[start:end]
            res.append(word)
            
            # move i to the next segment
            i = end
        
        return res