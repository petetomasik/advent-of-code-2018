#!/usr/bin/env python

import json
import re
from datetime import datetime,timedelta

with open("inputs") as f:
    lines = list(f)

inputs = [x.strip() for x in lines]
inputs = sorted(inputs)

#get all guard IDs
sleep_activity = {}
for activity in inputs:
    guard_id = re.findall(r'\[.+\] Guard #(\d+) ',activity)
    if guard_id:
        sleep_activity[guard_id[0]] = {}

#initialize minute 00..59 for all guard IDs
for guard in sleep_activity:
    for i in range(0,60):
        sleep_activity[guard][i] = 0

#generate guard sleep routines
time_fmt = '%Y-%m-%d %H:%M'
for activity in inputs:
    guard_id = re.findall(r'\[.+\] Guard #(\d+) ',activity)
    asleep = re.findall(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] falls asleep',activity)
    awake = re.findall(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] wakes up',activity)
    if guard_id:
        guard_on_duty = guard_id[0]
    if asleep:
        sleep_start = datetime.strptime(asleep[0],time_fmt)
    if awake:
        sleep_end = datetime.strptime(awake[0],time_fmt)
        minutes_asleep = sleep_end-sleep_start
        for i in range(int(sleep_start.minute),int(sleep_end.minute)):
            sleep_activity[guard_on_duty][i] += 1

#find the minute a guard was asleep the most
sleepiest_minute = [0,0]
sleepiest_guard = 0
for guard_id in sleep_activity:
    for minute_activity in sleep_activity[str(guard_id)]:
        if sleep_activity[str(guard_id)][minute_activity] > sleepiest_minute[1]:
            sleepiest_minute = [int(minute_activity),int(sleep_activity[str(guard_id)][minute_activity])]
            sleepiest_guard = guard_id

print("Guard %s was asleep during minute %s a total of %s times!!" % (sleepiest_guard,sleepiest_minute[0],sleepiest_minute[1]))
print("%s * %s = %s" % (sleepiest_guard,sleepiest_minute[0],(int(sleepiest_guard)*int(sleepiest_minute[0]))))
