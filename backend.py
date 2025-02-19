from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
import os


app = Flask(__name__)

def getHTMLDocument(url):
    response = requests.get(url)
    return response.text

def find_q(url) -> list:
    page = requests.get(url).content

    soup = BeautifulSoup(page, 'html.parser')

    labels = soup.find_all('div', {'class': 'form-label'})
    res = []
    for label in labels:
        lab = label.find('label')
        lab2 = lab.text
        res.append(lab2)
    return res

@app.route('/')
def view_form():
    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == "POST":
        url = request.form['url']
        res = find_q(url)
        # file_path = os.path.join("templates", "output.html")
        # with open(file_path, "w", encoding='utf-8') as file:
        #     for line in res:
        #         file.write(line)
        new = BeautifulSoup("<!DOCTYPE html><html><head><h1>Here are the questions for you to copy and paste:</h1><head><body></body><html>", "html.parser")
        for line in res:
            lein = new.new_tag('p')
            lein.string = line
            new.html.body.append(lein)
        return render_template(new)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

