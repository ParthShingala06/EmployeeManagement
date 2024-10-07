# HRView: Employee Management API - [Live Demo](https://hrview.onrender.com/docs)

## Overview

Welcome to HRView, an Employee Management API developed using Python and Flask. This project focuses on providing a robust Human Resource System, offering features such as Employee Data Management, Working Hour Registry, Promotion, and Salary functionalities. The implementation of this in-memory API has resulted in a 20% reduction in data retrieval times.

## Key Features

1. **Employee Data Management:**
   - Comprehensive functionality for managing employee information efficiently.

2. **Working Hour Registry:**
   - Tracking and managing working hours for accurate attendance records.

3. **Promotion and Salary:**
   - Streamlined processes for handling promotions and salary adjustments.

## Technology Stack

- Python
- Flask
- Object-Oriented Programming (OOP)
- Role-Based Access Control (RBAC)
- RESTful API
- Swagger

## Getting Started

Follow these steps to get started with HRView:

1. Clone the repository:
   ```
   git clone %Repo%
   ```

2. Install dependencies:
   ```
   pip install -U Flask
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```

4. Access the API documentation through Swagger at:
   ```
   http://localhost:5000/api/docs
   ```
   
## Endpoints

### 1. Add Worker

```http
POST http://127.0.0.1:5000/add_worker
```

Request Body:

```json
{
    "worker_name": "John Doe 3",
    "position": "Analyst"
}
```

### 2. Log Entry

```http
GET http://127.0.0.1:5000/log_entry/ID
```

### 3. Entries by ID

```http
GET http://127.0.0.1:5000/entries_by_id/ID
```

### 4. All Workers

```http
GET http://127.0.0.1:5000/all_workers
```

### 5. Total Time by ID

```http
GET http://127.0.0.1:5000/total_time_by_id/ID
```

### 6. Top Workers

```http
GET http://127.0.0.1:5000/top_workers/N
```

### 7. Salary Update

```http
POST http://127.0.0.1:5000/salary_update
```

Request Body:

```json
{
    "salary": 20000,
    "position": "Analyst"
}
```

### 8. Salary Slabs

```http
GET http://127.0.0.1:5000/salary_slabs
```

### 9. Promote Worker

```http
POST http://127.0.0.1:5000/promote_worker
```

Request Body:

```json
{
    "worker_id": 1,
    "position": "Associate"
}
```

### 10. Salary by ID

```http
GET http://127.0.0.1:5000/salary_by_id/4
```

## Getting Started

Follow the steps mentioned in the [Getting Started](#getting-started) section in the README file to set up and run the HRView API.

## Contribution Guidelines

We welcome contributions to HRView. If you have ideas for improvements or new features, feel free to submit a pull request.
