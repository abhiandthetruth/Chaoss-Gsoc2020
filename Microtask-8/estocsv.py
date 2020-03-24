import requests
import argparse, sys
import json,csv
from configparser import ConfigParser

# Global variables
SESSION = requests.Session()

def get_args():
    """
    Get params from cli required for exexution of module
    :argument --cfg: Path to config.ini
    """

    parser = argparse.ArgumentParser(description="Get the path to cfg")
    parser.add_argument('--cfg', dest='cfg_path', 
                        help="Path to config.ini")
    if len(sys.argv) == 0:
        parser.print_help()
        sys.exit()
    args = parser.parse_args()
    return args

def get_hits(es_url, index, fields, size=100):
    """
    Get all hits from elastic search for a given index
    
    This function returns all hits i.e., records for a given 'index' containing only the
    'fields' specified where the total records in each response equals 'size'. 
    
    :param es_url: url to connect elastic search
    :param index: the index from which records are to be retrieved
    :param fields: the list of fields that need to fetched from the index
    :param size: the size of response to fetch
    """

    url = es_url + "/" + index + "/_search?scroll=1m&size="+str(size)
    payload = {
            "_source": {
                "includes": fields
            },
            "query" : {
                "match_all" : {}
            }
        }
    r = SESSION.post(url, data=json.dumps(payload), headers={'Content-Type':'application/json'})
    raw_data = r.json()
    total_hits = raw_data['hits']['hits']
    scroll_id = raw_data['_scroll_id']
    scroll_url = es_url + "/_search/scroll"
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
    """
    Generates the csv file from a set of JSON documents
    
    This function receives as input a list of JSON 
    documents, and stores them to a CSV file, which name 
    is defined by the attribute `filename`.

    :param hits: a list of JSON documents
    :param filename: the output file where to store the CSV data
    """

    headers = [key for key in hits[0]['_source']]
    records = [headers]
    for hit in hits:
        record_dict = hit['_source']
        record = [value for value in record_dict.values()]
        records.append(record)
    with open(filename+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(records)

def main(config):
    """
    Get the params from config and execute the module
    
    :param config: the parser for the configuration file
    """ 

    es_url = config.get('elastic_search', 'url')
    index = config.get('elastic_search', 'index')
    fields = [string.strip() for string in config.get('elastic_search', 'fields').split(',')]
    hits = get_hits(es_url, index, fields)
    generate_csv(hits, index)
    print("Done!!")

if __name__ == "__main__":
    args = get_args()
    config = ConfigParser()
    config.read(args.cfg_path)
    main(config)

