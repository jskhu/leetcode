[1]: image.png
# Problem: [Insert Question #]
## Code
```python
import operator

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        characters = {}
        sorted_string = ""

        for c in s:
            if c in characters:
                characters[c] += 1
            else:
                characters[c] = 1
        sorted_chars = sorted(characters.items(), key=operator.itemgetter(1), reverse=True)
        for char, num in sorted_chars:
            sorted_string += char * num
        return sorted_string
```
## Proof of Problem (POP)
![alt_text][1]
