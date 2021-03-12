from flask import render_template, request, redirect
from app import app
from app.models.event_list import events, add_new_event
from app.models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['POST'])
def create():
    event_id = len(events) + 1
    event_date = request.form['date']
    event_name = request.form['name']
    no_of_guests = request.form['no_of_guests']
    room = request.form['room']
    description = request.form['description']
    new_event = Event(event_id, event_date, event_name, no_of_guests, room, description)
    add_new_event(new_event)
    return redirect('/events')