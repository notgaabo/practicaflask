from .app import main

app= main()

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>  This is the index page."

@app.route("/index")
def home_route():
    return 1 + 2

@app.route("/home")
def main():
    return "Esta es la ruta principal"
 

