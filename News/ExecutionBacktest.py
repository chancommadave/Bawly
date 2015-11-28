import datetime as dt

if __name__ == "__main__":

    start = '9:30'
    end = '11:00'
    format = '%H:%M'

    dt_time = dt.datetime.strptime(start, format)
    dt_end = dt.datetime.strptime(end, format)

    while dt_time <= dt_end:
        print(dt_time.time())
        dt_time = dt_time + dt.timedelta(minutes=1)
