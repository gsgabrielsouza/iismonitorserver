from flask import Flask
from iismonitorserver import app

if __name__ == "__main__":
    app.run(debug=True)