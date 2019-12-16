class Field:
    name = "field"
    attr = ['name']


class Member:
    name = "member"
    attr = ['name']


class Fees:
    name = "fees"
    attr = ['rate']


class Schedule:
    name = "schedule"
    attr = ['date']


class Session:
    name = "session"
    attr = ['time']


class Booking:
    name = "booking"
    attr = ['field_id', 'schedule_id', 'session_id', 'user_id', 'booking_time']