from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    student_name = "Karuna"

    user_data = {
        'name': 'Karuna Divekar',
        'age': 22,
        'course': 'Web Development',
        'email': 'karunadivek20@gmail.com',
        'city': 'Pune',
        'is_enrolled': True
    }

    programming_skills = ['Python', 'HTML', 'CSS', 'JavaScript', 'Flask']

    project_list = [
        {'name': 'Personal Website', 'status': 'Completed', 'tech': 'HTML/CSS'},
        {'name': 'Flask Blog', 'status': 'In Progress', 'tech': 'Python/Flask'},
        {'name': 'Weather Telegram_bot App', 'status': 'completed', 'tech': 'JavaScript'},
    ]

    grades_data = {
        'Mathematics': 'A',
        'Python': 'A+',
        'Web Development': 'A',
        'Data Structures': 'B+'
    }

    return render_template(
        'index.html',
        name=student_name,
        user=user_data,
        skills=programming_skills,
        projects=project_list,
        grades=grades_data
    )

if __name__ == '__main__':
    app.run(debug=True)
