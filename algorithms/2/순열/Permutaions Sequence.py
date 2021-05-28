from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        line = map(str, [ele for ele in range(1, n)])
        list1 = permutations(line)
        print(list1)

