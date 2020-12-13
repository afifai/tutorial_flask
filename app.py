from flask import Flask
app = Flask(__name__)

@app.route('/halo')
def hello_world():
    return '<h5>Hello, NgodingPython!</h5>'

@app.route('/')
def home():
    return '<p>Nama Saya Afif</p>'

if __name__ == '__main__':
    app.run(debug=True, port=1234)
