
from EmployeeManagement.Models.Salary import Salary


class Directory:
    def __init__(self):
        self.directory = {
            "workers" : {},
            "salary" : Salary()
        }
    
    def positionChecker(self, position):
        return self.directory["salary"].positionChecker(position)
    
    def updateSalary(self, salary, position):
        return self.directory["salary"].SalaryUpdate(position, int(salary))

    def salarySlabs(self):
        return self.directory["salary"].serialize()
    
    def addWorker(self, WorkerNode):
        WorkerDirectory = self.directory["workers"]
        for worker in WorkerDirectory.values():
            if worker.name == WorkerNode.name:
                return {'message': 'Worker already Exists', 'worker_id': worker.id}
        worker_id = len(WorkerDirectory) + 1
        WorkerNode.id = worker_id
        self.directory["workers"][worker_id] = WorkerNode
        return {'message': 'Worker added successfully', 'worker_id': WorkerNode.id}
    
    def promoteWorker(self, id, position):
        if id in self.directory["workers"] and self.positionChecker(position):
            self.directory["workers"][id].position = position
            return {'message': 'Worker positon promoted', 'position': position}
        else:
            return {'message': 'Data is Invalid', 'worker_id': id}

    def logEntry(self, EntryNode, id):
        if id in self.directory["workers"]:
            self.directory["workers"][id].entries.append(EntryNode)
            return {'message': 'Entry added successfully', 'worker_id': id}   
        else:
            return {'message': 'No Worker With this ID'}

    def getEntryById(self, id, flat = 0):
        if id in self.directory["workers"]:
            if flat == 1: return self.directory["workers"][id]
            serialized_worker = self.directory["workers"][id].serialize_Worker_With_Entity()
            return serialized_worker
        else: 
            if flat == 1: return None 
            return {'message': 'No Worker With this ID'}  
    
    def getAllWorkers(self, flat = 0):
        workers = {}
        for worker in self.directory["workers"].values():
            serialized_worker = worker.serialize_Worker_Without_Entity()
            workers[int(worker.id)]=serialized_worker
        
        if flat == 1: return workers
        return workers

    def getAllWorkersWithEntities(self, flat = 0):
        workers = {}
        for worker in self.directory["workers"].values():
            serialized_worker = worker.serialize_Worker_With_Entity()
            workers[int(worker.id)]=serialized_worker
        
        if flat == 1: return workers
        return workers

    def salaryById(self, id):
        if id in self.directory["workers"]:
            position = self.directory["workers"][id].position
            salary = self.directory["salary"].getSalary(position)
            return str(salary)
        else: 
            return {'message': 'No Worker With this ID'}            





