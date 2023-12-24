from flask import jsonify, request
from datetime import datetime

from Empolyee_hour_directory.models import Worker


def log_entry(workers, worker_id):
    if worker_id in workers:

        Worker.addEntry()

    #     return jsonify({'message': f'Entry logged successfully by Worker {worker_id}', 'entry': entry.to_dict()}), 201
    # else:
    #     return jsonify({'error': 'Invalid data'}), 400