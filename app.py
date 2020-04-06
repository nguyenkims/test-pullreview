from flask import Flask

app = Flask("hey")

@app.route("/")
def index():
	return "hey hey"

if __name__ == "__main__":
	app.run(host="0.0.0.0")