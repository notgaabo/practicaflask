from .app import main

app= main()

@app.route("/")
def home_route():
    return 1 + 2

@app.route("/home")
def main():
    return "Esta es la ruta principal"
 

