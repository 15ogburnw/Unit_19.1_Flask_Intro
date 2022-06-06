# Put your app in here.

from flask import Flask, request
from operations import add, div, sub, mult

app = Flask(__name__)


@app.route('/add')
def add_nums():
    nums = request.args
    a = int(nums.get('a'))
    b = int(nums.get('b'))

    return str(add(a, b))


@app.route('/sub')
def sub_nums():
    nums = request.args
    a = int(nums.get('a'))
    b = int(nums.get('b'))

    return str(sub(a, b))


@app.route('/mult')
def mult_nums():
    nums = request.args
    a = int(nums.get('a'))
    b = int(nums.get('b'))

    return str(mult(a, b))


@app.route('/div')
def div_nums():
    nums = request.args
    a = int(nums.get('a'))
    b = int(nums.get('b'))

    return str(div(a, b))


operations = {'add': add, 'sub': sub, 'mult': mult, 'div': div}


@app.route('/math/<operation>')
def all_ops(operation):
    nums = request.args
    a = int(nums.get('a'))
    b = int(nums.get('b'))

    return str(operations[operation](a, b))
