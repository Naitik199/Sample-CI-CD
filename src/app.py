from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "this time it should work"

if __name__ == "__main__":
    app.run()   