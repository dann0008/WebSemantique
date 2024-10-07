import json
from multiprocessing import Pool

import pandas as pd

from utils.logger import logger

def parse_event(event, sex):
    logger.info(event)
    print(event)
    if event in ["100-metres","200-metres","400-metres"]:
        category = "sprints"
        condition = "outdoor"
    elif event in ["100-metres-hurdles", "400-metres-hurdles", "110-metres-hurdles"]:
        category = "hurdles"
        condition = "all"
    page = 0
    df_list = []
    while True:
        page += 1
        url = f"""https://worldathletics.org/records/all-time-toplists/{category}/{event}/{condition}/{sex}/senior?regionType=world&timing=electronic&windReading=regular&page={page}&bestResultsOnly=false&firstDay=2000-01-01&lastDay=2024-09-29"""
        try:
            print(url)
            df = pd.read_html(url)
            df_list.append(df[0])
        except Exception:
            logger.info(len(df_list))
            df = pd.concat(df_list)
            df.to_csv(f"data/{sex}/{event}.csv")
            logger.info(f"Written {event} to csv")
            break


def parse_event_men(event):
    parse_event(event, "men")


def parse_event_women(event):
    parse_event(event, "women")


if __name__ == "__main__":
    with open("data/options.json") as f:
        data = json.load(f)

    events_male = data[7]["cases"][0]["values"]
    event_male_urls = [ev["disciplineNameUrlSlug"] for ev in events_male]
    print(event_male_urls)
    #with Pool(8) as p:
    #    print(p.map(parse_event_men, event_male_urls))
    events_female = data[7]["cases"][24]["values"]
    event_female_urls = [ev["disciplineNameUrlSlug"] for ev in events_female]
    with Pool(8) as p:
        print(p.map(parse_event_women, event_female_urls))
