from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, session, url_for
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def home(): 
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)
