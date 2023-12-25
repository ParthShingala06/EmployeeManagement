from flask import Flask

# from working_hour_registry import app
from src.Empolyee_hour_directory.WorkerController import add_worker, all_workers
from src.Empolyee_hour_directory.LogController import log_entry, get_entry_by_id
from Empolyee_hour_directory.Models.Directory import Directory

app = Flask(__name__)

Register = Directory()

@app.route('/add_worker', methods=['POST'])
def add_worker_route():
    print("Yes")
    return add_worker(Register)

# @app.route('/promote_worker/<int:worker_id>', methods=['POST'])
# def promote_worker_route(worker_id):
#     return promote_worker(workers, worker_id)

@app.route('/log_entry/<int:worker_id>', methods=['POST'])
def update_worker_route(worker_id):
    return log_entry(Register, worker_id)

@app.route('/entries_by_id/<int:worker_id>', methods=['GET'])
def get_worker_entries_route(worker_id):
    return get_entry_by_id(Register, worker_id)

@app.route('/all_workers', methods=['GET'])
def get_all_worker_route():
    return all_workers(Register)

if __name__ == '__main__':
    app.run(debug=True)