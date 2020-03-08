# Microtask-6
Using the dev tools in Kibiter, create a query that counts the number of unique authors on a Git repository from 2018-01-01 until 2019-01-01.

# Procedure
* Navigate to ```https://admin:admin@localhost:5601/```. Login as user 'admin' password 'admin'.
* Go to dev-tools in the left nav-bar.
* I had created to indices with ```git``` backend, one of which was the the ```git_chaoss_enriched``` and the other was the raw one. Type in the following query
```
GET git_chaoss_enriched/_search
{
  "query": {
    "range": {
      "author_date": {
        "gte": "2018-01-01T00:00:00",
        "lte": "2019-01-01T00:00:00"
      }
    }
  },
  "aggs": {
    "author_count": {
      "cardinality": {
        "field": "author_id"
      }
    }
  }
}
```
* Run the query using the run button.

# Result
```
{
...
...
"aggregations": {
    "author_count": {
      "value": 21
    }
  }
 }
 ```
 We can see the total number of different authors here along with the results of the query.
 
 # Attachments
 
 ![image](/Microtask-6/image.png)
