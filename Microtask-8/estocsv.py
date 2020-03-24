import requests
import json,csv
from configparser import ConfigParser

# Get the parser ready 
config = ConfigParser()
config.read('/home/abhia/Documents/config.ini')

# Getting the Global Parameters
ELASTIC_SEARCH_URL = config.get('elastic_search', 'url')
INDEX = config.get('elastic_search', 'index')
FIELDS = [string.strip() for string in config.get('elastic_search', 'fields').split(',')]
SESSION = requests.Session()
PAYLOAD = {
            "_source": {
                "includes": FIELDS
            },
            "query" : {
                "match_all" : {}
            }
        }


def get_hits(size=100):
    """Returns all hits given index, fields, url globally and passed size of one fetch"""
    url = ELASTIC_SEARCH_URL + "/" + INDEX + "/_search?scroll=1m&size="+str(size)
    r = SESSION.post(url, data=json.dumps(PAYLOAD), headers={'Content-Type':'application/json'})
    raw_data = r.json()
    total_hits = raw_data['hits']['hits']
    scroll_id = raw_data['_scroll_id']
    scroll_url = ELASTIC_SEARCH_URL + "/_search/scroll"
    scroll_payload = {
        "scroll" : "1m", 
        "scroll_id" : scroll_id
    }
    while True:
        r = SESSION.post(scroll_url, data=json.dumps(scroll_payload), headers={'Content-Type':'application/json'})
        raw_data = r.json()
        scroll_id = raw_data['_scroll_id']
        hits = raw_data['hits']['hits']
        if len(hits) < 1:
            break
        total_hits.extend(hits)
    return total_hits

def generate_csv(hits, filename):
    """Generates the csv given the hits with filename as the name"""
    headers = [key for key in hits[0]['_source']]
    records = [headers]
    for hit in hits:
        record_dict = hit['_source']
        record = [value for value in record_dict.values()]
        records.append(record)
    with open(filename+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(records)

def main():
    """The main function"""
    hits = get_hits()
    generate_csv(hits, INDEX)
    print("Done!!")

if __name__ == "__main__":
    main()

