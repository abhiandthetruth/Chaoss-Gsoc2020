# Microtask-8
Execute micro-mordred to collect and enrich data from a groupsio repository. You need to register to a group (e.g., https://lists.onap.org/g/main) and follow the instructions at https://github.com/chaoss/grimoirelab-sirmordred#groupsio. Then, write a script to read the enriched index and import the attributes uuid, project, project_1, origin, grimoirelab_creation_date, body and subject_analyzed to a CSV file. Import the obtained file to an excel sheet (in a manual or automatic way).

# Procedure (All the examples provided were used by me) 
* Signup to groups.io
* Join some groups who have the `download_archives` permission `true` by default, you can check your subscription and the available permission using [this](https://gist.github.com/valeriocos/ad33a0b9b2d13a8336230c8c59df3c55) script. Alternatively you can ask the owner of your group to enable the permission.
* Define the `groupsio` section in `setup.cfg`. See the example below for reference
  ```
  [general]
  short_name = abhi
  update = false
  min_update_delay = 10
  debug = True
  logs_dir = logs
  bulk_size = 100
  scroll_size = 100
  menu_file = ../menu.yaml
  aliases_file = ../aliases.json

  [projects]
  projects_file = ./projects.json

  [es_collection]
  url = http://localhost:9200

  [es_enrichment]
  url = http://localhost:9200

  [sortinghat]
  host = 127.0.0.1
  user = root
  password = leosingh
  database = abhi_shdb
  load_orgs = true
  orgs_file = data/orgs_sortinghat.json
  identities_api_token = 'xxxx'
  identities_file = [data/perceval_identities_sortinghat.json]
  affiliate = true
  # commonly: Unknown
  unaffiliated_group = Unknown
  autoprofile = [customer,git,github]
  matching = [email]
  sleep_for = 120

  [phases]
  collection = true
  identities = true
  enrichment = true
  panels = false


  [groupsio]
  raw_index = groupsio_raw
  enriched_index = groupsio_enriched
  email = abhiandthetruth@gmail.com
  password = xxxx
  ```
  /* I have switched to the without searchguard version of elasticsearch hence the urls are changed in this config. */
* List down those groups in the `projects.json`. See the below example for reference
  ```
  {
    "abhi": {
        "groupsio": [
            "onap",
            "zabiplane"
        ]
    }
  }
  ```
* Execute `micro.py --raw --enrich --cfg ./setup.cfg --backends groupsio`. Note that you need the dev environment setup. If you haven't then see Microtask-4.
* You can check both the raw and enriched indices are created.
* Now define a `config.ini` in the following format
  ```
  [elastic_search]
  url = http://localhost:9200
  index = groupsio_enriched
  fields = uuid, project, project_1, origin, grimoirelab_creation_date, body_extract, Subject_analyzed
  ```
* Execute the [`estocsv.py`](/Microtask-8/csvtoxlsheet.py). Here is the content of the script, for easier access
  ```
  import requests
  import json,csv
  from configparser import ConfigParser

  # Get the parser ready 
  config = ConfigParser()
  config.read('/home/abhia/Documents/config.ini')

  # Getting the Global Declarations
  ELASTIC_SEARCH_URL = config.get('elastic_search', 'url')
  INDEX = config.get('elastic_search', 'index')
  FIELDS = [string.strip() for string in config.get('elastic_search', 'fields').split(',')]
  HEADER = {'Content-Type':'application/json'}
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
      """Retrieves all the hits given the global params"""
      url = ELASTIC_SEARCH_URL + "/" + INDEX + "/_search?scroll=1m&size=" + str(size)
      r = SESSION.post(url, data=json.dumps(PAYLOAD), headers=HEADER)
      raw_data = r.json()
      total_hits = raw_data['hits']['hits']
      scroll_id = raw_data['_scroll_id']
      scroll_url = ELASTIC_SEARCH_URL + "/_search/scroll"
      scroll_payload = {
          "scroll" : "1m", 
          "scroll_id" : scroll_id
      }
      while True:
          r = SESSION.post(scroll_url, data=json.dumps(scroll_payload), headers=HEADER)
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
      """The main function which manages the tasks"""
      hits = get_hits()
      generate_csv(hits, INDEX)
      print("Done!!")

  if __name__ == "__main__":
      main()
  ```
  /* I know that there is an elasticsearch helper module present for python but I started it this way so here it is.I am sorry for breaking the pep8 guidline for maximum line length. I usually don't do it :). Will improve it over time.*/
* You can check the exported data in the `{index_name}.csv` which here is, [`groupsio_enriched.csv`](/Microtask-8/groupsio_enriched.csv).
* Now to make it into an excel sheet execute the file [`csvtoxlsheet.py`](/Microtask-8/csvtoxlsheet.py). It uses the dependency `xlsxwriter`./* Thanks to http://coderscrowd.com/app/public/codes/view/201 for a solid reference :).*/
* You have all you wanted.

# Result
You have created raw, enriched indices, exported the selected fields into a csv and converted it into an excel sheet.

# Attachments

![Image](/Microtask-8/image.png)
![Image](/Microtask-8/Microtask-8_kibiter.png)
![Image](/Microtask-8/Microtask-8_csv.png)
![Image](/Microtask-8/Microtask-8_xlsheet.png)
