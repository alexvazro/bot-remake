from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"


@app.route("/run")
def test_run():
    keep_alive()
    return "hello"


def run():

  app.run(port=8080)



def keep_alive():  

    t = Thread(target=run)

    t.start()

if __name__ == "__main__":
    app.run()

