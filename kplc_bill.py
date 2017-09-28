import argparse

import mechanize
from bs4 import BeautifulSoup

# get user inpur
parser = argparse.ArgumentParser(description='Get KPLC Bill.')
parser.add_argument("account")
args = parser.parse_args()

br = mechanize.Browser()
br.set_handle_robots(False)
br.open("http://www.kplc.co.ke/")

# follow link to Bill page
response1 = br.follow_link(text="Click Here to check your bill")

# select the form using form ID
br.select_form(name="billAmt")
# fill in form
br["billAmt:srn"] = args.account
# submit form
response2 = br.submit()
# read HTML into beautifulsoup
soup = BeautifulSoup(response2.read(), "html5lib")
bill = soup.select_one("div > #billAmt:messages .ui-messages-info-summary")
print(bill.text)
