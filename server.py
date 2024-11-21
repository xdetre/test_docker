from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_wrld():
    return 'Hi, Artur'

@app.route('/my_json/')
def get_json():
    return{'Hello': 'Artur'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)