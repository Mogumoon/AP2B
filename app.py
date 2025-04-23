from flask import Flask, render_template, request, redirect, url_for, session

app = Flask (__name__)

app.secret_key='?'
USER_CREDS = {"username": "Drajat", "password": "secret"}

@app.route('/')
def index():
    return """
    <h1> My simple Website </h1>
    <p> nama <br> kelas <br> npm <br></p>
    <a href="http://127.0.0.1:5000/login"> login here <a>
    """
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USER_CREDS['username'] and password == USER_CREDS['password']:
            session['username'] = username
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', failed=True, username=username)
    else:
        return render_template('login.html')

@app.route('/admin')
def admin():
    if 'username' in session:
        username = session['username']
        return render_template('admin.html', username=username)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)