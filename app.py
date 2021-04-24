from flask import Flask, render_template, request, jsonify
import time
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/',methods=['GET','POST'])
def hello_world():
    template_data = {}
    return render_template('main.html', **template_data)

@app.route('/add', methods=['GET','POST'])
def add():
    print('add')
    json_data = request.json
    return json_data

if __name__ == "__main__":
    port = None
    app.run(host='0.0.0.0', port=5000,threaded=True)