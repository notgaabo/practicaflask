from .app import main

app= main()

@app.route("/")
def home_route():
    return 1 + 2
