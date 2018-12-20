from flask import Flask, Response
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/")
def index():
    resp = scrape_releases()
    return Response(resp, mimetype='text/plain')


def scrape_releases():
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'DNT': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,pt;q=0.7',
    }

    page = requests.get('https://www.dvdsreleasedates.com/', headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    requested_table = soup.find("div", {"id": 'requested'})
    requested_hrefs = requested_table.find_all('a')
    movie_names = [ movie.contents[0].replace(' ', '?') + "*," for movie in requested_hrefs ]

    return movie_names


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)

