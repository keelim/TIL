def sieve(n):
    """
    에라토스테네스의 체
    """
    if n < 2:
        return []

    #[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    s = [0, 0] + [1] * (n - 1)

    for i in range(2, int(n**0.5)+1):
        if s[i]:
            s[i*2::i] = [0] * ((n - i)//i)
    return [i for i, v in enumerate(s) if v]


def solution(nums):
    primes = sieve(3000)
    set1 = set()
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                a = nums[i] + nums[j] + nums[k]
                if a in primes and not a in set1:
                    count += 1
                    set1.add(a)

    return count
