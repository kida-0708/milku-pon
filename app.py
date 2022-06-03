import os
from flask import Flask, render_template, request, redirect, url_for 
from werkzeug.utils import secure_filename

#UPLOAD_FORDER = 'milku\static\upload'
#ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, static_url_path='/static')

app.config['DEBUG'] = True

@app.route('/')
def emp():
    return render_template('emp.html', title="Flask")

if __name__ == '__main__':
    app.run(debug=True)