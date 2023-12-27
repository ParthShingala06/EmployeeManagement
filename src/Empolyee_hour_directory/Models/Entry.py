
class Entry:
    def __init__(self, timestamp):
        self.timestamp = timestamp  

    def serialize(self):
        return (self.timestamp)
