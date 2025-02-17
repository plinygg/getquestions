from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

def getHTMLDocument(url):
    response = requests.get(url)
    return response.text

def find_q(url) -> list:
    page = requests.get(url).content

    soup = BeautifulSoup(page)

    labels = soup.find_all('div', {'class': 'form-label'})
    res = []
    for label in labels:
        lab = label.find('label')
        lab2 = lab.text
        res.append(lab2[1:])
    return res

@app.route('/')
def view_form():
    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == "POST":
        url = request.form['url']
        res = find_q(url)
        return res
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

