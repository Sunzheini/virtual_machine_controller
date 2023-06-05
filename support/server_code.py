from flask import Flask, request


app = Flask(__name__)


@app.route('/command', methods=['POST'])
def command():
    data = request.get_json(force=True)
    cmd = data['command']

    print('received command: {}'.format(cmd))

    return {"result": "success"}


if __name__ == '__main__':
    print('started')
    app.run(host='0.0.0.0', port=5000)
