from .app import main

app= main()

@app.route("/home")
def main():
    return "Esta es la ruta principal"
 