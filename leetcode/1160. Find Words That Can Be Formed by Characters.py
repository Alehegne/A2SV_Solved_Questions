class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:


        char_freq=Counter(chars)
        len_=0
        for word in words:

            w_c=Counter(word)
            isValid=True
            for ch,freq in w_c.items():

                if char_freq[ch]<freq:
                    isValid=False
            if not isValid:
                continue
            len_+=len(word)
        return len_
        