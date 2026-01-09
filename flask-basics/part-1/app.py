"""
Part 1: Hello Flask - Your First Web Server
============================================
How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask

app = Flask(__name__)


# Exercise 1.1 + 1.2
# Home route with name and HTML
@app.route('/')
def home():
    return "<h1>Hello Karuna!</h1><p>Welcome to my first Flask web server.</p>"


# Exercise 1.3
# About page route
@app.route('/about')
def about():
    return "<h2>About Page</h2><p>This is the about page of my Flask app.</p>"


if __name__ == '__main__':
    app.run(debug=True)
