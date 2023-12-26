from flask import jsonify, request
import json
from datetime import datetime

from Empolyee_hour_directory.Models.Entry import Entry


def log_entry(Register, worker_id):
    newEntry = Entry(datetime.now())
    return Register.logEntry(newEntry, worker_id)

def get_entry_by_id(Register, worker_id):
    return Register.getEntryById(worker_id)

def get_total_time_spent(Register, worker_id):
    entries = Register.getEntryById(worker_id, flat = 1).entries
    print(entries)
    if entries is None or len(entries) == 0:
        return jsonify({'message': 'No Entries for this worker', 'worker_id': worker_id}), 201  
    else:
        if len(entries)%2 !=0:
            length = len(entries) -1
        else: 
            length = len(entries)
        total_time = sum((entries[i+1].timestamp - entries[i].timestamp).total_seconds()/3600 for i in range(0,length,2))  
    
    return jsonify({'Total Work Hours': total_time, 'worker_id': worker_id}), 201
