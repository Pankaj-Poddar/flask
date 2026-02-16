from flask import Flask, render_template, request, redirect, url_for, session,Response

app = Flask(__name__)
app.secret_key='supersecretkey'

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect(url_for('Welcome'))
        else:
            return Response('Invalid credentials', status=401)
    
    return '''
        <h2>Login Page</h2>   
        <form method='POST'>
        username: <input type='text' name='username'><br>
        password: <input type='password' name='password'><br>
        <input type='submit' value='Login'>
        </form>    
        '''

@app.route('/welcome')
def Welcome():
    if session.get('logged_in'):
        return "Welcome, you are logged in!"
    else:
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))
