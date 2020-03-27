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
  password = xxxx
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
Done !! Please check the scripts [estocsv.py](https://github.com/abhiandthetruth/Chaoss-Gsoc2020/blob/master/Microtask-8/estocsv.py) and [csvtoxlsheet.py](https://github.com/abhiandthetruth/Chaoss-Gsoc2020/blob/master/Microtask-8/csvtoxlsheet.py), run them to your desire.

Following are the descriptions:
* estocsv.py
  * exports the index documents with only the selected fields.
  * command line parameter `--cfg` to specify path of `config.ini`. You are free to keep your config files anywhere as long as you specify it's path.
* csvtoxlsheet.py
  * Support to export the csv to xlsx and google sheets using the api.
  * Various command line arguments are now supported: 
 ```
--csv : Path to the csv file, required
--gen-xlsx: If specified,  generates the xlsx file
--new-sheet: Name of google sheet to be created, if a new one is to be created
--spreadsheet-id: Id of the spreadsheet the data is to be inserted, if an existing one is going to be used
--coordinates: Co-ordinates on sheet where to add data. If not specified 0, 0 is used.
```
  Clearly either of `--new-sheet` or `--spreadsheet-id` is required. If both are specified `--spreadsheet-id` gets a preference over `--new-sheet`. If neither of them is specified no interaction will take with google sheets api. The spreadsheet id of a spreadsheet can be extracted from the url of the spreadsheet. Maybe I will allow users to specify spreadsheet url in future versions.

Example commands 
```
python3 estocsv.py --cfg ./config.ini
python3 csvtoxlsheet.py --csv ./groupsio_enriched.csv --gen-xlsx --new-sheet groupsio --coordinates 0 5
python3 csvtoxlsheet.py --csv ./groupsio_enriched.csv --spreadsheet-id <spreadsheet-id>
```

Note that you need a `credentials.json` containing the client id and client secret for the api in the working directory for the script to work. You can obtain one from [here](https://developers.google.com/sheets/api/quickstart/python). Click on `enable sheets api` button there. Download the file and paste in the working directory. For the first time, it will attempt to open a new window or tab in your default browser. If this fails, copy the URL from the console and manually open it in your browser. If you are not already logged into your Google account, you will be prompted to log in. If you are logged into multiple Google accounts, you will be asked to select one account to use for the authorization. Click the Accept button. The sample will proceed automatically, and you may close the window/tab.
I will add the documentation later for the latest developments. 
Please review @valeriocos. Thanks
  
  /* I know that there is an elasticsearch helper module present for python but I started it this way so here it is.I am sorry for breaking the pep8 guidline for maximum line length. I usually don't do it :). Will improve it over time.*/
* You can check the exported data in the `{index_name}.csv` which here is, [`groupsio_enriched.csv`](/Microtask-8/groupsio_enriched.csv).
* You have all you wanted.

# Result
You have created raw, enriched indices, exported the selected fields into a csv and converted it into an excel sheet.

# Attachments

![Image](/Microtask-8/image.png)
![Image](/Microtask-8/Microtask-8_kibiter.png)
![Image](/Microtask-8/Microtask-8_csv.png)
![Image](/Microtask-8/Microtask-8_xlsheet.png)
