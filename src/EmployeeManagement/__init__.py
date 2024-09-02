import config
from apiflask import APIFlask
from flask_httpauth import HTTPTokenAuth
from EmployeeManagement.Auth.Tokens import verifyToken

# Initialize the APIFlask app
app = APIFlask(__name__, version=config.VERSION, title=config.TITLE, docs_ui=config.DOCS_UI)

# Load configuration file
app.config.from_pyfile('../config.py')

# Optional: Additional OpenAPI Info (not mandatory for authentication to work)
app.info = {
    'description': 'Employee Management API',
    'termsOfService': 'http://example.com/terms/',
    'contact': {
        'name': 'API Support',
        'url': 'http://www.example.com/support',
        'email': 'support@example.com'
    },
    'license': {
        'name': 'Apache 2.0',
        'url': 'http://www.apache.org/licenses/LICENSE-2.0.html'
    }
}

# Define security scheme for API Key (if needed)
app.security_schemes = {
    'ApiKeyAuth': {
      'type': 'apiKey',
      'in': 'header',
      'name': 'X-API-Key',
    }
}

# Initialize HTTP Token Auth for Bearer tokens
auth = HTTPTokenAuth(scheme='Bearer')

# Verify token function for Bearer authentication
@auth.verify_token
def verify_token(token):
    return verifyToken()

# Import routes after initializing the app and auth
from EmployeeManagement import routes
