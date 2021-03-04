from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.connect(("8.8.8.8", 80))
   myip = s.getsockname()[0]
   s.close()

   return 'Hello World from {}'.format(myip)

if __name__ == '__main__':
   app.run(host="0.0.0.0")
