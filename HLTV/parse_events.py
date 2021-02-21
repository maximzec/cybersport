import requests
from bs4 import BeautifulSoup
from constants.headers import headers
from pprint import pprint
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
        for month in months:
            month_headline = month.find('div', class_='standard-headline').text
            upcoming_events[month_headline] = {}
            for month_event in month.find_all('a', 'a-reset small-event standard-box'):
                event_name = month_event.find(
                    'div', class_='text-ellipsis').text
                event_url = month_event['href']
                event_teams = month_event.find(
                    'td', class_='col-value small-col').text
                event_pool = month_event.find(
                    'td', class_='col-value small-col prizePoolEllipsis').text
                event_status = month_event.find(
                    'td', class_='col-value small-col gtSmartphone-only').text
                upcoming_events[month_headline][event_name] = {}
                upcoming_events[month_headline][event_name]['url'] = 'htlv.org' + event_url
                upcoming_events[month_headline][event_name]['teams'] = event_teams
                upcoming_events[month_headline][event_name]['pool'] = event_pool
                upcoming_events[month_headline][event_name]['status'] = event_status
        return upcoming_events
    else:
        return "Not successful status code" + response.status_code


# print(parse_on_going_events())
pprint(parse_upcoming_events())
