"""
Flask app that checks Venmo handle validity. A user can input a list of Venmo
handles and will receive a table showing which handles are valid. 
"""


from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import re
import requests
from scipy.stats import poisson
import time

VENMO_URL = "https://account.venmo.com/u/{}"
handle_pattern = re.compile(r'([A-Za-z0-9_\\-]+)')

#Avoid CloudFlare blocks
headers = requests.utils.default_headers()
headers.update({
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0',
})

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        handles = request.form.get('handles')
        parsed_handles = handle_pattern.findall(handles)
        results = []

        for handle in parsed_handles:
            result = {}
            response = requests.get(VENMO_URL.format(handle), headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            if "Sorry, the page you requested does not exist!" in response.text:
                result['handle'] = handle
                result['valid'] = False
            else:
                name = soup.find('p', class_='profileInfo_username__G9vVA').text
                img = soup.find('img', class_='MuiAvatar-img')['src']

                result['handle'] = handle
                result['name'] = name
                result['img'] = img
                result['valid'] = True

            results.append(result)
            time.sleep(poisson.rvs(1.5))

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)

