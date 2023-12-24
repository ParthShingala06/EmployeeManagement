from flask import jsonify, request

from Empolyee_hour_directory.models import Worker


def add_worker(Register):
    data = request.get_json()
    name = data.get('worker_name')
    WorkerDirectory = Register.directory["workers"]

    if name:
        worker_id = len(WorkerDirectory) + 1
        newWorker = Worker(name, worker_id)
        Register.addWorker(newWorker, worker_id)
        print(WorkerDirectory[worker_id].name)
        # workers[worker_id] = {'name': name}
        return jsonify({'message': 'Worker added successfully', 'worker_id': worker_id}), 201
    else:
        return jsonify({'error': 'Invalid data'}), 400
