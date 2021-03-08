class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        dict1 = dict(zip(alpha, morse))
        print(dict1)
        s = ''
        set1 = set()
        for ele in words:
            s = ''.join(map(lambda ele: dict1[ele], ele))
            set1.add(s)

        return len(set1)
