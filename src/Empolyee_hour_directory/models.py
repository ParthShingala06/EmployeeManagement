from flask import jsonify

class Directory:
    def __init__(self):
        self.directory = {
            "workers" : {}
        }
    
    def addWorker(self, WorkerNode):
        WorkerDirectory = self.directory["workers"]
        for worker in WorkerDirectory.values():
            if worker.name == WorkerNode.name:
                return jsonify({'message': 'Worker already Exists', 'worker_id': worker.id}), 201
        worker_id = len(WorkerDirectory) + 1
        WorkerNode.id = worker_id
        self.directory["workers"][worker_id] = WorkerNode
        return jsonify({'message': 'Worker added successfully', 'worker_id': WorkerNode.id}), 201
    
    def logEntry(self, EntryNode, id):
        print(EntryNode.timestamp)
        if id in self.directory["workers"]:
            self.directory["workers"][id].entries.append(EntryNode)
            return jsonify({'message': 'Entry added successfully', 'worker_id': id}), 201    
        else:
            return jsonify({'message': 'No Worker With this ID'}), 201        


class Worker:
    def __init__(self, name):
        self.id = None
        self.name = name
        self.entries = []


class Entry:
    def __init__(self, timestamp):
        self.timestamp = timestamp  


