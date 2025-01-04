from flask import Flask, render_template, request, redirect, url_for, session
from database import init_db
from view import register, login, dashboard, book_appointment, view_appointments
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.add_url_rule('/', 'index', view_func=lambda: redirect(url_for('login')))
app.add_url_rule('/register', 'register', view_func=register, methods=['GET', 'POST'])
app.add_url_rule('/login', 'login', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/dashboard', 'dashboard', view_func=dashboard)
app.add_url_rule('/book_appointment', 'book_appointment', view_func=book_appointment, methods=['GET', 'POST'])
app.add_url_rule('/view_appointments', 'view_appointments', view_func=view_appointments)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)