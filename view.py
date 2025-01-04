from flask import render_template, request, redirect, url_for, session
from database import db_session
from models import User, Appointment
from datetime import datetime

def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # hashed_password = bcrypt.generate_password_hash(password)
        user = User(username=username, password=password)
        db_session.add(user)
        db_session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else :
            return redirect(url_for('register'))
    return render_template('login.html')

def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

def book_appointment():
    if request.method == 'POST':
        doctor_id = request.form['doctor_id']
        # appointment_time = request.form['appointment_time']
        appointment_time = datetime.fromisoformat(request.form['appointment_time'])
        # appointment = Appointment(user_id=session['user_id'], doctor_id=doctor_id, appointment_time=appointment_time)
        appointment = Appointment(user_id=session['user_id'], doctor_id=doctor_id, appointment_time=appointment_time)
        db_session.add(appointment)
        db_session.commit()
        return redirect(url_for('dashboard'))
    return render_template('book_appointment.html')

def view_appointments():
    appointments = Appointment.query.filter_by(user_id=session['user_id']).all()
    return render_template('view_appointment.html', appointments=appointments)