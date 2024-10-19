import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import urlparse

app = Flask(__name__)

    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        feedback = request.form['feedback']
        
        # Store feedback in the global list
        
        # After saving feedback, redirect the user to the home page
        return redirect(url_for('home'))
    
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug=True)
