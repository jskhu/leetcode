[1]: image.png
# Problem: [Insert Question #]
## Code
```python
class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        def count(limit):
            total_subs = 0
            current_subs = 0
            for x in A:
                if x <= limit:
                    current_subs += 1
                    total_subs += current_subs
                else:
                    current_subs = 0

            return total_subs
        return count(R) - count(L - 1)
```
## Proof of Problem (POP)
![alt_text][1]
