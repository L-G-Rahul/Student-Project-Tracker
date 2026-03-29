import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# 1. INITIALIZE FLASK APP
app = Flask(__name__)
app.secret_key = "flask_exam_secure_key_2024"

# 2. DATABASE CONFIGURATION (SQLite)
# This creates project_db.sqlite in your project folder
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'project_db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# 3. DATABASE MODEL (The 'Table' structure)
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    student_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250))
    status = db.Column(db.String(20), default='In Progress')  # In Progress or Completed

    def __repr__(self):
        return f'<Project {self.name}>'


# Create the database file and tables automatically
with app.app_context():
    db.create_all()


# 4. ROUTES (The Logic)

@app.route('/')
def index():
    """FETCH ALL DATA (READ)"""
    all_projects = Project.query.all()
    return render_template('index.html', projects=all_projects)


@app.route('/add', methods=['POST'])
def add_project():
    """INSERT DATA (CREATE)"""
    name = request.form.get('name')
    s_name = request.form.get('student_name')
    desc = request.form.get('description')

    if name and s_name:
        new_project = Project(name=name, student_name=s_name, description=desc)
        db.session.add(new_project)
        db.session.commit()
        flash("Project added to database successfully!", "success")
    else:
        flash("Project Name and Student Name are required!", "error")

    return redirect(url_for('index'))


@app.route('/update/<int:id>')
def update_status(id):
    """UPDATE DATA (UPDATE)"""
    project = Project.query.get_or_404(id)
    # Toggle status
    project.status = 'Completed' if project.status == 'In Progress' else 'In Progress'
    db.session.commit()
    flash(f"Status updated for {project.name}", "info")
    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete_project(id):
    """DELETE DATA (DELETE)"""
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    flash("Project deleted from records.", "warning")
    return redirect(url_for('index'))


# 5. UI (HTML Template)
index_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Project Tracker</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body class="bg-slate-50 min-h-screen font-sans">

    <div class="max-w-4xl mx-auto py-12 px-6">
        <header class="mb-10 text-center">
            <h1 class="text-4xl font-extrabold text-slate-800 tracking-tight">Student Project Tracker</h1>
            <p class="text-slate-500 mt-2 font-medium">Flask & SQLite Database Connectivity Demo</p>
        </header>

        <!-- Notification Area -->
        {% with messages = get_flashed_messages(with_categories=true) %}
          {% if messages %}
            {% for category, message in messages %}
              <div class="mb-6 p-4 rounded-xl border {% if category == 'success' %}bg-emerald-50 border-emerald-200 text-emerald-700{% elif category == 'error' %}bg-rose-50 border-rose-200 text-rose-700{% else %}bg-sky-50 border-sky-200 text-sky-700{% endif %} shadow-sm flex items-center">
                <i class="fas fa-info-circle mr-3"></i>
                {{ message }}
              </div>
            {% endfor %}
          {% endif %}
        {% endwith %}

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">

            <!-- Sidebar: Add Project Form -->
            <div class="md:col-span-1">
                <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 sticky top-6">
                    <h2 class="text-lg font-bold text-slate-800 mb-4 border-b pb-2">Register Project</h2>
                    <form action="/add" method="POST" class="space-y-4">
                        <div>
                            <label class="block text-xs font-bold text-slate-500 uppercase tracking-wider mb-1">Project Title</label>
                            <input type="text" name="name" placeholder="e.g. Library System" required 
                                class="w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-500 uppercase tracking-wider mb-1">Student Name</label>
                            <input type="text" name="student_name" placeholder="Full Name" required 
                                class="w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-500 uppercase tracking-wider mb-1">Description</label>
                            <textarea name="description" rows="3" placeholder="Brief overview..." 
                                class="w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition text-sm"></textarea>
                        </div>
                        <button type="submit" class="w-full bg-indigo-600 text-white py-2.5 rounded-lg font-bold hover:bg-indigo-700 transform active:scale-95 transition shadow-md shadow-indigo-200">
                            Save to Database
                        </button>
                    </form>
                </div>
            </div>

            <!-- Main Content: Project List -->
            <div class="md:col-span-2 space-y-4">
                <div class="flex items-center justify-between px-2">
                    <h2 class="text-xl font-bold text-slate-800">Existing Records</h2>
                    <span class="bg-slate-200 text-slate-600 text-xs font-bold px-2.5 py-1 rounded-full">{{ projects|length }} Total</span>
                </div>

                {% if projects %}
                    {% for p in projects %}
                    <div class="bg-white p-5 rounded-2xl shadow-sm border border-slate-200 hover:border-indigo-300 transition group">
                        <div class="flex justify-between items-start">
                            <div class="flex-1">
                                <div class="flex items-center space-x-2">
                                    <h3 class="font-bold text-slate-800 text-lg">{{ p.name }}</h3>
                                    <span class="px-2 py-0.5 text-[10px] font-bold uppercase rounded-md {{ 'bg-emerald-100 text-emerald-700' if p.status == 'Completed' else 'bg-amber-100 text-amber-700' }}">
                                        {{ p.status }}
                                    </span>
                                </div>
                                <p class="text-indigo-600 text-sm font-semibold mb-2"><i class="far fa-user mr-1"></i> {{ p.student_name }}</p>
                                <p class="text-slate-500 text-sm leading-relaxed">{{ p.description }}</p>
                            </div>
                            <div class="flex flex-col space-y-2 ml-4">
                                <a href="/update/{{ p.id }}" class="p-2 bg-slate-50 text-slate-400 hover:text-indigo-600 hover:bg-indigo-50 rounded-xl transition border border-transparent hover:border-indigo-100" title="Toggle Status">
                                    <i class="fas fa-sync-alt"></i>
                                </a>
                                <a href="/delete/{{ p.id }}" class="p-2 bg-slate-50 text-slate-400 hover:text-rose-600 hover:bg-rose-50 rounded-xl transition border border-transparent hover:border-rose-100" title="Remove Record">
                                    <i class="fas fa-trash-alt"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                {% else %}
                    <div class="bg-white border-2 border-dashed border-slate-200 rounded-3xl p-12 text-center">
                        <div class="bg-slate-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4 text-slate-400">
                            <i class="fas fa-folder-open text-2xl"></i>
                        </div>
                        <p class="text-slate-400 font-medium">No projects found in the database.</p>
                        <p class="text-slate-300 text-sm">Register a project using the form on the left.</p>
                    </div>
                {% endif %}
            </div>
        </div>

        <footer class="mt-20 text-center border-t border-slate-200 pt-8">
            <p class="text-slate-400 text-sm">Python Practical Exam &copy; 2024</p>
        </footer>
    </div>

</body>
</html>
"""

from jinja2 import DictLoader

app.jinja_loader = DictLoader({'index.html': index_html})

if __name__ == '__main__':
    app.run(debug=True)
