from pushbullet import Pushbullet
import datetime
import multiprocessing as mp
import time
import sys
import signal
import os

PB_API_KEY = 'o.hqwwAkrFglblWfL0Q4slIyRCLtZ50cea'
pb = Pushbullet(PB_API_KEY)

def process(hr, minute):
    while True:
        d = datetime.datetime.now()
        if d.hour == hr and d.minute == minute:
            push = pb.push_note("this a test", "this is a test with specific time")
            os.kill(os.getppid(), signal.SIGTERM)
            sys.exit()
        else:
            time.sleep(1)

if __name__ == '__main__':
    p = mp.Process(target = process, args = (1, 14))
    p.start()
