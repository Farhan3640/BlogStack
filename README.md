# BlogStack
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)
![Django](https://img.shields.io/badge/Django-5.2.5-green?style=flat-square)
![License](https://img.shields.io/badge/License-Educational-orange?style=flat-square)

A simple Django blog project with MySQL integration.

## Features
- Single-user blog
- Create, edit, delete posts
- Modal view for full content
- Responsive design with Bootstrap

# Prerequisites
Python 3.10+
MySQL installed and running
pip (Python package manager)
Virtual environment recommended

# Setup Instructions
```bash
1. Clone the repository:
git clone https://github.com/Farhan3640/BlogStack.git
cd BlogStack

2. Create a virtual environment:
python -m venv venv

3. Activate the virtual environment:
venv\Scripts\activate

4. Install dependencies:
pip install -r requirements.txt

5. Configure MySQL database:
DB_NAME=blog_db
DB_USER=blog_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
SECRET_KEY=your_secret_key
DEBUG=True

6. Apply migrations:
python manage.py makemigrations
python manage.py migrate
```

# License
This project is for educational purposes.

7. Run the development server
python manage.py runserver
