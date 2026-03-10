class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.k = k
        

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.queue = deque()
            return False
        else:
            self.queue.append(num)
            if len(self.queue) == self.k:
                self.queue.popleft()
                return True
            else:
                return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
