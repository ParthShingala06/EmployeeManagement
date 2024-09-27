from flask import request
import heapq

from EmployeeManagement.Controllers.LogController import get_total_time_spent

def salary_update(Register):
    data = request.get_json()
    salary = data.get('salary')
    position = data.get('position')
    return Register.updateSalary(salary, position)

def salary_slab(Register):
    return Register.salarySlabs()

def salary_by_id(Register, id):
    return Register.salaryById(id)