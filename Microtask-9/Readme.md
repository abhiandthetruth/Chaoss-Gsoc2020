# Microtask-9
Build a Data Table visualization in Kibiter (you can use the CHAOSS community dashboard) that shows for emails (mbox index) the text of emails (split row by Termbody_extract field).

# Procedure
* Go to the visualize wizard from the left-navbar.
* Click on the ```+``` button to create new visualization.
* Select ```Data Table``` under Data visuaslization type.
* Select the index. In my case it is ```git_chaoss_enriched```.
* A default metric ```count``` is already added. Add a bucket by selecting ```split rows```.
* Choose the ```aggregation``` as ```Terms```.
* Select the field to aggregate upon. In my case it is `Author_name`. Increase the size as required.
* Add metrics if needed like I added `Average lines_changed`. You can do this by clicking `add metrics`, selecting the `aggregation`(here `Average`), and then the field to be aggregated upon(`lines_changed`).
* Click on the visualize button to visualize.\
* You can change the entries `Per Page`, `sum function` attribute in the option tab. The uses are self explanatory.

# Result
A data table is generated with the desired attributes.

# Attachments
![image](/Microtask-9/image.png)
