from flask import jsonify, request

from Empolyee_hour_directory.Models.Worker import Worker


def add_worker(Register):
    data = request.get_json()
    name = data.get('worker_name')
    if name:
        newWorker = Worker(name)
        return Register.addWorker(newWorker)
    else:
        return jsonify({'error': 'Invalid data'}), 400

def all_workers(Register):
    return Register.getAllWorkers()