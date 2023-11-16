from datetime import timedelta
import time


def main():
    seconds_1 = timedelta(seconds=1)
    seconds_20 = timedelta(seconds=20*60)
    while seconds_20 != timedelta(seconds=0):
        print(seconds_20)
        time.sleep(1)
        seconds_20 = seconds_20 - seconds_1
    print('times up!')


if __name__ == '__main__':
    main()
