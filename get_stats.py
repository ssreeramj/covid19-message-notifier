import requests
from bs4 import BeautifulSoup

WORLD_URL = 'https://worldometers.info/coronavirus'
INDIA_URL = 'https://www.worldometers.info/coronavirus/country/india/'

url_list = [WORLD_URL, INDIA_URL]

def get_counts():
    counts = {}
    
    for name, url in zip(['world', 'india'], url_list):

        resp = requests.get(url).text

        soup = BeautifulSoup(resp, 'html5lib')

        infected_span = soup.find('div', attrs={'class': 'maincounter-number'}).find('span')
        infected_stats = infected_span.text.strip()

        deaths_span = infected_span.findNext('span')
        deaths_stats = deaths_span.text.strip()

        recovered_span = deaths_span.findNext('span')
        recovered_stats = recovered_span.text.strip()

        counts[name] = (infected_stats, deaths_stats, recovered_stats)

        print(f'{name} counts scraped...')

    print('data scrapped successfully')
    return counts

