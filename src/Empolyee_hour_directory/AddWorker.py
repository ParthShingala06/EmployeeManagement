from flask import jsonify, request

from Empolyee_hour_directory.models import Worker


def add_worker(Register):
    data = request.get_json()
    name = data.get('worker_name')
    WorkerDirectory = Register.directory["workers"]

    if name:
        newWorker = Worker(name)
        return Register.addWorker(newWorker)
    else:
        return jsonify({'error': 'Invalid data'}), 400
