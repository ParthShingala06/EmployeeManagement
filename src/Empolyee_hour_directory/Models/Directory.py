from flask import jsonify

from Empolyee_hour_directory.Models.Salary import Salary


class Directory:
    def __init__(self):
        self.directory = {
            "workers" : {},
            "salary" : Salary()
        }
    
    def updateSalary(self, salary, position):
        self.directory["salary"].SalaryUpdate(position, int(salary))
        return jsonify({'message': 'Salary Updated'}), 201

    def salarySlabs(self):
        return jsonify(self.directory["salary"].serialize())
    
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
        if id in self.directory["workers"]:
            self.directory["workers"][id].entries.append(EntryNode)
            return jsonify({'message': 'Entry added successfully', 'worker_id': id}), 201    
        else:
            return jsonify({'message': 'No Worker With this ID'}), 201

    def getEntryById(self, id, flat = 0):
        if id in self.directory["workers"]:
            if flat == 1: return self.directory["workers"][id]
            serialized_worker = self.directory["workers"][id].serialize_Worker_With_Entity()
            return jsonify(serialized_worker) 
        else: 
            return None   
    
    def getAllWorkers(self, flat = 0):
        workers = {}
        for worker in self.directory["workers"].values():
            serialized_worker = worker.serialize_Worker_Without_Entity()
            workers[int(worker.id)]=serialized_worker
        
        if flat == 1: return workers
        return jsonify(workers)

    def getAllWorkersWithEntities(self, flat = 0):
        workers = {}
        for worker in self.directory["workers"].values():
            serialized_worker = worker.serialize_Worker_With_Entity()
            workers[int(worker.id)]=serialized_worker
        
        if flat == 1: return workers
        return jsonify(workers)






