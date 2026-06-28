class TimeMap:

    def __init__(self):
        # mapping name to a special array that is timestamp to value
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [(timestamp, value)]
        else:
            self.d[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        timestamps = self.d[key]

        l, r = 0, len(timestamps) - 1

        while l <= r:
            m = (l + r) // 2

            if timestamp == timestamps[m][0]:
                return timestamps[m][1]
            elif timestamp < timestamps[m][0]:
                r = m - 1
            else:
                l = m + 1

        if r < 0:
            return ""
        
        return timestamps[r][1]

            
        
