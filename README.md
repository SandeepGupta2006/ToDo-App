# ✅ Flask ToDo App

A simple and session-based ToDo web app built with Flask and SQLAlchemy.  
Each user gets their own task list stored in a database using a unique session ID (no login required).

---

## 🧩 Features

- 📝 Add, update, complete, and delete tasks
- 📋 Tasks stored per user (via Flask session)
- 🧠 Uses SQLAlchemy ORM for database operations
- 🗃️ Persistent data via SQLite (or any SQL DB)
- 🌐 Clean HTML + CSS frontend with Jinja templating
- 🔒 Secure secret key and DB URI managed via `.env`

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Database**: SQLite (by default)
- **Frontend**: HTML, CSS (Jinja templates)
- **Environment Management**: `python-dotenv`

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/SandeepGupta2006/ToDo-App.git
cd ToDo-App

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your .env file
# Create a .env file in the project root with the following:
SECRET_KEY=your_secret_key_here
db_uri=sqlite:///todo.db  # or your preferred database URI

# 5. Run the app
python app.py
```

---

## 🔐 Privacy Note
No login or personal information is collected. Each session gets a unique task list, and data is isolated per session ID.
The app does not use any third-party tracking or external APIs.

---

## 🙋‍♂️ Author

**Sandeep Gupta**

[Portfolio](https://sandeepgupta2006.github.io/) • [GitHub](https://github.com/SandeepGupta2006/) • [LinkedIn](https://www.linkedin.com/in/sandeep-gupta-5872b4315/)
