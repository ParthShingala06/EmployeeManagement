# Empolyee_hour_directory/routes.py
from apiflask import Schema
from apiflask.fields import Integer, Float, String
from apiflask.validators import Length, Range

from EmployeeManagement import app, auth, role_auth
from EmployeeManagement.Controllers.WorkerController import add_worker, all_workers, top_n_workers, promote_workers
from EmployeeManagement.Controllers.SalaryController import salary_update, salary_slab, salary_by_id
from EmployeeManagement.Controllers.LogController import log_entry, get_entry_by_id, get_total_time_spent
from EmployeeManagement.Models.Directory import Directory
from EmployeeManagement.Auth.Tokens import newUser

Register = Directory()

# Define Schemas for input validation and serialization
class WorkerSchema(Schema):
    worker_name = String(required=True, validate=Length(min=1))
    position = String(required=True, validate=Length(min=1), default="Analyst")

class SalarySchema(Schema):
    position = String(required=True, validate=Length(min=1), default="Analyst")
    salary = Float(required=True, validate=Range(min=0))

class PromoteSchema(Schema):
    worker_id = Integer(required=True)
    position = String(required=True, validate=Length(min=1), default="Analyst")

class TokenSchema(Schema):
    name = String(required=True, validate=Length(min=1))
    email = String(required=True, validate=Length(min=1))


# Auth API routes
@app.post('/01_auth/get_token')
@app.input(TokenSchema, location='json')
def get_token(json_data):
    """Get API Token"""
    return newUser()


# Worker Info API routes
@app.post('/02_worker_info/add_worker')
@app.input(WorkerSchema, location='json')
@app.doc(security='ApiKeyAuth')
@auth.login_required
def add_worker_route(json_data):
    """Add a new worker"""
    return add_worker(Register)

@app.post('/02_worker_info/promote_worker')
@app.input(PromoteSchema, location='json')
@app.doc(security='ApiKeyAuth')
@auth.login_required
@role_auth('Admin', auth)
def promote_worker_route(json_data):
    """Promote a worker"""
    role_auth('Admin', auth)
    return promote_workers(Register)

@app.get('/02_worker_info/top_workers/<int:number>')
def get_top_workers_route(number):
    """Get the top N workers by performance"""
    return top_n_workers(Register, number)

@app.get('/02_worker_info/all_workers')
def get_all_worker_route():
    """Get all workers"""
    return all_workers(Register)


# Salary Info API routes
@app.post('/03_salary_info/salary_update')
@app.input(SalarySchema, location='json')
@app.doc(security='ApiKeyAuth')
@auth.login_required
@role_auth('Admin', auth)
def salary_update_route(json_data):
    """Update salary for a worker"""
    return salary_update(Register)

@app.get('/03_salary_info/salary_by_id/<int:worker_id>')
def get_salary_by_id_route(worker_id):
    """Get salary by worker ID"""
    return salary_by_id(Register, worker_id)

@app.get('/03_salary_info/salary_slabs')
def salary_slabs_route():
    """Get salary slabs"""
    return salary_slab(Register)


# TimeSheet Info API routes
@app.post('/04_timesheet/log_entry/<int:worker_id>')
@app.doc(security='ApiKeyAuth')
@auth.login_required
def update_worker_route(worker_id):
    """Log time entry for a worker"""
    return log_entry(Register, worker_id)

@app.get('/04_timesheet/entries_by_id/<int:worker_id>')
def get_worker_entries_route(worker_id):
    """Get log entries by worker ID"""
    return get_entry_by_id(Register, worker_id)

@app.get('/04_timesheet/total_time_by_id/<int:worker_id>')
def get_total_time_by_id_route(worker_id):
    """Get total time spent by worker ID"""
    return get_total_time_spent(Register, worker_id)


