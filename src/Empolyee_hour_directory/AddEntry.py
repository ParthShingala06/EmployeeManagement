from flask import jsonify, request
from datetime import datetime

from Empolyee_hour_directory.models import Entry


def log_entry(Register, worker_id):
    newEntry = Entry(datetime.now())
    return Register.logEntry(newEntry, worker_id)

# def get_entry_by_id(Register, worker_id):
#     return 