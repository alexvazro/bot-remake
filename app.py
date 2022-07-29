from flask import Flask
from threading import Thread
import d_bot

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"


@app.route("/reset")
#TODO: this function resets the bot: TO DO
def test():
    import d_bot
    keep_alive()

def run():

  app.run(port=8080)



def keep_alive():  

    t = Thread(target=run)

    t.start()
    print("keepalive end")

if __name__ == "__app__":
    app.run()

keep_alive()

