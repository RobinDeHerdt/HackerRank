from Testing import assertions
import datetime
import calendar
import operator

# https://stackoverflow.com/questions/33673116/eval-with-a-variable-operator
# since we need to do inverse operations, add this (confusing) operator map.
operator_map = {
    "-": operator.add,
    "+": operator.sub
}


def time_delta(t1, t2):
    return abs(get_timestamp(t1) - get_timestamp(t2))


def get_timestamp(datetime_string):
    date = datetime.datetime.strptime(datetime_string, '%a %d %b %Y %H:%M:%S %z')
    return int(date.timestamp())


def time_delta_get_timestamp_without_format(t1, t2):
    return abs(get_timestamp_without_format(t1) - get_timestamp_without_format(t2))


# Some string formatting / time diff exercise.
def get_timestamp_without_format(datetime_string):

    day_name, day_number, month, year, time, time_diff = datetime_string.split()

    month_names = list(calendar.month_name)
    month_number = month_names.index(month)
    hours, minutes, seconds = map(int, time.split(":"))

    date = datetime.datetime(int(year), int(month_number), int(day_number), hours, minutes, seconds, 0, tzinfo=datetime.timezone.utc)

    time_diff_operator = time_diff[:1]
    time_diff_hours = int(time_diff[1:3])
    time_diff_minutes = int(time_diff[3:5])

    hours_diff = datetime.timedelta(hours=time_diff_hours)
    minutes_diff = datetime.timedelta(minutes=time_diff_minutes)

    date = operator_map.get(time_diff_operator)(date, hours_diff)
    date = operator_map.get(time_diff_operator)(date, minutes_diff)

    return int(date.timestamp())


assertions.assert_equals(25200, time_delta("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"))
assertions.assert_equals(88200, time_delta("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"))

assertions.assert_equals(25200, time_delta_get_timestamp_without_format("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"))
assertions.assert_equals(88200, time_delta_get_timestamp_without_format("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"))