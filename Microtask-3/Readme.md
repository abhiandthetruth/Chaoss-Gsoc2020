# Microtask-3
Based on the JSON documents produced by Perceval and its source code, try to answer the following questions:

* What is the meaning of the JSON attribute 'timestamp'?
* What is the meaning of the JSON attribute 'updated_on'?
* What is the meaning of the JSON attribute 'origin'?
* What is the meaning of the JSON attribute 'category'?
* How many categories do the GitHub and GitLab backends have?
* What is the meaning of the JSON attribute 'uuid'?
* What is the meaning of the JSON attribute search_fields?
* What is stored in the attribute data of each JSON document produced by Perceval?

# Procedure

* Going through the documentations and code.

# Result

* The attribute 'timestamp' is the unix timestamp(zone - utc) of the moment the request is processed.
* The attribute 'updated_on' is the unix timestamp(zone - utc) of the last update in the repository. It could be a commit, change in details, access properties of the repository. Since the github api provides the updated_on attribute in utc too, it makes conversions easy.
* The attribute 'origin' is the actual url of the repo.
* The attribute 'category' of the response corresponds to the 'category' parameter of the request, which denotes whether the requested information is about 'issue' or 'pull_request'(in case of github and gitlab backends)).
* There are three categories for the github backend 'issue', 'repsitory' and 'pull_request', whreas the gitlab backends have two categories 'issue', 'merge_request'.
* In the perceval.backend package there is a method 'uuid' that converts the concatenation of list of arguments( with a ':' between each string) to it's SHA1. Each argument must be a non-empty string. In this case it is the uuid formed by passing the arguments 'origin'( explained above), 'metadata_id'( it is the identifier extracted from github item which is the github response for the issue in consideration). As the name stands universal unique identifier, it is used to uniquely identify the object on the internet.
* As I can see it the search fields contain the information about our request item, the 'owner', 'repo' and the 'item_id' which is the id obtained by the metadata_id method which in turn is the id asociated with the github item explained above. In general it contains the key value pairs of the keys present in the search_fields attribute of the class. This helps in querying data since it we can quickly search look only in the search fields of an item instead of whole item inspection.
* In the code the 'data' attribute is being assigned the github item itself i.e it contains all the data github sent for that particular issue as it is with all its fields, i.e. 'id', 'node_id', 'number', 'title', 'user' etc.
