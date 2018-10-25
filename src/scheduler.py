"""
Demonstrates how to use the blocking scheduler to schedule a job that executes on 3 second
intervals.
"""

from datetime import datetime
import os
import requests

from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    print('Tick! The time is: %s' % datetime.utcnow())

def tick2():
    print('Tick2! The time is: %s' % datetime.utcnow())

def access_baidu():
    url = 'https://www.baidu.com'
    resp = requests.get(url)
    print(f"{datetime.utcnow()} - {url} - {resp.status_code}")


if __name__ == '__main__':
    scheduler = BlockingScheduler({
        'apscheduler.timezone': 'UTC'
    })
    scheduler.add_job(tick, 'cron', second='*')
    scheduler.add_job(tick2, 'cron', second='*/2')

    print('Scheduler starts. Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
