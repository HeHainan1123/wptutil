import requests
from bs4 import BeautifulSoup


class WPTRunner(object):

    def __init__(self):

        self.wpt_server = "https://www.webpagetest.org/"

        self.api_endpoint = "/runtest.php?"

    def run_test(self, payload):

        response = requests.post(self.wpt_server + self.api_endpoint, payload)
        if not response.status_code == 200:
            raise Exception("Failed to run web page test: Request returned HTTP-{}: {}".format(response.status_code, response.text))

        soup = BeautifulSoup(response.text, 'html.parser')
        # result_id = (soup.find('a', title='Test Result'))['href']

        # test_result[page + '_' + browser] = result_id

        print('\n Test Result: ' + self.wpt_server + (soup.find('a', title='Test Result'))['href'] + '\n')

