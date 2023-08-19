from flask import Flask

app = Flask(__name__)

@app.route('/my')
def entry_point():
    return "hello world"


if __name__ == '__main__':
    app.run(port=3000)