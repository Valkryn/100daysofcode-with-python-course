from datetime import \
    datetime  # imports use of date and time ; year,month ,day , hours , minutes, seconds , milliseconds
from datetime import date  # imports use of just date ; year , month , day
from datetime import timedelta


def main():
    print(datetime.today())
    today_ = date.today()
    print(today_.month)
    christmas = date(today_.year, 12, 25)
    print(christmas)
    time_left = christmas - today_
    print(f'There are {time_left.days} days until christmas')
    if today_ != christmas:
        print('sorry not christmas yet')
    else:
        print('Yay its christmas')
    t = timedelta(days=10, hours=14)
    print(str(t + datetime.today()))


if __name__ == '__main__':
    main()