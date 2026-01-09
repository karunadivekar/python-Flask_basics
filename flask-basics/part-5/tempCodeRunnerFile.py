from flask import Flask, render_template

app = Flask(__name__)

# ===================== PERSONAL INFO =====================
PERSONAL_INFO = {
    'name': 'Karuna Divekar',
    'title': 'Web Developer',
    'bio': 'Hi! I am Karuna Divekar from Burhanpur, currently pursuing MSc (IMSA) from Nowrosjee Wadia College. '
           'I am passionate about learning Flask, web development, and building useful projects.',
    'email': 'karunadivekar@example.com',
    'github': 'https://github.com/karunadivekar',
    'linkedin': 'https://linkedin.com/in/karunadivekar'
}

# ===================== SKILLS =====================
SKILLS = [
    {'name': 'Python', 'level': 80},
    {'name': 'HTML/CSS', 'level': 75},
    {'name': 'Flask', 'level': 60},
    {'name': 'JavaScript', 'level': 50},
    {'name': 'SQL', 'level': 45},
]

# ===================== PROJECTS =====================
PROJECTS = [
    {'id': 1, 'name': 'Personal Website', 'description': 'A Flask-powered personal portfolio website.',
     'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'Todo App', 'description': 'A simple task management application.',
     'tech': ['Python', 'Flask', 'SQLite'], 'status': 'In Progress'},
    {'id': 3, 'name': 'Weather Dashboard', 'description': 'Display weather data from an API.',
     'tech': ['Python', 'Flask', 'API'], 'status': 'Planned'},
]

# ===================== ROUTES =====================

# Home Page
@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)

# About Page
@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)

# Projects Page
@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)

# Individual Project Page
@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in PROJECTS if p['id'] == project_id), None)
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)

# ===================== RUN SERVER =====================
if __name__ == '__main__':
    app.run(debug=True)
