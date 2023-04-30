class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # replace paragraph with a dictionary containing the count of each word AFTER replacing all punctuation with whitespace and splitting to list
        paragraphs = Counter(paragraph.lower().translate(str.maketrans(string.punctuation,' '*len(string.punctuation))).split())
        for i in banned: # use length of banned list
            if i in paragraphs: # iterate through dictionary paragraphs
                del paragraphs[i] # delete any words in paragraphs that are in banned list
        return max(paragraphs, key=paragraphs.get) # return the word with max count -> question stated that largest count is unique
