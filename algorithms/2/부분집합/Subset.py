def subset(nums):
    n = len(nums)

    sub = [[]]

    for num in nums:
        sub += [cur + [num] for cur in sub]
        print(sub)
    return sub


a = subset([1, 2, 3])
print(a)


def subset2(nums):
    def backtracking(first = 0, cur =[]):
        if len(cur) == ele:
            output.append(cur[:])
        
    output = []
    n = len(nums)
    for ele in range(n+1):
        backtracking()

    return output
