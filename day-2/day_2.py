class Solution:
    def romanToInt(self, s):
        # Mapping Roman symbols to integer values
        roman_map = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,            # defining key and value in romanmap 
            'D': 500, 'M': 1000
        }

        total = 0  # we give initially total 0 we can the total value into this 
        n = len(s)  # through the len we can loop each value 

        for i in range(n):
            # Check if next value exists and current < next
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]  # subtract in special cases
            else:
                total += roman_map[s[i]]  # otherwise just add

        return total

  # simply we can say ..
        # < Add 
        # > subtract 
