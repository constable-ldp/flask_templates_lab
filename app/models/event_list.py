from app.models.event import *
import datetime

event1 = Event(1, datetime.date(2021, 2, 22), "Judys Seminar on Cats", 15, "Room 401", "Judy talks about her numerous cats")
event2 = Event(2, datetime.date(2021, 4, 15), "Multi-level Marketing Opportunity", 3, "Room 10", "Totally legitimate business, yep")
event3 = Event(3, datetime.date(2021, 3, 2), "Gathering of the Juggalos", 75, "Room 3", "ICP Appreciation Society")

events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)
