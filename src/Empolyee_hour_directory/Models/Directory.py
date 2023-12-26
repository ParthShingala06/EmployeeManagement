from flask import jsonify
import json

from Empolyee_hour_directory.Models.Entry import Entry
from Empolyee_hour_directory.Models.Worker import Worker


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

    def getEntryById(self, id, flat = 0):
        if id in self.directory["workers"]:
            if flat == 1: return self.directory["workers"][id]
            serialized_worker = Worker.serialize_Worker(self.directory["workers"][id])
            return jsonify(serialized_worker) 
        else: 
            return None   
    
    def getAllWorkers(self):
        workers = {}
        for worker in self.directory["workers"].values():
            serialized_worker = Worker.serialize_all_workers(worker)
            workers[int(worker.id)]=serialized_worker
        
        return jsonify(workers)





