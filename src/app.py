import config
from apiflask import APIFlask

from EmployeeManagement import app

if __name__ == '__main__':
    app.run(debug=True)