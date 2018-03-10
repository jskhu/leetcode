class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        word_heads = self.sortWordHeads(words)
        num_matching_subsequences = 0

        for letter in S:
            if letter in word_heads:
                # Remove first letter from words
                for i, word in enumerate(word_heads[letter]):
                    word_heads[letter][i] = word_heads[letter][i][1:]
                    if len(word_heads[letter][i]) == 0:
                        num_matching_subsequences += 1
                word_heads[letter] = [x for x in word_heads[letter] if len(x) > 0]

                new_word_heads = list(word_heads[letter])
                word_heads.pop(letter)
                for word in new_word_heads:
                    if word[0] in word_heads:
                        word_heads[word[0]].append(word)
                    else:
                        word_heads[word[0]] = [word]

        return num_matching_subsequences

    def sortWordHeads(self, words):
        new_words = {}
        for word in words:
            if word[0] in new_words:
                new_words[word[0]].append(word)
            else:
                new_words[word[0]] = [word]

        return new_words
