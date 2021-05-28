# 중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ele1 = {}
        start = 0
        max_length = 0

        for index, char in enumerate(s):
            # 이미 등장 했던 문자라면 start 를 갱신하고 새로 시작
            if char in ele1 and start <= ele1[char]:
                start = ele1[char]+1
            else:
                #  아니면 길이를 늘려준다
                max_length = max(max_length, index-start+1)

            # 현재 문자 위치를 삽입
            ele1[char] = index

        return max_length
