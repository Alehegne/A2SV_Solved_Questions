class FrequencyTracker:

    def __init__(self):
        self.freq = Counter()
        # self.values = set()
        self.valFreq = Counter()
        

    def add(self, number: int) -> None: 
        if self.valFreq[self.freq[number]]:
            self.valFreq[self.freq[number]]-=1
            if self.valFreq[self.freq[number]] == 0:
                del self.valFreq[self.freq[number]]
        self.freq[number]+=1
        # self.values = set(self.freq.values())
        self.valFreq[self.freq[number]]+=1
        

    def deleteOne(self, number: int) -> None:
        if number in self.freq:
            self.valFreq[self.freq[number]]-=1
            if self.valFreq[self.freq[number]]==0:
                del self.valFreq[self.freq[number]]

            self.freq[number]-=1
            if self.freq[number] == 0:
                del self.freq[number]
                return
            self.valFreq[self.freq[number]]+=1
        
        

    def hasFrequency(self, frequency: int) -> bool:
        print("valfreq:",self.valFreq)
        if frequency in self.valFreq:
            return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
