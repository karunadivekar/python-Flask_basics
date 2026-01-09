from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ---------------- SAMPLE DATA ----------------
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]

# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template('index.html', tasks=TASKS)

# ---------------- ADD TASK ----------------
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        new_id = len(TASKS) + 1
        title = request.form['title']
        status = request.form['status']
        priority = request.form['priority']

        TASKS.append({
            'id': new_id,
            'title': title,
            'status': status,
            'priority': priority
        })

        return redirect(url_for('home'))

    return render_template('add.html')

# ---------------- SINGLE TASK ----------------
@app.route('/task/<int:id>')
def task_detail(id):
    task = None
    for t in TASKS:
        if t['id'] == id:
            task = t
            break
    return render_template('task.html', task=task)

# ---------------- ABOUT ----------------
@app.route('/about/')
@app.route('/about')
def about():
    return render_template('about.html')

# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True, port=5001)
