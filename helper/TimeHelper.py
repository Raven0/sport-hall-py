from datetime import date
from datetime import datetime


class TimeHelper:
    @staticmethod
    def returnDateNow():
        return date.today().strftime("%m/%d/%Y")

    @staticmethod
    def returnTimeNow():
        return datetime.now().strftime("%H:%M")
