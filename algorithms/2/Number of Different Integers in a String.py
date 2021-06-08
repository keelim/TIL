from curses.ascii import isalpha
from itertools import count


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        sample = ''
        for w in word:
            if w.isalpha():
                sample +=' '
            else:
                sample+=w

        result = set()
        data = sample.split()
        for d in data:
            if len(d) != 1 and d.count('0')>=1:
                result.add(d.replace('0', ''))
        return len(result)