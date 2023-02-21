# CeListial

## Overview

CeListial is a task management application that enables users to create and assign projects to team members. The app is built using Django, a high-level Python web framework, and utilizes the Django REST framework to handle data transfer. In addition to creating and assigning tasks, Tasker also allows users to easily update or delete tasks and projects. When a project is deleted, the app uses the "CASCADE" feature to ensure that all associated tasks are also deleted, providing a streamlined and efficient workflow.

Django ORM manages the database models and queries, enabling seamless data retrieval and storage. The front-end is designed using HTML and CSS, providing a user-friendly interface for managing projects and tasks.

## Getting Started

1. Clone this [repository](https://github.com/sukchung/CeListial) to your local computer
2. Navigate or cd into the cloned repository
3. Run the following commands to activate your virtual environment
    ```
    python -m venv .venv
    source .venv/bin/activate
    ```
4. Run the following command to install requirements
    ```
    pip install -r requirements.txt
    ```
5. Run the following command to make migrations
    ```
    python manage.py migrate
    ```
6. Run the following command to start up the development server
    ```
    python manage.py runserver
    ```
7. View the web application on your browser: http://localhost:8000/
8. That is it. You are good to go! 🏁
