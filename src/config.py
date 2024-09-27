DEBUG = True


# App Config
DOCS_UI='rapidoc'

VERSION = "1.0"
TITLE='Employee Hour Directory API'


INFO = {
    'description': '______________________________\n\n'
                   'The Employee Management API allows users and admins to manage worker information, salaries, and '
                   'timesheet entries with secure token-based authentication. This API provides endpoints for adding workers, '
                   'promoting them, logging time entries, and updating salary details, along with robust security measures.\n\n'
                   '______________________________\n'
                   '**GET YOUR API TOKEN TO ACCESS ALL ENDPOINTS.**\n\n'
                   '______________________________\n\n'
                   '1. **Get an Authentication Token**:\n'
                   '- Endpoint: `/01_auth/get_token`\n'
                   '- Method: `POST`\n'
                   '- Description: Generate an API token for authentication, which is required for all protected routes.\n'
                   '- Required Data: `{ "name": "John Doe", "email": "john@example.com" }`\n\n'

                   '2. **Add Yourself as a Worker**:\n'
                   '- Endpoint: `/02_worker_info/add_worker`\n'
                   '- Method: `POST`\n'
                   '- Description: After getting an auth token, add yourself as a worker.\n'
                   '- Required Data: `{ "worker_name": "John Doe", "position": "Engineer" }`\n\n'

                   '3. **View All Workers**:\n'
                   '- Endpoint: `/02_worker_info/all_workers`\n'
                   '- Method: `GET`\n'
                   '- Description: Fetch a list of all workers in the system. No authentication is required.\n\n'

                   '4. **Promote a Worker (Admin Only)**:\n'
                   '- Endpoint: `/02_worker_info/promote_worker`\n'
                   '- Method: `POST`\n'
                   '- Description: An admin can promote a worker to a higher position.\n'
                   '- Required Data: `{ "worker_id": 1, "position": "Senior Engineer" }`\n\n'

                   '5. **Update Worker Salary (Admin Only)**:\n'
                   '- Endpoint: `/03_salary_info/salary_update`\n'
                   '- Method: `POST`\n'
                   '- Description: Admins can update the salary of a worker based on their position.\n'
                   '- Required Data: `{ "position": "Engineer", "salary": 85000 }`\n\n'
                   
                   '6. **Log Time for a Worker**:\n'
                   '- Endpoint: `/04_timesheet/log_entry/<int:worker_id>`\n'
                   '- Method: `POST`\n'
                   '- Description: Log time entries for a worker. Authentication is required.\n'
                   '- URL Parameter: `worker_id` (the ID of the worker whose time you are logging).\n',
    'contact': {
        'name': 'Parth Shingala',
        'url': 'https://parthshingala06.github.io/',
        'email': 'parth.shingalaa@gmail.com'
    },

    'endpoints_summary': [
        {'path': '/01_auth/get_token', 'method': 'POST', 'description': 'Generate API token for authenticated users.'},
        {'path': '/02_worker_info/add_worker', 'method': 'POST', 'description': 'Add a new worker (requires authentication).'},
        {'path': '/02_worker_info/promote_worker', 'method': 'POST', 'description': 'Promote a worker (admin-only).'},
        {'path': '/02_worker_info/all_workers', 'method': 'GET', 'description': 'Retrieve all workers.'},
        {'path': '/03_salary_info/salary_update', 'method': 'POST', 'description': 'Update worker salary (admin-only).'},
        {'path': '/04_timesheet/log_entry/<int:worker_id>', 'method': 'POST', 'description': 'Log a timesheet entry for a worker (requires authentication).'},
    ]
}