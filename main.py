from flask import Flask, render_template, request
from tkinter import filedialog, Tk

import json

app = Flask(__name__)

phone_data = []
phone_results = []
size_list = []


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/choose')
def choose_file():
    filename = get_file()
    sort_file(filename)
    sort_data()
    list_of_phones = add_phone()
    return render_template('display.html', phones=list_of_phones)


def get_file():
    window = Tk()
    window.geometry("10x10")
    window.attributes('-topmost', True)
    filename = filedialog.askopenfilename(initialdir="/", title="Select file")
    return filename


def sort_file(filename):
    with open(filename, 'r') as file:
        for jsonObj in file:
            each_row = json.loads(jsonObj)
            phone_data.append(sort_each_row(each_row))


def sort_each_row(each_row):
    name = each_row['name'].split(' ')
    return [name[0],each_row['screen_inches']]


def add_phone():
    size_list = []
    phone_list = []
    file = []
    phone_size = 0.0
    for data in phone_results:
        if type(data) == float:
            if data is not None:
                size_list.append(data)
                phone_size += float(data)
        else:
            if len(size_list) > 0:
                total = phone_size / len(size_list)
                file.append(round(total, 2))
                size_list = []
                phone_size = 0.0
            if data not in phone_list:
                file = []
                file.append(data)
            phone_list.append(file)

    for phone in phone_list:
        print(f"phone {phone}")
    return phone_list


def sort_data():
    for name in phone_data:
        if name[0] in phone_results:
            phone_results.append(name[1])
        else:
            phone_results.append(name[0])
            phone_results.append(name[1])


if __name__ == '__main__':
    app.run(debug=True)