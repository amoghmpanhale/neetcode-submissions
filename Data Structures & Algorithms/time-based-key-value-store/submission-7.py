class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((value, timestamp))
        else:
            self.map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        # Binary search over the timestamped list for the given key
        # timestamp = target

        if key not in self.map:
            return ""

        moods = self.map[key]

        low = 0
        high = len(moods) - 1

        if timestamp < moods[0][1]:
            return ""

        while low <= high:
            mid = (low + high) // 2

            if moods[mid][1] == timestamp:
                return moods[mid][0]
            elif moods[mid][1] < timestamp:
                low = mid + 1
            else:
                high = mid - 1

        return moods[high][0]
