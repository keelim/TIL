def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(
            bin(arr1[i] | arr2[i])[2:]
            .zfill(n)
            # .rjust(n) 를 사용하는 방법도 있다.
            .replace('1', '#')
            .replace('0', '.')
        )
    return answer
