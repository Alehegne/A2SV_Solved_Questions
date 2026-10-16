
class FreqStack:
    def __init__(self):
        self.frequency_count = defaultdict(int)
        self.priority_queue = []
        self.timestamp = 0

    def push(self, val: int) -> None:
        self.timestamp += 1
        self.frequency_count[val] += 1
        heappush(self.priority_queue, 
                (-self.frequency_count[val], -self.timestamp, val))

    def pop(self) -> int:
        _, _, value = heappop(self.priority_queue)
        self.frequency_count[value] -= 1
        return value


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
