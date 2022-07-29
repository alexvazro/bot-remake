from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def index():
    import d_bot
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

if __name__ == "__main__":
    app.run()

