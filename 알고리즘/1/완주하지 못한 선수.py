def solution(participant, completion):
    dict1={}
    answer=''
    for ele in participant:
        dict1[ele] = dict1.get(ele, 0)+1
    for ele in completion:
        dict1[ele]-=1
            
    for i, ele in dict1.items():
        if ele>0:
            return i