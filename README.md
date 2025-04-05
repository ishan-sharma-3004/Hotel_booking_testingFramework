# Hotel_Booking_Testing_Framework

A pytest based framework for testing the RESTful Booking API  with self healing capabilities.

## Features
- Complete CRUD operation testing (Create, Read, Update, Delete).
- Authentication and Token management.
- Allure Reporting.
- Parallel test execution.
- CI/CD ready with Tox.

## Setup Instructions

### Prerequisites
- Python 3.10+
- pip package manager
- Git

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ishan-sharma-3004/Hotel_Booking_Testing_framework.git
    cd Hotel_Booking_Testing_framework
    ```
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate #Linux/MacOS
    venv/Scripts/activate #Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Basic Test Execution:
    ```bash
    pytest tests/
    ```

5. Run with allure reporting:
    ```bash
    pytest tests/ --alluredir=allure-results
    allure serve allure-results
    ```

6. Run with parallel execution:
    ```bash
    pytest tests/ -n auto
    ```

7. Run with Tox(Multiple Python Versions)
    ```bash
    tox
    ```


