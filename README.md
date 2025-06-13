
# 🗓️ Event Scheduler – Django Project

Event Scheduler is a web-based application built using **Django** and **Django REST Framework** that allows users to create, update, and manage events or appointments efficiently. This project is a backend-focused implementation, offering RESTful API endpoints for event scheduling and management.

---

## 🚀 Features

- Create new events with title, date, and description
- Update or delete scheduled events
- Retrieve a list of all events via API
- REST API built using Django REST Framework
- Simple and modular structure for easy extension

---

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (default database)

---

## 📁 Project Structure

```
event_scheduler/
├── events/              # App handling events
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
├── event_scheduler/     # Project config
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3
├── manage.py
```

---

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/event-scheduler-django.git
   cd event-scheduler-django
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the server**
   ```bash
   python manage.py runserver
   ```

---

## 📡 API Endpoints (Sample)

| Method | Endpoint           | Description         |
|--------|--------------------|---------------------|
| GET    | `/api/events/`     | List all events     |
| POST   | `/api/events/`     | Create a new event  |
| PUT    | `/api/events/<id>/`| Update an event     |
| DELETE | `/api/events/<id>/`| Delete an event     |

---
