class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        langList = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(sentence)):
            if sentence[i][0].lower() in langList:
                sentence[i] = sentence[i] + 'ma'
            else:
                sentence[i] = sentence[i][1:] + sentence[i][0] + 'ma'
            sentence[i] = sentence[i] + ((i+1) * 'a')
        return ' '.join(sentence)
