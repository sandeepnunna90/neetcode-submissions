class TimeMap:

    def __init__(self):
        self.store = {} # key=string, value = [list of [value, timestamp]]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        result = ''

        if key not in self.store:
            return result
        else:
            values = self.store.get(key, [])
            l, r = 0, len(values) - 1

            while l <= r: 
                mid = (l+r) // 2 

                if values[mid][1] <= timestamp:
                    result = values[mid][0]
                    l = mid + 1
                else: 
                    r = mid - 1 
                
        return result
