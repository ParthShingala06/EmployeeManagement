from flask import jsonify, request
import heapq

from Empolyee_hour_directory.Models.Worker import Worker
from Empolyee_hour_directory.LogController import get_total_time_spent

def add_worker(Register):
    data = request.get_json()
    name = data.get('worker_name')
    position = data.get('position')
    if not Register.positionChecker(position):
        return {'error': 'Invalid position'}
    if name:
        newWorker = Worker(name, position)
        return Register.addWorker(newWorker)
    else:
        return {'error': 'Invalid data'}

def all_workers(Register):
    return Register.getAllWorkers()

def top_n_workers(Register, n):
    Workers = Register.getAllWorkers(flat = 1)
    min_heap = []
    for worker in Workers.keys():
        time = get_total_time_spent(Register, int(worker), flat=1)
        if time is not None: 
            heapq.heappush(min_heap, (time, int(worker)))
            if len(min_heap)>n:
                heapq.heappop(min_heap)
    top_n_workers = {}
    for hours, id in min_heap:
        top_n_workers[id] = hours
    return top_n_workers

def promote_workers(Register):
    data = request.get_json()
    id = data.get('worker_id')
    position = data.get('position')
    return Register.promoteWorker(id, position)
