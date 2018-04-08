import argparse
import json
from datetime import datetime

from libwpt import *

# -------------------------------------
# Run wpt test
# ------------------------------------


class WPTClient(object):

    def __init__(self):

        # Args for all command
        parser = argparse.ArgumentParser(description='Web Page Test Utility')
        parser.add_argument('-e', '--env',
                            help="The env test run against to",
                            default="qa1")

        parser.add_argument('-l', '--label',
                            help="The label for the test",
                            default=datetime.now().strftime('%d-%H-%M'))

        parser.add_argument('-p', '--pages',
                            help="which page you want to test",
                            default="home,srp,vip")

        parser.add_argument('-s', '--script',
                            help="The script will be executed in the test",
                            default='')

        parser.add_argument('-b', '--block',
                            help="The servers will be blocked in the test",
                            default='async-ads.js ads.js advertising prebid adsensecommon.js adnxs.com doubleclick.net pubmatic.com casalemedia.com adservice.google.com adservices.google.com.au demdex.net imrworldwide.com amazonaws.com criteo.com openx.net')

        parser.add_argument('-v', '--vip',
                            help="Specific vip need to be tested",
                            default='')

        parser.add_argument('-r', '--runs',
                            help="Run times for the test",
                            default=3)

        self.config = parser.parse_args()

        with open('../config/env_setup.json', 'r') as f:
            self.env_setup = json.load(f)

    def execute_test(self):
        browsers = ['chrome', 'iPhone6']
        wpt_runner = WPTRunner()
        for page in self.config.pages.split(','):
            for browser in browsers:
                wpt_runner.run_test(self.get_payload(page, browser))

    def get_payload(self, page, browser):

        payload = dict()

        # block 3rd party requests
        payload['block'] = self.config.block

        payload['ignoreSSL'] = 1
        payload['runs'] = self.config.runs

        # disable it avoid the performance impaction from video recording
        payload['video'] = 0

        # Since we only enabled React VIP in non-vertical & non - BS category
        # If you want to test React VIP, please specify the VIP you want to test
        if page == 'vip' and (not self.config.vip):
            url = self.config.vip
        else:
            url = "{domain}{page}".format(domain=self.env_setup['env'][self.config.env], page=self.env_setup['paths'][page])
        payload['url'] = url

        display_label = "{page}_{browser}_{label}".format(page=page, browser=browser, label=self.config.label)
        payload['label'] = display_label

        # Now we only support AB tests setting
        if not self.config.script:
            payload['script'] = self.set_cookie_for_ab_test(url)

        # If it is mobile viewport, mock the 3G fast speed
        if browser == 'iPhone6':
            payload['mobile'] = 1
            payload['mobileDevice'] = 'iPhone6'
            payload['bwDown'] = 1600
            payload['bwUp'] = 768
            payload['latency'] = 150

        return payload

    def set_cookie_for_ab_test(self, url):
        return """setCookie {domain} abtfo=\"{abtests}\"
        navigate\t{url}""".format(domain=self.env_setup['env'][self.config.env], abtests=self.config.script, url=url)


if __name__ == '__main__':
    wpt_client = WPTClient()
    wpt_client.execute_test()