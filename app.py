from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def index():
  url = request.form['url']
  key_word = request.form['key_word']
  page = requests.get('https://www.bbc.com/news')
  soup = BeautifulSoup(page.content, 'html.parser')
  headlines = soup.find_all('h1', class_='gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text')
  return render_template('index.html', headlines=headlines)


if __name__ == "__main__": 
  app.run(debug=True)
 