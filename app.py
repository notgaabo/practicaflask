from flask import Flask

#AQUI CREAMOS RUTAS

def main():
    app=Flask(__name__)

    return app

if __name__ =="__main__":
    app = main()
    app.run()