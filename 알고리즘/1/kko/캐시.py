from collections import deque
import collections

def solution(cacheSize, cities):
    elapsed: int = 0
    cache = collections.deque(maxlen=cacheSize) #  dequeu 를 이용하여 캐시를 구한 것이다.

    for city in cities:
        city = city.lower()

        if city in cache:
            cache.remove(city)
            cache.append(city)
            elapsed+=1
        else:
            cache.append(city)
            elapsed+=5
    # elapesed 실행 시간
    return elapsed