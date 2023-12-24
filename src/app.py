from flask import Flask

# from working_hour_registry import app
from Empolyee_hour_directory.AddWorker import add_worker
from Empolyee_hour_directory.AddEntry import log_entry
from Empolyee_hour_directory.models import Directory

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

# Other routes related to working hours (log_entry, get_analytics) can be added here

if __name__ == '__main__':
    app.run(debug=True)