from flask import Flask
from threading import Thread
import d_bot


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"


@app.route("/run")
def run():
    app.run()



def keep_alive():  

    t = Thread(target=run)

    t.start()
    print("keepalive end")



app.run()
keep_alive()
