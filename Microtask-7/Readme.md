# Microtask-7
Install and use elasticdump to download the mapping and data of an ElasticSearch index (it can be anyone created in Microtask 5).

# Procedure
* ```npm install elasticdump -g```. Where ```-g``` directs npm to install the package globally so that it is available as a command line utility.
* ```export NODE_TLS_REJECT_UNAUTHORIZED=0```. This indicates node not to reject unauthorized tls requests. For some reasons the elastic search setup fails to produce a valid ssl cerificate.
* ```elasticdump --input=https://admin:admin@localhost:9200/git_chaoss_enriched --output=/home/abhia/Downloads/es_git_chaoss_enriched_mapping.json --type=mapping```
* ```elasticdump --input=https://admin:admin@localhost:9200/git_chaoss_enriched --output=/home/abhia/Downloads/es_git_chaoss_enriched_data.json --type=data```

# Result
The commands are self-explanatory. The first one installs the elasticdump utility as clu(command line utility, I just made this term up ;) ). The third one dumps the mapping while the fourth one dumps the data. 
The dumps are provided in this directory.

# Attachments
![image](/Microtask-7/image.png)
