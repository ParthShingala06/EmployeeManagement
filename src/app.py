from flask import Flask

from Empolyee_hour_directory.WorkerController import add_worker, all_workers, top_n_workers
from Empolyee_hour_directory.SalaryController import salary_update, salary_slab
from Empolyee_hour_directory.LogController import log_entry, get_entry_by_id, get_total_time_spent

from Empolyee_hour_directory.Models.Directory import Directory

app = Flask(__name__)

Register = Directory()

@app.route('/add_worker', methods=['POST'])
def add_worker_route():
    return add_worker(Register)

@app.route('/salary_update', methods=['POST'])
def salary_update_route():
    return salary_update(Register)

# @app.route('/promote_worker/<int:worker_id>', methods=['POST'])
# def promote_worker_route(worker_id):
#     return promote_worker(workers, worker_id)

@app.route('/log_entry/<int:worker_id>', methods=['POST'])
def update_worker_route(worker_id):
    return log_entry(Register, worker_id)

@app.route('/entries_by_id/<int:worker_id>', methods=['GET'])
def get_worker_entries_route(worker_id):
    return get_entry_by_id(Register, worker_id)

@app.route('/total_time_by_id/<int:worker_id>', methods=['GET'])
def get_total_time_by_id_route(worker_id):
    return get_total_time_spent(Register, worker_id)

@app.route('/top_workers/<int:number>', methods=['GET'])
def get_top_workers_route(number):
    return top_n_workers(Register, number)

@app.route('/all_workers', methods=['GET'])
def get_all_worker_route():
    return all_workers(Register)

@app.route('/salary_slabs', methods=['GET'])
def salary_slabs_route():
    return salary_slab(Register)

if __name__ == '__main__':
    app.run(debug=True)