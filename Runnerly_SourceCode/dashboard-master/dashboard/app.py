from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/api/runs.json')
@app.route('/api/training.json')
@app.route('/api/races.json')
def _runs():
    run1 = {'title': 'Endurance', 'type': 'training'}
    run2 = {'title': '10K de chalon', 'type': 'race'}
    _data = [run1, run2]
    return jsonify(_data)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
