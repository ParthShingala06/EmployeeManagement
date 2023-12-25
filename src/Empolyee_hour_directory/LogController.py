from flask import jsonify, request
import json

from datetime import datetime

from Empolyee_hour_directory.Models.Entry import Entry


def log_entry(Register, worker_id):
    newEntry = Entry(datetime.now())
    return Register.logEntry(newEntry, worker_id)

def get_entry_by_id(Register, worker_id):
    return Register.getEntryById(worker_id)
