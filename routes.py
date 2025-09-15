from .app import main

app= main()

@app.route("/")
def home():
    return "Hello world"
 