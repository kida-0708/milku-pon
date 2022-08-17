import os
from flask import Flask, render_template, request, redirect, url_for 
from werkzeug.utils import secure_filename

#UPLOAD_FORDER = 'milku\static\upload'
#ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, static_url_path='/static')

app.config['DEBUG'] = True

@app.route('/')
def top():
    return render_template('top.html')

@app.route('/top/nerdbird')
def nerdbird():
    return render_template('nerdbird.html', title="Flask")

@app.route('/top/honoo')
def honoo():
    return render_template('honoo.html', title="Flask")

@app.route('/top/th')
def th():
    return render_template('th.html', title="Flask")

@app.route('/top/maruta')
def maruta():
    return render_template('maruta.html', title="Flask")

@app.route('/top/tomara')
def tomara():
    return render_template('tomara.html', title="Flask")

@app.route('/top/suitu')
def suitu():
    return render_template('suitu.html', title="Flask")

@app.route('/top/kcafe')
def kcafe():
    return render_template('kcafe.html', title="Flask")

@app.route('/top/nichiyoubi')
def nichiyoubi():
    return render_template('nichiyoubi.html', title="Flask")

@app.route('/top/banbuu')
def banbuu():
    return render_template('banbuu.html', title="Flask")

@app.route('/top/dondon')
def dondon():
    return render_template('dondon.html', title="Flask")

@app.route('/top/ishigama')
def ishigama():
    return render_template('ishigama.html', title="Flask")

@app.route('/top/felice')
def felice():
    return render_template('felice.html', title="Flask")

@app.route('/top/misudo')
def misudo():
    return render_template('misudo.html', title="Flask")

@app.route('/top/qui')
def qui():
    return render_template('qui.html', title="Flask")

@app.route('/top/thirty')
def thirty():
    return render_template('thirty.html', title="Flask")

@app.route('/top/hc')
def hc():
    return render_template('hc.html', title="Flask")

@app.route('/top/page')
def page():
    return render_template('page.html', title="Flask")

@app.route('/top/nankou')
def nankou():
    return render_template('nankou.html', title="Flask")

@app.route('/top/ttw')
def ttw():
    return render_template('ttw.html', title="Flask")

@app.route('/top/miro')
def miro():
    return render_template('miro.html', title="Flask")

@app.route('/top/cream')
def cream():
    return render_template('cream.html', title="Flask")

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()