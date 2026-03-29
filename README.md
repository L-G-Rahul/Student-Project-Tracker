🎓 ### Student Project Tracker 🚀

Welcome to the Student Project Tracker! This is a sleek, lightweight web application built with Python Flask and SQLite to help students manage their academic projects efficiently. 📝✨

🌟 Features

🆕 Create: Add new projects with student names and descriptions.

📑 Read: View a beautiful, real-time list of all registered projects.

🔄 Update: Toggle project status between In Progress and Completed with one click.

🗑️ Delete: Remove old or incorrect entries instantly.

🎨 Modern UI: Built with Tailwind CSS for a clean, responsive, and professional look.

💾 Database: Powered by SQLite for reliable data persistence.

🛠️ Tech Stack

Component

Technology

Backend

Python 🐍

Framework

Flask 🔥

Database

SQLite 🗄️

ORM

SQLAlchemy 🏗️

Styling

Tailwind CSS 🖌️

🚀 Getting Started

Follow these steps to get your project running locally! 💻

1️⃣ Clone the Repository

git clone [https://github.com/your-username/student-project-tracker.git](https://github.com/your-username/student-project-tracker.git)
cd student-project-tracker


2️⃣ Install Dependencies

Make sure you have Python installed, then run:

pip install flask flask-sqlalchemy


3️⃣ Run the Application

python app.py


4️⃣ Open in Browser

Visit the following URL in your favorite browser:
👉 http://127.0.0.1:5000

📁 Project Structure

.
├── app.py              # 🧠 Main Flask Application & Logic
├── project_db.sqlite   # 🗄️ Database File (Generated automatically)
└── README.md           # 📖 This file!


💡 How It Works (The "Deep Dive")

The Brain (Flask): Manages all web routes and user requests.

The Translator (SQLAlchemy): Maps Python classes to database tables so we don't have to write raw SQL.

The Vault (SQLite): Stores all your project data safely in a local file.


Distributed under the MIT License. See LICENSE for more information. 📄

Made with ❤️ and Python 🐍
