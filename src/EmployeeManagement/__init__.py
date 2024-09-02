import config
from apiflask import APIFlask


app = APIFlask(__name__, version=config.VERSION, title=config.TITLE, docs_ui=config.DOCS_UI)
app.config.from_pyfile('../config.py')


from EmployeeManagement import routes