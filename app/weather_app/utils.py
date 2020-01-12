from datetime import datetime, timedelta


#soring function in show flights
def sort_by(element):
    return element[2]


def date_time_now():
    now = datetime.now() + timedelta(hours=1)
    current_time = now.strftime("%H:%M:%S")
    return current_time
