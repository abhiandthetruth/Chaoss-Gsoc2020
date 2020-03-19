# Microtask-7
Install and use elasticdump to download the mapping and data of an ElasticSearch index (it can be anyone created in Microtask 5).

# Procedure
* ```npm install elasticdump -g```. Where ```-g``` directs npm to install the package globally so that it is available as a command line utility.
* ```export NODE_TLS_REJECT_UNAUTHORIZED=0```. This indicates node not to reject unauthorized tls requests. For some reasons the elastic search with searchguard setup fails to produce a valid ssl cerificate.
* You may do the next steps in either of the below way. The first one involves manual commands while the secomd is uses the script made by me which dumps both the data and mapping of a given index in the directory it is executed in.
  * Manual
    * ```elasticdump --input=https://admin:admin@localhost:9200/git_chaoss_enriched --output=/home/abhia/Downloads/es_git_chaoss_enriched_mapping.json --type=mapping```
    * ```elasticdump --input=https://admin:admin@localhost:9200/git_chaoss_enriched --output=/home/abhia/Downloads/es_git_chaoss_enriched_data.json --type=data```
  * Script
    * Copy the [script](/Microtask-7/dump-elastic.sh) to your working directory and execute the following `chmod +x dump-elastic.sh` then `./dump-elastic.sh [-s] {index_name}`. Enter the `-s` only if you use searchguard else omit it. And ofcourse replace `{index_name}` with the name of the index you wanna dump. For example the equivalent execution of the commands in manual section is `./dump-elastic.sh -s git_chaoss_enriched`. This will dump the files `git_chaosss_enriched_mapping.json` and `git_chaoss_enriched_data.json` in the current directory.
# Result
The commands are self-explanatory. The first one installs the elasticdump utility as clu(command line utility, I just made this term up ;) ). The third one dumps the mapping while the fourth one dumps the data. 
The dumps are provided in this directory.

# Attachments
![image](/Microtask-7/image.png)
