from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1 = dict()

        for ele in arr:
            dict1[ele] = dict1.get(ele, 0) + 1
        
        print(dict1)
        result =[]
        for value in dict1.values():
            print(value, result)
            
            if(len(result)==0):
                result.append(value)
                continue
                
            if value in result:
                return False

            result.append(value)
            
        return True
    
    def uniqueOccurrences2(self, arr: List[int]) -> bool:
        
        myDict = Counter(arr)
        return len(myDict.values()) == len(set(myDict.values()))    
            

