import requests
from bs4 import BeautifulSoup
from constants.headers import headers

tab = 'All'


def gen_tab(tab):
    tabs = {
        "Featured": "FEATURED",
        "Today": "TODAY",
        "All": "ALL"
    }
    assert tab in tabs.keys()
    return tabs[tab]


url_link = "https://www.hltv.org/events#tab-FEATURED"
session = requests.session()
# TODO: Придумать как добавить дату в турнир


def parse_on_going_events():
    response = session.get(url_link, headers=headers)
    ongoing_events = {}
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find('div', id=gen_tab(tab))
        for event in table.find_all('a', class_='a-reset ongoing-event'):
            event_url = event['href']
            event_name = event.find('div', class_='text-ellipsis').text
            ongoing_events[event_name] = 'htlv.org' + event_url
        return str(ongoing_events)

    else:
        return "Not successful status code:" + response.status_code


def parse_upcoming_events():
    response = session.get(url_link, headers=headers)
    upcoming_events = {}
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        months = soup.find_all('div', class_='events-month')
        for month in soup.find_all('div', class_='events-month'):
            month_headline = soup.find('div', class_='standard-headline').text
            upcoming_events[month_headline] = {}

        return upcoming_events
    else:
        return "Not successful status code" + response.status_code


# print(parse_on_going_events())
print(parse_upcoming_events())
