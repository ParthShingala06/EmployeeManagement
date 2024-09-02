# Empolyee_hour_directory/routes.py
from apiflask import Schema
from apiflask.fields import Integer, Float, String
from apiflask.validators import Length, Range



from EmployeeManagement import app
from EmployeeManagement.Controllers.WorkerController import add_worker, all_workers, top_n_workers, promote_workers
from EmployeeManagement.Controllers.SalaryController import salary_update, salary_slab, salary_by_id
from EmployeeManagement.Controllers.LogController import log_entry, get_entry_by_id, get_total_time_spent
from EmployeeManagement.Models.Directory import Directory

Register = Directory()

# Define Schemas for input validation and serialization
class WorkerSchema(Schema):
    worker_name = String(required=True, validate=Length(min=1))
    position = String(required=True, validate=Length(min=1))

class SalarySchema(Schema):
    position = String(required=True, validate=Length(min=1))
    salary = Float(required=True, validate=Range(min=0))

class PromoteSchema(Schema):
    worker_id = Integer(required=True)
    position = String(required=True, validate=Length(min=1))

# Define API routes
@app.post('/add_worker')
@app.input(WorkerSchema, location='json')
def add_worker_route(json_data):
    """Add a new worker"""
    return add_worker(Register)

@app.post('/salary_update')
@app.input(SalarySchema, location='json')
def salary_update_route(json_data):
    """Update salary for a worker"""
    return salary_update(Register)

@app.post('/log_entry/<int:worker_id>')
def update_worker_route(worker_id):
    """Log time entry for a worker"""
    return log_entry(Register, worker_id)

@app.post('/promote_worker')
@app.input(PromoteSchema, location='json')
def promote_worker_route(json_data):
    """Promote a worker"""
    return promote_workers(Register)

@app.get('/entries_by_id/<int:worker_id>')
def get_worker_entries_route(worker_id):
    """Get log entries by worker ID"""
    return get_entry_by_id(Register, worker_id)

@app.get('/total_time_by_id/<int:worker_id>')
def get_total_time_by_id_route(worker_id):
    """Get total time spent by worker ID"""
    return get_total_time_spent(Register, worker_id)

@app.get('/top_workers/<int:number>')
def get_top_workers_route(number):
    """Get the top N workers by performance"""
    return top_n_workers(Register, number)

@app.get('/salary_by_id/<int:worker_id>')
def get_salary_by_id_route(worker_id):
    """Get salary by worker ID"""
    return salary_by_id(Register, worker_id)

@app.get('/all_workers')
def get_all_worker_route():
    """Get all workers"""
    return all_workers(Register)

@app.get('/salary_slabs')
def salary_slabs_route():
    """Get salary slabs"""
    return salary_slab(Register)
