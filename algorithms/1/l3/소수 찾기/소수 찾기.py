primes = set()

def is_prime(number:int) -> bool:
    if number in (0, 1):
        return False
    for i in range(2, number//2+1):
        if number % i == 0:
            return False

    return True


def makeCombinations(str1, str2):
    if str1 != "":
        if is_prime(int(str1)):
            primes.add(int(str1))

    for i in range(len(str2)):
        print(str1 + str2[i], str2[:i] + str2[i + 1:])
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])


def solution(numbers):
    makeCombinations("", numbers)

    return len(primes)

print(solution("17"))
print(solution("011"))