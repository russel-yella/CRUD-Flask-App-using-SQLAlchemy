# Library Management Web App

A simple CRUD web application built with Flask and SQLAlchemy for managing a personal book library.

Users can:

* Add books
* Edit books
* Delete books
* View all books

The project uses server-rendered HTML templates with Jinja.

---

# Features

* Add new books
* Edit existing books
* Delete books
* SQLite database integration
* Flask templating with Jinja
* Modern SQLAlchemy 2.0 ORM syntax

---

# Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* SQLAlchemy 2.0
* SQLite
* HTML
* Jinja2

---

# Project Structure

```text id="v9x6t7"
project/
│
├── templates/
│   ├── index.html
│   ├── add.html
│   └── edit.html
│
├── main.py
├── books.db
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone the repository

```bash id="lhg7hg"
git clone https://github.com/your-username/library-management-app.git
```

---

## 2. Navigate into the project

```bash id="fh4m42"
cd library-management-app
```

---

## 3. Create virtual environment

### Windows

```bash id="ddvn4m"
python -m venv .venv
```

---

## 4. Activate virtual environment

### Windows

```bash id="vww6rn"
.venv\Scripts\activate
```

---

## 5. Install dependencies

```bash id="5d5n32"
pip install -r requirements.txt
```

---

# Run the Application

```bash id="lmqmmj"
python main.py
```

The application will start on:

```text id="x0cxbb"
http://127.0.0.1:5000
```

---

# Application Routes

| Route          | Description    |
| -------------- | -------------- |
| `/`            | View all books |
| `/add`         | Add a new book |
| `/edit/<id>`   | Edit a book    |
| `/delete/<id>` | Delete a book  |

---

# Database

The project uses SQLite.

Database file:

```text id="mbnh5s"
books.db
```

Tables are automatically created using SQLAlchemy.

---

# Example Features

## Add Book

Users can add:

* title
* author
* rating

---

## Edit Book

Users can update:

* title
* author
* rating

---

## Delete Book

Books can be permanently removed from the database.

---

# Technologies Used

## Flask

Used to handle:

* routing
* templates
* HTTP requests

---

## Flask-SQLAlchemy

Used for ORM database management.

---

## Jinja2

Used for dynamic HTML rendering.

Example:

```html id="c6t2dp"
{{ book.title }}
```

---

# Future Improvements

* Bootstrap styling
* User authentication
* Search functionality
* Pagination
* API version
* PostgreSQL support

---

