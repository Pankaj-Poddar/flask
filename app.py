from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello User !! This is my first flask app"

@app.route('/about')
def about():
    return "This is the about page"

@app.route('/contact')
def contact():
    return "Hello User !! This is contact page"

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        data = request.form
        return f"Data received: {data}"
    else:
        return "Please submit the form using POST method"

if __name__ == '__main__':
    app.run(debug=True)
