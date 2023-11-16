from datetime import timedelta
import time


def main():
    while True:
        try:
            user_input = int(input('How many minutes to focus for?: '))
            break
        except ValueError:
            print('please input a number')
    seconds_1 = timedelta(seconds=1)
    study_time = timedelta(seconds=user_input * 60)
    pomodoro(study_time, seconds_1)


def pomodoro(study_time, seconds_1):
    while study_time != timedelta(seconds=0):
        print(study_time)
        time.sleep(1)
        study_time = study_time - seconds_1
    print('times up!')


if __name__ == '__main__':
    main()

#add break cycle