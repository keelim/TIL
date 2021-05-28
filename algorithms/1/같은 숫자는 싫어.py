def solution(arr):
    # 함수를 완성하세요
    a=[ v for i,v in enumerate(arr) if arr[i-1]!=arr[i]]

    return a

    