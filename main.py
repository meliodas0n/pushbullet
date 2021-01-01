from pushbullet import Pushbullet

PB_API_KEY = 'o.hqwwAkrFglblWfL0Q4slIyRCLtZ50cea'

print("creating pb object with key: ")

try:
    pb = Pushbullet(PB_API_KEY)
except Exception as e:
    print(str(e))
    exit()

print("pushing note: ")

try:
    push = pb.push_note('important subject', 'this is a test')
except Exception as e:
    print(str(e))
    exit()

print("done")
