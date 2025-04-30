from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.routing import Map, Rule

app = Flask(__name__)

app.secret_key = '1e49cf78608b6fe644cf5d3fa80c387a13d0235de30ed58d693881f496c27'  
USER_CREDS = {"username": "Drajat", "password": "secret"}  

url_map = Map((
    Rule('/', endpoint='index'),
    Rule('/user/<name>', endpoint='user'),
    Rule('/mahasiswa/<npm>', endpoint='mahasiswa'),
    Rule('/login', endpoint='login', methods=['GET', 'POST']),
    Rule('/admin', endpoint='admin'),
    Rule('/logout', endpoint='logout')
))


@app.endpoint('index')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html', title='index', username=username)
    else:
        return render_template('index.html', title='index')

@app.endpoint('user')
def user(name):
    header = f'<h1>Hello, {name}!</h1>'
    instruct = '<p>Change the name in the <em>browser address bar</em> and reload the page.</p>'
    return header + instruct


data_mahasiswa = {
    "50424346": "Drajat wibowo"
}

@app.endpoint('mahasiswa')
def mahasiswa(npm):
    if npm in data_mahasiswa:
        nama = data_mahasiswa[npm]
        header = f'<h1>Halo, {nama}</h1>'
        return header
    else:
        return 'Mahasiswa not found!'

@app.endpoint('login')
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USER_CREDS['username'] and password == USER_CREDS['password']:
            session['username'] = username
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', title='login', failed=True, username=username)
    else:
        return render_template('login.html', title='login')


@app.endpoint('admin')
def admin():
    if 'username' in session:
        username = session['username']
        return render_template('admin.html', title='admin', username=username)
    return redirect(url_for('login'))

@app.endpoint('logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

app.url_map = url_map

if __name__ == '__main__':
    app.run(debug=True)