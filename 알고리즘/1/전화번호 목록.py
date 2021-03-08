def solution(phone_book):
    answer = True
    dict1 = dict()
    for ele in phone_book:
        dict1[ele] = 1

    for ele in phone_book:
        temp = ""
        for number in ele:
            temp += number
            if temp in dict1 and temp != ele:
                answer = False
    return answer