[1]: image.png
# Problem: 788
## Code
```python
import math

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        not_allowed = ['3', '4', '7']
        must_contain = ['2', '5', '6', '9']
        for i in range(1, N+1):
            digits = [x for x in list(str(i))]
            contains_valid_digit = False
            for d in digits:
                if d in not_allowed:
                    contains_valid_digit = False
                    break
                if d in must_contain:
                    contains_valid_digit = True
            if contains_valid_digit:
                count += 1
                
        return count
```
## Proof of Problem (POP)
![alt_text][1]
