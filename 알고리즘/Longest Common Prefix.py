class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        s = strs[0]

        for b in len(s):
            i =s[:b+1]
            for ele in strs:
                print(ele)
                print(ele.find(i))
                if ele.find(i) <0:
                    return i[:-1]
        
        