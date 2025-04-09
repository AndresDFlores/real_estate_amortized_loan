import requests
from bs4 import BeautifulSoup


class RateScrape:

    def __init__(self): 
        pass    


    #  this method initializes the scrape protocol per input url
    def scrape_request(self, url):

        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

        response = requests.get(url=url, headers=header)
        return BeautifulSoup(response.text, 'html.parser')


    @staticmethod
    def get_numeric(str_val):
        return float(''.join([character for character in str_val if character.isnumeric() or character is '.']))


    def scrape_rates(self, loan_term):

        url_summary = f'https://www.bankrate.com/mortgages/mortgage-rates'
        soup = RateScrape.scrape_request(self=self, url=url_summary)

        avg_apr = soup.find('td', {'id': f'brChartMortgage-rate-{loan_term}'})
        return self.get_numeric(str_val=avg_apr.text)


if __name__=='__main__':

    rate_scrape =  RateScrape()

    for loan_term in [30, 15, 10, 51]:
        apr = rate_scrape.scrape_rates(loan_term=loan_term)
        print(apr)
