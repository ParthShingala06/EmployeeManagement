class Directory:
    def __init__(self):
        self.directory = {
            "workers" : {}
        }
    
    def addWorker(self, WorkerNode, id):
        WorkerDirectory = self.directory["workers"]
        

        self.directory["workers"][id] = WorkerNode
    
    def logEntry(self, timestamp, id):
        self.directory["workers"][id].entries.append(timestamp)


class Worker:
    def __init__(self, name, id):
        self.id = id  # Assign an ID when adding to the system
        self.name = name
        self.entries = []


class Entry:
    def __init__(self, timestamp):
        self.timestamp = timestamp  


