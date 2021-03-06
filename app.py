from flask import Flask, Response, json, jsonify, request
from flask_bootstrap import Bootstrap
from flask import render_template
import csv


app = Flask(__name__)
Bootstrap(app)

template = 'index.html'
    
def get_csv(st):
    csv_file = open(st, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

@app.route("/", methods = ['GET', 'POST'])
def index1():
    object_list = get_csv('./static/assets/data/asansol.csv')
    return render_template(template, object_list=object_list)


@app.route("/fuljhore", methods = ['GET', 'POST'])
def index2():
    object_list = get_csv('./static/assets/data/fuljhore.csv')
    return render_template(template, object_list=object_list)


@app.route("/durgapur", methods = ['GET', 'POST'])
def index3():
    object_list = get_csv('./static/assets/data/durgapur.csv')
    return render_template(template, object_list=object_list)


if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run(debug=True)
