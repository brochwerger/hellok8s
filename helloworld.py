from flask import Flask
import socket
import time
import random
import os
import redis

app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = 'Hello World\n'  # 1.0

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    myip = s.getsockname()[0]
    myname = socket.gethostbyaddr(socket.gethostname())[0]
    s.close()

    naptime = random.uniform(100, 500) / 1000
    time.sleep(naptime)

    #   greeting = 'Hello World\n' # 1.0
    #   greeting = 'Hello World from {}.\n'.format(myname) # 1.1
    #   greeting = 'Hello World from {} ({}).\n'.format(myname, myip) # 1.2

    greeting = 'Hello {} from {} ({}).\n'.format(os.environ.get("NAME", "You"), myname, myip)  # >= 1.3

    # 1.4
    db = redis.Redis(host=os.environ.get('BE_HOST', 'localhost'))
    counter_key = os.environ.get('COUNTER', "Counter")
    visits = db.get(counter_key)
    if visits == None:
        visits = 1
    else:
        visits = int(visits) + 1

    db.set(counter_key, visits)
    # greeting = greeting + 'You are visitor number {}\n'.format(visits)
    greeting = 'Hello visitor #{} from {}.\n'.format(visits, myip)

    return greeting


if __name__ == '__main__':
    app.run(host="0.0.0.0")
