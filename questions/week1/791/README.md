[1]: image.png
# Problem: 791
## Code
```python
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """

        ordering = list(S)
        count = {}

        for char in T:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        custom_sort_string = ''
        for order in ordering:
            if order in count:
                custom_sort_string += order * count[order]

        not_ordered_chars =  set(count) - set(ordering)

        for char in not_ordered_chars:
            custom_sort_string += char * count[char]

        return custom_sort_string
```
## Proof of Problem (POP)
![alt_text][1]
