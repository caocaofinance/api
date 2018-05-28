# -*- coding: utf-8 -*- 
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return render_template('index.html')
@app.route('/api/news')
def games():
    return jsonify(result=['a','b'])
if __name__ == '__main__':
    app.run(port=80,debug=True)