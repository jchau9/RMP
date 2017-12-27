import requests
import urllib

class Weblib:
    def __init__(self, year, dept, div):
        url = 'https://www.reg.uci.edu/perl/WebSoc'
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'identity',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}
        data = {
            'YearTerm': year,
            "Breadth": 'ANY',
            "Dept": dept,
            'Division':div,
            'ShowFinals': 'on',
            'Submit': 'Display Text Results'

        }
        self.response = requests.post(url, data = data, headers = hdr).text

    def get_response(self):
        return self.response

this_year = Weblib('2018-03', 'CSE', '0xx')
print(this_year.get_response())