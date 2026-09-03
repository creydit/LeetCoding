class TimeMap:
    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        
        self.mp[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        
        arr = self.mp[key]
        lo = 0
        hi = len(arr) - 1
        ans = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)