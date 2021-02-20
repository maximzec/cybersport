import requests
from bs4 import BeautifulSoup
from headers import headers

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

# TODO: Придумать как добавить дату в турнир


def parse_on_going_events():
    session = requests.session()
    response = session.get(url_link, headers=headers)
    events = {}
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find('div', id=gen_tab(tab))
        for event in table.find_all('div', class_='content standard-box'):
            event_name = event.find('div', class_='text-ellipsis').text
            events[event_name] = None
        return str(events)

    else:
        return "Not successful status code:" + response.status_code


print(parse_on_going_events())
