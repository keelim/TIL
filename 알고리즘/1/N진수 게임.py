DIGITS = list('0123456789ABCDEF')


def n_to_base(n, base):
    if n == 0:
        return '0'

    # 각 자리수에 해당하는 문자열을 담을 리스트
    result = []
    while n > 0:
        # 제일 마지막 자리의 숫자 구하기. 예를 들어 1658이면 '8'
        result.append(DIGITS[n % base])
        # 제일 마지막 자리 제거. 예를 들어 1658이면 165로
        n = int(n // base)

    # 뒤집어서 반환. 예를 들어 '8561'이면 '1658'
    return ''.join(result[::-1])


def solution(n, t, m, p):
    digits = []
    turn = 0
    while len(digits) < t * m:
        digits += list(n_to_base(turn, n))
        turn += 1
    return ''.join(digits[p-1::m][:t])