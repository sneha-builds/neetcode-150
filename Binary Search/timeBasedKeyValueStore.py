# Time Based Key-Value Store

"""

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a 
certain timestamp.

Implement the TimeMap class:

-> TimeMap() Initializes the object of the data structure.
-> void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
-> String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
If there are multiple such values, it returns the value associated with the largest timestamp_prev. 
If there are no values, it returns "".

"""

class TimeMap:

    def __init__(self):
        self.keyStore = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = {}
        if timestamp not in self.keyStore[key]:
            self.keyStore[key][timestamp] = []
        self.keyStore[key][timestamp].append(value)        


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        seen = 0

        for time in self.keyStore[key]:
            if time <= timestamp:
                seen = max(seen, time)
        return "" if seen == 0 else self.keyStore[key][seen][-1]
        