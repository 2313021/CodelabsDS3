from flask import Flask, request

app = Flask(__name__)

@app.route('/suma')
def suma():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return str(a + b)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
