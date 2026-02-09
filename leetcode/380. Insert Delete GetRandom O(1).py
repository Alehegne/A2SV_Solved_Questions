import random
class RandomizedSet:

    def __init__(self):
        self.index_map = defaultdict(int)
        self.ordered = list()
        self.index = 0

    def insert(self, val: int) -> bool:
        if val not in self.index_map:
            #map the index
            self.index_map[val] = self.index
            #add to the list
            self.ordered.append(val)
            #increment the index for tracking
            self.index+=1
            return True
        return False
    def remove(self, val: int) -> bool:
        if val in self.index_map:
            #get the index from mapping
            index = self.index_map[val]
            #swap index and the last
            removed = self.ordered[index]
            last = self.ordered[-1]
            #swap
            self.ordered[index] = last
            self.ordered[-1] = removed
            #pop the last
            self.ordered.pop()
            #update the index map
            self.index_map[last] = index
            del self.index_map[removed]
            #decrement index
            self.index -= 1
            return True
        return False
    def getRandom(self) -> int:
        rand = random.choice(self.ordered)
        return rand
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
