class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # Binary search over the timestamped list for the given key
        # timestamp = target

        if not self.map[key]:
            return ""

        moods = self.map[key]

        low = 0
        high = len(moods) - 1

        while low < high:
            mid = (low + high + 1) // 2

            if moods[mid][1] > timestamp:
                high = mid - 1
            else:
                low = mid

        if moods and moods[low][1] <= timestamp:
            return moods[low][0]
        return ""
