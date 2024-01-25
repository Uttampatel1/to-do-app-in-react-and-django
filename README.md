
# To-Do App in React and Django 🚀

## Description 📝

This is a delightful To-Do application built using React for the front end and Django for the back end. The application provides a user-friendly interface to manage your tasks, bringing joy to your productivity journey.

## Setup ⚙️

### Backend (Django)

1. Ensure you have Python installed. Download it from [python.org](https://www.python.org/).

3. Install the required Python packages using pip.

```bash
pip install -r requirements.txt
```

3. Apply migrations to set up the database.

```bash
python manage.py migrate
```

4. Run the Django development server.

```bash
python manage.py runserver
```

The Django backend will be accessible at `http://localhost:8000/`.

### Frontend (React)

1. Ensure you have Node.js and npm installed. Download them from [nodejs.org](https://nodejs.org/).

2. Navigate to the `frontend` directory.

```bash
cd frontend
```

3. Install the required npm packages.

```bash
npm install
```

4. Run the React development server.

```bash
npm start
```

The React frontend will be accessible at `http://localhost:3000/`.

## API Endpoints 🛣️

### 1. Overview

- **Endpoint:** `/`
- **Method:** `GET`
- **Description:** Get an overview of the API.

### 2. Task List

- **Endpoint:** `/task-list/`
- **Method:** `GET`
- **Description:** Get a list of all tasks.

### 3. Task Detail

- **Endpoint:** `/task-detail/<str:pk>/`
- **Method:** `GET`
- **Description:** Get details of a specific task by providing its primary key (`pk`).

### 4. Task Create

- **Endpoint:** `/task-create/`
- **Method:** `POST`
- **Description:** Create a new task by sending a POST request with task details.

### 5. Task Update

- **Endpoint:** `/task-update/<str:pk>/`
- **Method:** `PUT`
- **Description:** Update an existing task by providing its primary key (`pk`) and sending a PUT request with updated task details.

### 6. Task Delete

- **Endpoint:** `/task-delete/<str:pk>/`
- **Method:** `DELETE`
- **Description:** Delete an existing task by providing its primary key (`pk`) and sending a DELETE request.

## Technologies Used 🚧

- **Frontend:**
  - React
  - HTML
  - CSS

- **Backend:**
  - Django
  - Django REST framework

Feel free to contribute to this project by creating issues or pull requests. 🎉✨
