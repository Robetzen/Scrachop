from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

<<<<<<< HEAD
@app.route('/h')  
=======

 
@app.post('/')  
>>>>>>> ccff61dd6d8120c803dfcab3cf80d72d8e9070dc
def index():
  page = requests.get('https://www.bbc.com/news')
  soup = BeautifulSoup(page.content, 'html.parser')
  headlines = soup.find_all('h1', class_='gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text')
  return render_template('index.html', headlines=headlines)
<<<<<<< HEAD
 
=======
>>>>>>> ccff61dd6d8120c803dfcab3cf80d72d8e9070dc

if __name__ == "__main__": 
  app.run(debug=True)
 