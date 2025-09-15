from .app import main

app= main()

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>  This is the index page."
 