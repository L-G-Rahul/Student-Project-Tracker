# 🚀 Student Project Tracker 📊

A simple yet powerful **Flask + SQLite** web application to manage student projects with full CRUD functionality.

---

## 📌 Features

✨ Add new student projects  
📖 View all stored projects  
🔄 Update project status (In Progress ↔ Completed)  
❌ Delete projects  
💾 Persistent database using SQLite  
🎨 Clean UI with Tailwind CSS  

---

## 🛠️ Tech Stack

- 🐍 Python (Flask)
- 🗄️ SQLite Database
- 🎨 Tailwind CSS
- ⚡ HTML (Jinja2 Templates)

---

## 📂 Project Structure

```
📁 project-folder
│── app.py              # Main Flask application
│── project_db.sqlite   # Database (auto-created)
│── templates/
│    └── index.html     # Frontend UI
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/student-project-tracker.git
cd student-project-tracker
```

### 2️⃣ Install Dependencies
```bash
pip install flask flask_sqlalchemy
```

### 3️⃣ Run the Application
```bash
python app.py
```

### 4️⃣ Open in Browser 🌐
```
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

- 🧾 Projects are stored in a SQLite database  
- ➕ Form allows adding new entries  
- 🔁 Status toggle updates progress  
- ❌ Delete removes records permanently  
- 💡 Flash messages provide user feedback  

---

## 🗃️ Database Model

```python
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    student_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250))
    status = db.Column(db.String(20), default='In Progress')
```

---

## 🔥 Key Routes

| Route | Method | Description |
|------|--------|------------|
| `/` | GET | Display all projects |
| `/add` | POST | Add new project |
| `/update/<id>` | GET | Toggle status |
| `/delete/<id>` | GET | Delete project |

---

## 🖼️ UI Highlights

🎯 Responsive layout  
📌 Sidebar form for quick input  
📋 Project cards with status tags  
⚡ Smooth hover & transition effects  

---

## ⚠️ Notes

- Database is created automatically on first run  
- Requires Python 3.x  
- Debug mode is enabled (disable for production)

---

## 🏁 Future Improvements

🚀 User authentication system  
📊 Dashboard analytics  
🔍 Search & filter functionality  
🌐 Deploy to cloud (Render/Heroku)  

---

## 👨‍💻 Author
 L.G.Rahul

Built for learning Flask + Database integration 💡  
