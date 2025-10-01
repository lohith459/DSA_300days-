class Solution(object):
    def firstUniqChar(self, s):
        # Step 1: create a dictionary (hash map) to count characters
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1  # .get is a function method  we use 0 for when there is no exist then return 0

        # Step 2: check from left to right for the first unique char
        for i, ch in enumerate(s):  # enumerate ues's for returns both index an value 
            if counts[ch] == 1:
                return i

        # Step 3: if no unique char found, return -1
        return-1