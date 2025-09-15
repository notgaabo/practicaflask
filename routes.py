from .app import main

app= main()

@app.route("/")
def angel():
    return "angel"
