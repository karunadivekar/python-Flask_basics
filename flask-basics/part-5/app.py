"""
Part 5: Mini Project - Personal Website with Flask
=================================================
A complete personal website using everything learned in Parts 1-4.

How to Run:
1. Activate virtual environment
2. Run: python app.py
3. Open browser: http://127.0.0.1:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# PERSONAL INFORMATION
# =============================================================================

PERSONAL_INFO = {
    'name': 'Karuna Divekar',
    'title': 'Web Developer',
    'bio': 'A passionate developer learning Flask and web development.',
    'email': 'karunadivekar20@gmail.com',
    'github': 'https://github.com/karunadivekar',
    'linkedin': 'https://linkedin.com/in/karuna-divekar',
}

# =============================================================================
# SKILLS
# =============================================================================

SKILLS = [
    {'name': 'Python', 'level': 80, 'slug': 'python'},
    {'name': 'HTML / CSS', 'level': 75, 'slug': 'html-css'},
    {'name': 'Flask', 'level': 60, 'slug': 'flask'},
    {'name': 'JavaScript', 'level': 50, 'slug': 'javascript'},
    {'name': 'DBMS', 'level': 80, 'slug': 'dbms'},
]

# =============================================================================
# PROJECTS
# =============================================================================

PROJECTS = [
    {
        'id': 1,
        'name': 'Personal Website',
        'description': 'A Flask-powered personal portfolio website.',
        'tech': ['Python', 'Flask', 'HTML', 'CSS'],
        'status': 'Completed'
    },
    {
        'id': 2,
        'name': 'Weather Telegram Bot',
        'description': (
            'A Python-based Telegram bot that provides real-time weather '
            'information using external APIs.'
        ),
        'tech': ['Python', 'python-telegram-bot', 'APIs', 'SQLite'],
        'status': 'Completed'
    },
    {
        'id': 3,
        'name': 'Pet Well Connect',
        'description': (
            'Pet Well Connect is a digital platform that provides essential '
            'information related to pet care, health tips, and awareness.'
        ),
        'tech': [
            'Python',
            'Flask',
            'Flask-Login',
            'MySQL',
            'OpenCV',
            'Tesseract OCR',
            'Pillow',
            'NumPy',
            'ReportLab'
        ],
        'features': [
            'Pet profile management',
            'Health and wellness tracking',
            'Vaccination and check-up reminders',
            'Diet and nutrition guidance',
            'Pet care tips and information'
        ],
        'status': 'Completed'
    }
]

# =============================================================================
# BLOG POSTS
# =============================================================================

BLOG_POSTS = [
    {
        'id': 1,
        'title': 'My Flask Learning Journey',
        'date': '2025-01-05',
        'content': (
            'I started learning Flask to understand backend web development. '
            'It helped me learn routing, templates, and dynamic URLs.'
        )
    },
    {
        'id': 2,
        'title': 'Building a Telegram Bot with Python',
        'date': '2025-01-10',
        'content': (
            'I built a Daily Inspiration Bot using python-telegram-bot. '
            'The bot sends daily quotes and supports user settings.'
        )
    },
    {
        'id': 3,
        'title': 'OCR and Image Processing with Python',
        'date': '2025-01-15',
        'content': (
            'Using OpenCV and Tesseract OCR, I learned how to extract text '
            'from images and generate PDF reports.'
        )
    }
]

# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


# ✅ FIX: Allow /about AND /about/
@app.route('/about')
@app.route('/about/')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in PROJECTS if p['id'] == project_id), None)
    return render_template(
        'project_detail.html',
        info=PERSONAL_INFO,
        project=project
    )


@app.route('/blog')
def blog():
    return render_template(
        'blog.html',
        info=PERSONAL_INFO,
        posts=BLOG_POSTS
    )


@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)


@app.route('/skill/<slug>')
def skill_projects(slug):
    filtered_projects = [
        project for project in PROJECTS
        if any(
            slug.replace('-', '').lower() in tech.replace('/', '').lower()
            for tech in project['tech']
        )
    ]

    skill_name = slug.replace('-', ' / ').upper()

    return render_template(
        'skills.html',
        info=PERSONAL_INFO,
        skill_name=skill_name,
        projects=filtered_projects
    )

# =============================================================================
# RUN APP
# =============================================================================

if __name__ == '__main__':
    app.run(debug=True)



# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 5.1: Personalize your website
#   - Update PERSONAL_INFO with your real information
#   - Add your actual skills and projects
#
# Exercise 5.2: Add a new page
#   - Create a /blog route
#   - Add blog posts data structure
#   - Create blog.html template
#
# Exercise 5.3: Enhance the styling
#   - Modify static/style.css
#   - Add your own color scheme
#   - Make it responsive for mobile
#
# Exercise 5.4: Add more dynamic features
#   - Create a /skill/<skill_name> route
#   - Show projects that use that skill
#
# =============================================================================