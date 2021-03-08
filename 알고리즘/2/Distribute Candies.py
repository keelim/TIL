
from collections import Counter


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # dict1 = {ele: candyType.count(ele) for ele in candyType}
        # dict1 = dict()
        # for ele in candyType:
        #     dict1[ele] = dict1.get(ele, 0) + 1

        # dict1 = Counter(candyType)
        # limit = len(candyType)//2
        # return limit if len(dict1)>= limit else len(dict1)

        # distinctTypes = set(candyType)
        # return min(len(distinctTypes), int(len(candyType)/2))

        distinctTypes = set(candyType)
        return min(len(distinctTypes), len(candyType)//2)
