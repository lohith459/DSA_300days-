class Solution(object):
    def firstUniqChar(self, s):
        # Step 1: create a dictionary (hash map) to count characters
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        # Step 2: check from left to right for the first unique char
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i

        # Step 3: if no unique char found, return -1
        return-1