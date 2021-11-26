import datetime

class get_date:
    def return_date(time):
        now = datetime.datetime.utcnow() - datetime.timedelta(days=time)
        date_last = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        #print(date_last)
        return date_last
