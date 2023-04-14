from flask import Flask,request
import pandas
# import requests

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def home():
    return"Hello world!"


@app.route('/upload_xl', methods=['POST'])
def upload_excel():
    excel = request.files['file']
    data = pandas.read_excel(excel)
    return data.to_json()


if (__name__ == '__main__'):
    app.run()